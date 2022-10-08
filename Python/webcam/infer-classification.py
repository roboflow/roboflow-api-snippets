import json
import cv2
import base64
import requests
import time

# Check to be sure your config file contains details for a Classification Model trained with Roboflow Train
# https://docs.roboflow.com/train | https://docs.roboflow.com/inference-classification/hosted-api
# load config file:
with open('roboflow_config.json') as f:
    config = json.load(f)

    ROBOFLOW_API_KEY = config["ROBOFLOW_API_KEY"]
    ROBOFLOW_MODEL = config["ROBOFLOW_MODEL"]
    ROBOFLOW_SIZE = config["ROBOFLOW_SIZE"]

    FRAMERATE = config["FRAMERATE"]
    BUFFER = config["BUFFER"]

# Construct the Roboflow Infer URL
# (if running locally replace https://classify.roboflow.com/ with eg http://127.0.0.1:9001/)
upload_url = "".join([
    "https://classify.roboflow.com/",
    ROBOFLOW_MODEL,
    "?api_key=",
    ROBOFLOW_API_KEY,
    "&format=image",
    ])

# Get webcam interface via opencv-python
video = cv2.VideoCapture(0)

# Infer via the Roboflow Infer API and return the result
def infer():
    # Get the current image from the webcam
    ret, img = video.read()
    image = img.copy()

    # Resize (while maintaining the aspect ratio) to improve speed and save bandwidth
    height, width, channels = img.shape
    scale = ROBOFLOW_SIZE / max(height, width)
    img = cv2.resize(img, (round(scale * width), round(scale * height)))

    # Encode image to base64 string
    retval, buffer = cv2.imencode('.jpg', img)
    img_str = base64.b64encode(buffer)

    # Get prediction from Roboflow Infer API
    resp = requests.post(upload_url, data=img_str, headers={
        "Content-Type": "application/x-www-form-urlencoded"
    }, stream=True)
    # Convert Response to JSON
    preds = resp.json()
    
    # Add predictions (class label and confidence score) to image
    (text_width, text_height), _ = cv2.getTextSize(
        f"{preds['top']} conf: {preds['confidence']}",
        fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, thickness=2)
    
    text_location = (5, text_height)
    
    cv2.putText(image, f"{preds['top']} | conf: {preds['confidence']}",
                text_location, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8,
                color=(255,255,255), thickness=2)   

    return image


# Main loop; infers sequentially until you press "q"
while 1:
    # On "q" keypress, exit
    if(cv2.waitKey(1) == ord('q')):
        break

    # Capture start time to calculate fps
    start = time.time()

    # Synchronously get a prediction from the Roboflow Infer API
    image = infer()
    # And display the inference results
    cv2.imshow('image', image)

    # Print frames per second
    print((1/(time.time()-start)), " fps")

# Release resources when finished
video.release()
cv2.destroyAllWindows()
