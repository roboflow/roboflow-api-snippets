# Python Webcam Inference Examples
These scripts demonstrate how to use the Roboflow Infer API to get predictions
from a live webcam feed.

![python-webcam](https://user-images.githubusercontent.com/870796/112769782-7d29ad00-8fe8-11eb-8233-2e1b81781dd6.gif)

## Installation
Install the requirements with pip3 ([`infer-async.py`](infer-async.py) requires
Python 3.7+ for [asyncio](https://docs.python.org/3/library/asyncio.html) support.)
```
pip install -r requirements.txt
```

## Configuration
Create a `roboflow_config.json` file with your Roboflow API key, model name, and
model size (defaults to 416 if you didn't use a `resize` preprocessing step
when you created your Version in Roboflow).

## Usage

**[`infer-simple.py`](infer-simple.py)** does inference sequentially; meaning it
waits for the predictions from the previous frame before sending another.
The framerate depends on the latency between your machine and the Inference API.

In our tests, we saw ~4 fps with the Roboflow
[Hosted API](https://docs.roboflow.com/inference/hosted-api)
and ~8 fps with an NVIDIA Jetson Xavier NX running the
[on-prem Roboflow Infer API](https://docs.roboflow.com/inference/nvidia-jetson).

**[`infer-async.py`](infer-async.py)** does inference in parallel using a frame
buffer which you can configure in your `roboflow_config.json`. You should be able
to achieve arbitrary framerates by adjusting the buffer size.
