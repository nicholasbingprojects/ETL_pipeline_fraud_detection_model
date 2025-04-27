import pandas as pd
from src.model.train import train_model
from sklearn.model_selection import train_test_split

def test_model():
    data = pd.DataFrame({
        'feature': [1, 2, 3, 4, 5],
        'target': [2, 3, 5, 7, 11]
    })
    
    X = data[['feature']]
    y = data['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = train_model(X_train, y_train)
    assert model is not None