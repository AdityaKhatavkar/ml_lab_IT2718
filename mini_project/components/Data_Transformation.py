# Data_Transformation.py
import os
import pandas as pd
import numpy as np
import re
import string
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

import nltk, os



def text_preprocessing(text):

        #Remove html tags
        pattern = re.compile('<.*?>')
        text =  pattern.sub(r'', text)
    
        #Remove urls
        #text = re.sub(r'https?://\S+|www\.\S+', '', text)
        temp = re.compile(r'https?://\S+|www\.\S+')
        text =  temp.sub('', text)

        #Lowering the text
        text = text.lower()

        #Removing punctions
        '''
        exclude = string.punctuation
        text =  text.translate(str.maketrans('','',exclude))
        '''
        text =  text.translate(str.maketrans('','',string.punctuation))

        #Tokanizing text
        text = word_tokenize(text)

        #Removinng stopwords
        stopwords_to_remove = stopwords.words('english')
        text = [word for word in text if word not in stopwords_to_remove]
        '''
        for w in text.split():
            if w in stopwords_to_remove:
                text = ''.join(text.replace(w, ''))
        '''

        #Lemmatization
        lemmatizer = WordNetLemmatizer()
        text = ' '.join([lemmatizer.lemmatize(word) for word in text])


        if not os.path.exists('artifacts'): 
             os.makedirs('artifacts')
        with open('artifacts/preprocessing.pkl','wb')as f:
            pickle.dump((text_preprocessing),f)

        return text


def text_vectorization(X_train, X_test):
    tv = TfidfVectorizer(max_features=5000)
    X_train_tv = pd.DataFrame(tv.fit_transform(X_train).toarray())
    X_test_tv = pd.DataFrame(tv.transform(X_test).toarray())

    if not os.path.exists('artifacts'):
        os.makedirs('artifacts')

    with open('artifacts/vectorizer.pkl', 'wb') as f:
        pickle.dump(tv, f)

    return X_train_tv, X_test_tv



def data_preprocessing(Dataset_file_path):
    
    df = pd.read_csv(Dataset_file_path)
    '''
    df['review']=df['review'].apply(text_preprocessing)
    '''

    # Initialize an empty list to store processed chunks
    chunks = []
    # Process the dataframe in chunks of 10,000 rows
    chunk_size = 10000
    for start in range(0, len(df), chunk_size):
        end = start + chunk_size
        chunk = df.iloc[start:end].copy()  # Copy the chunk to avoid modifying the original dataframe
        chunk['review'] = chunk['review'].apply(text_preprocessing)
        chunks.append(chunk)

    # Concatenate the processed chunks back into a single dataframe
    df= pd.concat(chunks, ignore_index=True)
    # Now df contains the preprocessed reviews


    with open('artifacts/preprocessing.pkl','wb')as f:
            pickle.dump((text_preprocessing),f)

    
    X = df['review']
    y = df['sentiment']

    le = LabelEncoder()
    y = le.fit_transform(y)
    return X,y


    
 