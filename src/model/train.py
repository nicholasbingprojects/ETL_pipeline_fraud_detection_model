from sklearn.linear_model import LogisticRegression
import pickle

def train_model(X, y):
    """Train a logistic regression model for fraud detection."""
    model = LogisticRegression()
    model.fit(X, y)
    
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)

    return model