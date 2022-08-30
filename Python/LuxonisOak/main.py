from roboflowoak import RoboflowOak
import cv2
import time
import numpy as np

from stream_utils import MakeStreamingHandler, StreamingOutput, StreamingServer

if __name__ == '__main__':
    # instantiating an object (rf) with the RoboflowOak module
    rf = RoboflowOak(model="[MODEL]", confidence=0.05, overlap=0.5,
    version="[VERSION]", api_key="[API_KEY]", rgb=True,
    depth=True, device=None, blocking=True)
    
    # Create our MPEG streaming server
    # The stream will be available at http://localhost:8000/stream.mjpg by default
    output = StreamingOutput()
    address = ('', 8000) # Change 8000 to the port you want to serve the MPJEG stream on
    StreamingHandler = MakeStreamingHandler(output)
    server = StreamingServer(address, StreamingHandler)
    server.serve_forever()
    
    # Running our model and displaying the video output with detections
    while True:
        t0 = time.time()
        # The rf.detect() function runs the model inference
        result, frame, raw_frame, depth = rf.detect(visualize=True)
        predictions = result["predictions"]
        #{
        #    predictions:
        #    [ {
        #        x: (middle),
        #        y:(middle),
        #        width:
        #        height:
        #        depth: ###->
        #        confidence:
        #        class:
        #        mask: {
        #    ]
        #}
        #frame - frame after preprocs, with predictions
        #raw_frame - original frame from your OAK
        #depth - depth map for raw_frame, center-rectified to the center camera

        # timing: for benchmarking purposes
        t = time.time()-t0
        print("FPS ", 1/t)
        print("PREDICTIONS ", [p.json() for p in predictions])

        # Uncomment the follow two lines to enable
        # the optional depth view
        # max_depth = np.amax(depth)
        # cv2.imshow("depth", depth/max_depth)
        
        # displaying the video feed as successive frames
        cv2.imshow("frame", frame)
        
        # pass the latest frame to the MJPEG stream
        output.write(cv2.imencode('.JPEG', frame)[1].tobytes())

        # how to close the OAK inference window / stop inference: CTRL+q or CTRL+c
        if cv2.waitKey(1) == ord('q'):
           break
        
