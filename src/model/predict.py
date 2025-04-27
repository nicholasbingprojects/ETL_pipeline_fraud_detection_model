import pickle

def predict(input_data):
    """Make predictions using the trained model."""
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    return model.predict(input_data)