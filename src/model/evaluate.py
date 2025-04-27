from sklearn.metrics import classification_report

def evaluate_model(model, X_test, y_test):
    """Evaluate the model performance."""
    predictions = model.predict(X_test)
    report = classification_report(y_test, predictions)
    print(report)