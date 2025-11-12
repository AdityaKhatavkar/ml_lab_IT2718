# Training_Pipeline.py 
import nltk, os
nltk.data.path.append(os.path.expanduser('~/nltk_data'))

print("Ithe tari aalo aahe me ")
import pandas as pd
from mini_project.components.Data_Transformation import data_preprocessing, text_vectorization
from mini_project.components.Model_Training import model_trainer
from sklearn.model_selection import train_test_split

Dataset_file_path = "/home/aditya/ml_lab_IT2718/mini_project/dataset_for_project/IMDB Dataset.csv"

# Step 1: Preprocess text 
print("Ataa Prepross honar")
X, y = data_preprocessing(Dataset_file_path)
print("/n Data_preprocessing completed")

# Step 2: Split before vectorization
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("/n Train-Test Split Done")

# Step 3: Vectorize (fit only on training data)
X_train_tv, X_test_tv = text_vectorization(X_train, X_test)
print("/n Text Vectorizatioin Done")

# Step 4: Train and evaluate
accuracy = model_trainer(X_train_tv, X_test_tv, y_train, y_test)
print(f"Model training completed with accuracy: {accuracy:.3f}")
