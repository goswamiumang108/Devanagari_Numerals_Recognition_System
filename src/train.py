from tensorflow.keras.callbacks import EarlyStopping


def Train_Model(model, X_train, y_train, X_test, y_test, epochs=10, batch_size=32):
	"""Train the model on the training data."""
	
	# Early stopping to prevent overfitting
	early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
	
	# Train the model
	model.fit(X_train, y_train, validation_data=(X_test, y_test),
			epochs=epochs, batch_size=batch_size, callbacks=[early_stopping])
	
	# Save the model after training
	model.save('Devanagari_Numerals_Recognition_Model.keras')
