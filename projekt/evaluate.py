import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    
    y_pred = np.argmax(y_pred, axis=1)
    
    print(classification_report(y_test, y_pred))
    cm = confusion_matrix(y_test, y_pred)
    print(cm)