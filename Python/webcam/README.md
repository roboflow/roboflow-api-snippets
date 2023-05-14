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
model size (defaults to `416` if you didn't use a `Resize` [preprocessing step](https://docs.roboflow.com/image-transformations/image-preprocessing)
when you created your Version in Roboflow).
* [Resize - Roboflow Documentation](https://docs.roboflow.com/image-transformations/image-preprocessing#resize) | [Selecting a Resize value](https://blog.roboflow.com/you-might-be-resizing-your-images-incorrectly/)

## Usage

### [Object Detection](https://docs.roboflow.com/inference/hosted-api)
**[`infer-simple.py`](infer-simple.py)** does inference sequentially on *Object Detection models
trained with Roboflow Train*; meaning it waits for the predictions from the previous frame before sending another. The framerate depends on the latency between your machine and the Inference API.

In our tests, we saw ~4 fps with the Roboflow
[Hosted API](https://docs.roboflow.com/inference/hosted-api)
and ~8 fps with an NVIDIA Jetson Xavier NX running the
[on-prem Roboflow Infer API](https://docs.roboflow.com/inference/nvidia-jetson).

**[`infer-async.py`](infer-async.py)** does inference in parallel for *Object Detection models
trained with Roboflow Train* using a frame buffer which you can configure in your `roboflow_config.json`. You should be able to achieve arbitrary framerates by adjusting the buffer size.

### [Classification](https://docs.roboflow.com/inference-classification/hosted-api)
**[`infer-classification.py`](infer-classification.py)** does inference sequentially
on *Classification models trained with Roboflow Train*; meaning it waits for the predictions from the previous frame before sending another. The framerate depends on the latency between your machine and the Inference API.