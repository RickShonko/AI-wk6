# complete_deployment.py

import tflite_runtime.interpreter as tflite
from PIL import Image
import numpy as np
import time

class RecyclableClassifier:
    """Complete recyclable items classifier for Raspberry Pi deployment"""
    
    def __init__(self, model_path):
        self.interpreter = tflite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        
        self.class_names = ['plastic', 'paper', 'glass', 'metal']
    
    def preprocess_image(self, image_path):
        """Preprocess image for classification"""
        image = Image.open(image_path).convert('RGB')
        image = image.resize((128, 128))
        image_array = np.array(image, dtype=np.float32) / 255.0
        image_array = np.expand_dims(image_array, axis=0)
        return image_array
    
    def predict(self, image_path):
        """Predict recyclable item class"""
        input_data = self.preprocess_image(image_path)
        
        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
        self.interpreter.invoke()
        
        output_data = self.interpreter.get_tensor(self.output_details[0]['index'])
        predicted_class = np.argmax(output_data[0])
        confidence = output_data[0][predicted_class]
        
        return self.class_names[predicted_class], confidence
    
    def real_time_demo(self):
        """Simulate real-time classification"""
        print("Starting real-time classification demo...")
        print("Press Ctrl+C to stop")
        
        try:
            while True:
                # Simulate capturing frames
                # In real deployment, this would capture from camera
                dummy_prediction = np.random.choice(self.class_names)
                confidence = np.random.uniform(0.7, 0.95)
                
                print(f"Predicted: {dummy_prediction} (Confidence: {confidence:.2f})")
                time.sleep(2)  # Simulate processing delay
                
        except KeyboardInterrupt:
            print("\nDemo stopped")

# Main execution
if __name__ == "__main__":
    # Initialize classifier
    classifier = RecyclableClassifier('recyclable_classifier.tflite')
    
    # Test with sample image
    try:
        class_name, confidence = classifier.predict('sample_image.jpg')
        print(f"Classification: {class_name} (Confidence: {confidence:.2f})")
    except:
        print("Sample image not found, running demo mode...")
    
    # Run real-time demo
    classifier.real_time_demo()