import os
from src.data_loader import Load_Data, Preprocess_Data
from src.model import Create_Model
from src.train import Train_Model
from src.evaluate import Evaluate_Model
from src.predict import Predict_Character
from sklearn.model_selection import train_test_split
from tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk()
data_dir = os.path.abspath(r".\dataset")  # Path to the dataset folder


def prepare_DNRS_model():
	# Load and preprocess the data
	X, y = Load_Data(data_dir)
	X, y = Preprocess_Data(X, y)
	# Split the dataset into training and testing sets
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
	
	# Create the model
	model = Create_Model(y.shape[1])
	# Train the model
	Train_Model(model, X_train, y_train, X_test, y_test)
	# Evaluate the model
	Evaluate_Model(model, X_test, y_test)
	
	return model


def make_label_predictions(model):
	Tk.lift(root)
	img_path = str(askopenfilename(defaultextension=".img", initialdir=".",
			title="Select an image to make label-predictions"))
	
	return Predict_Character(model=model, image_path=img_path)


def main():
	print("Welcome to Devanagari Numerals Recognition System")
	print("Developed by Umang Goswami")
	print("-" * 21)
	print("This is the presentation of how the system shall work")
	print("-" * 21)
	print("\nFirst the DNRS_model shall be developed and saved")
	DNRS_model = prepare_DNRS_model()
	print("\nCongratulations the DNRS_model is successfully developed and saved !!")
	print("\nNow we shall make label-predictions")
	predicted_label = make_label_predictions(DNRS_model)
	print(f'\nPredicted label: {predicted_label}')
	

if __name__ == '__main__':
	main()