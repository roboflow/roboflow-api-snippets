
import io
import logging
import socketserver
from threading import Condition, Thread
from http import server

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            print(True)
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)
            
def MakeStreamingHandler(output):
    class StreamingHandler(server.BaseHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
             super(StreamingHandler, self).__init__(*args, **kwargs)
             self.output = output
             
        page = PAGE="""\
                <html>
                <head>
                <title>roboflowoak Stream View</title>
                </head>
                <body>
                <center><img src="stream.mjpg"></center>
                </body>
                </html>
            """
        content = page.encode('utf-8')

        def do_GET(self):
            if self.path == '/':
                self.send_response(301)
                self.send_header('Location', '/index.html')
                self.end_headers()
            elif self.path == '/index.html':
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', len(self.content))
                self.end_headers()
                self.wfile.write(self.content)
            elif self.path == '/stream.mjpg':
                self.send_response(200)
                self.send_header('Age', 0)
                self.send_header('Cache-Control', 'no-cache, private')
                self.send_header('Pragma', 'no-cache')
                self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
                self.end_headers()
                try:
                    while True:
                        with output.condition:
                            output.condition.wait()
                            frame = output.frame
                        self.wfile.write(b'--FRAME\r\n')
                        self.send_header('Content-Type', 'image/jpeg')
                        self.send_header('Content-Length', len(frame))
                        self.end_headers()
                        self.wfile.write(frame)
                        self.wfile.write(b'\r\n')
                except Exception as e:
                    logging.warning(
                        'Removed streaming client %s: %s',
                        self.client_address, str(e))
            else:
                self.send_error(404)
                self.end_headers()
    
    return StreamingHandler

class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True
    
    def serve_forever(self, *k, **kw) -> None:
        Thread(target=super().serve_forever, args=k, kwargs=kw).start()
        