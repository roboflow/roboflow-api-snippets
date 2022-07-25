## Luxonis OAK with MJPEG Streaming Example

This script demonstrates how to incorporate MJPEG streaming into a Roboflow + Luxonis OAK system. This is
especially useful when the host is headless (no external display). In this case, the detection visualization
can conveniently be accessed over a local network.

If indeed run on a headless host, ensure that cv2.imshow calls are removed (the script will crash since there
is no display).
