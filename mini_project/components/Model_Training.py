#Model_Training.py
import os
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def model_trainer(X_train, X_test, y_train, y_test):
    if not os.path.exists("artifacts"):
        os.makedirs("artifacts")

    model = LogisticRegression(max_iter=200, solver='liblinear')
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    with open("artifacts/model.pkl", "wb") as f:
        pickle.dump(model, f)

    return accuracy
