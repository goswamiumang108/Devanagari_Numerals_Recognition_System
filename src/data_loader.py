import os
import cv2
import numpy as np


def Load_Data(data_dir):
	"""Load images and labels from the dataset directory."""
	images = []
	labels = []
	
	# Iterate through each subfolder in the dataset directory
	for label in os.listdir(data_dir):
		label_dir = os.path.join(data_dir, label)
		if os.path.isdir(label_dir):
			for image_file in os.listdir(label_dir):
				image_path = os.path.join(label_dir, image_file)
				image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
				
				image = cv2.resize(image, (28, 28))  # Resize to 28x28
				if image is not None:
					images.append(image)
					labels.append(int(label))  # Convert label to integer
	return np.array(images), np.array(labels)


def Preprocess_Data(X, y):
	"""Preprocess the images and labels."""
	# Resize images to 28x28 and normalize
	X_resized = np.array([cv2.resize(img, (28, 28)) for img in X])
	X_normalized = X_resized.astype('float32') / 255.0
	X_normalized = X_normalized.reshape(-1, 28, 28, 1)  # Reshape for CNN
	
	# One-hot encode the labels
	from tensorflow.keras.utils import to_categorical
	y_encoded = to_categorical(y)
	
	return X_normalized, y_encoded
