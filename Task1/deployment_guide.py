# deployment_guide.py

def deployment_steps():
    """Step-by-step deployment guide for Raspberry Pi"""
    
    steps = [
        {
            "step": 1,
            "title": "Hardware Setup",
            "description": "Set up Raspberry Pi 4 with Raspberry Pi OS",
            "commands": [
                "sudo apt update",
                "sudo apt upgrade -y",
                "sudo apt install python3-pip -y"
            ]
        },
        {
            "step": 2,
            "title": "Install Dependencies",
            "description": "Install TensorFlow Lite Runtime",
            "commands": [
                "pip3 install tflite-runtime",
                "pip3 install pillow numpy"
            ]
        },
        {
            "step": 3,
            "title": "Transfer Model",
            "description": "Copy TFLite model to Raspberry Pi",
            "commands": [
                "scp recyclable_classifier.tflite pi@raspberrypi.local:/home/pi/"
            ]
        },
        {
            "step": 4,
            "title": "Camera Setup",
            "description": "Configure Raspberry Pi camera module",
            "commands": [
                "sudo raspi-config",
                "# Enable Camera interface"
            ]
        },
        {
            "step": 5,
            "title": "Run Inference",
            "description": "Execute real-time classification",
            "code": """
import tflite_runtime.interpreter as tflite
from PIL import Image
import numpy as np

# Load model
interpreter = tflite.Interpreter(model_path='recyclable_classifier.tflite')
interpreter.allocate_tensors()

# Run inference on camera feed
def classify_frame(frame):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    # Preprocess frame
    input_data = preprocess_frame(frame)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    
    return interpreter.get_tensor(output_details[0]['index'])
            """
        }
    ]
    
    return steps

# Print deployment guide
steps = deployment_steps()
for step in steps:
    print(f"\nStep {step['step']}: {step['title']}")
    print(f"Description: {step['description']}")
    if 'commands' in step:
        print("Commands:")
        for cmd in step['commands']:
            print(f"  {cmd}")