from data_loader import Load_Data, Preprocess_Data
import os


data_dir = os.path.abspath(r".\dataset")  # Update this path
X, y = Load_Data(data_dir)
X, y = Preprocess_Data(X, y)


def Evaluate_Model(model, X_test, y_test):
	"""Evaluate the model on the test data."""
	loss, accuracy = model.evaluate(X_test, y_test)
	print(f'\nTest Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}')
