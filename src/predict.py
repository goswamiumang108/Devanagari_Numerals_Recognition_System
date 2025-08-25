import cv2
import numpy as np


def Load_and_Preprocess_Image(image_path):
	"""Load and preprocess the image for prediction."""
	image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
	image = cv2.resize(image, (28, 28))
	image = image.astype('float32') / 255.0
	image = image.reshape(-1, 28, 28, 1)  # Reshape for the model
	
	return image


def Predict_Character(model, image_path):
	"""Predict the character in the given image."""
	image = Load_and_Preprocess_Image(image_path)
	
	prediction = model.predict(image)
	predicted_label = np.argmax(prediction)
	
	return predicted_label
