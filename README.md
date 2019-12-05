# AnyAI - Automatic product/customer detection for anyone.
AnyAI allows anyone to visually track objects which vary from time to time, with just a few images of each (e.g., daily meal offerings). AnyAI builds on recent advancements in transfer learning and few-shot learning.

In a concrete usecase, together with a userbase of profile pictures, AnyAI can visually detect the current product that a customer is buying in for example a university restaurant and identify the customer at the same time. This way, the customer is charged automatically for the right product and checking out only takes 2 seconds, instead of the usual 10 or 20 seconds. A web interface connects to two cameras (product & customer), and provides an intuitive UI through which a customer can perform self-checkout (see video [here](https://www.youtube.com/watch?v=8olhjUy0d8k)).

[More information on Devpost](https://devpost.com/software/anyai)

## Requirements
- TensorFlow 1.15.0

## Running
```
python app.py
npm start
```

## Debug
- Camera not working: open desktop app (e.g., FaceTime on macos) to activate camera.
