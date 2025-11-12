# nltk_data_downloader.py
import nltk, os

nltk_data_dir = os.path.expanduser('~/nltk_data')
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.append(nltk_data_dir)

for res in ['stopwords', 'wordnet', 'omw-1.4', 'punkt']:
    try:
        if res in ['stopwords', 'wordnet', 'omw-1.4']:
            nltk.data.find(f'corpora/{res}')
        else:
            nltk.data.find(f'tokenizers/{res}')
    except LookupError:
        nltk.download(res)
