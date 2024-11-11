from data_processing.api import *
import re 
import emoji
from urllib.parse import urlparse
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

class DataCleaning:

    """
    The DataCleaning class is designed to process and clean YouTube video comment data, preparing it for further analysis. 
    Basically, the whole class is a sequence of cleaning methods and includes methods to standardize text by applying lowercasing, 
    removing punctuation, eliminating stop words, and lemmatizing terms for consistency. The method sentence_tokenize, which is 
    implemented below, is responsible for tokenizing comments.

    """

    def __init__(self, video_id):
        self.video_id = video_id
        youtube_client = YouTubeAPIClient(video_id)
        self.data = youtube_client.get_video_comments()
        self.otherapidata = youtube_client.get_video_details()
        self.lemmatizer = WordNetLemmatizer()

    def get_video_id(self):
        parsed_url = urlparse(self.website)

        data = parsed_url.query
        data = data.replace('v=', '')        
        return data   

    def clean_data(self):
        clean_data =[]

        for comment in self.data:
            
            preprocessed_text = comment.lower()  
            preprocessed_text = re.sub(r'\b\w{1}\b', '', preprocessed_text)  
            preprocessed_text = re.sub(r'\s+', ' ', preprocessed_text)  
            preprocessed_text = re.sub(r'[^\w\s]', '', preprocessed_text) 

            preprocessed_text = emoji.replace_emoji(preprocessed_text, replace='')
            preprocessed_text = re.sub(r'http\S+|www.\S+', '', preprocessed_text)
            
            clean_data.append(preprocessed_text)

        return clean_data

    def sentence_tokenize(self):
        data = self.clean_data()
        filtered_sentences = []

        for sentence in data:
            words = word_tokenize(sentence)

            filtered_sentence = ' '.join([
            self.lemmatizer.lemmatize(word) for word in words 
            if word not in set(stopwords.words("english"))
            ])

            if len(filtered_sentence) > 0:
                filtered_sentences.append(filtered_sentence)

        return filtered_sentences
    