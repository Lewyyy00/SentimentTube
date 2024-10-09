import api
import re 
import emoji
from urllib.parse import urlparse
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('punkt')

class DataCleaning:

    def __init__(self, website):
        self.website = website
        video_id = self.get_video_id()
        self.data = api.get_video_comments(video_id)


    def get_video_id(self):
        parsed_url = urlparse(self.website)

        data = parsed_url.query
        data = data.replace('v=', '')        
        return data   

    def clean_data(self):
        clean_data =[]

        for comment in self.data:
            
            preprocesed_text = comment.lower()  
            preprocesed_text = re.sub(r'\b\w{1}\b', '', preprocesed_text)  
            preprocesed_text = re.sub(r'\s+', ' ', preprocesed_text)  
            preprocesed_text = re.sub(r'[^\w\s]', '', preprocesed_text) 
            clean_data.append(preprocesed_text)

        return clean_data

    def sentence_tokenize(self):
        data = self.clean_data()
        filtered_sentences = []

        for sentence in data:
            words = word_tokenize(sentence)
           
            filtered_sentence = ' '.join([word for word in words if word not in set(stopwords.words("english"))]) 
            filtered_sentences.append(filtered_sentence)

        for i in filtered_sentences:
            if len(i) == 0:
                filtered_sentences.remove(i)

        return filtered_sentences
    

x = DataCleaning('https://www.youtube.com/watch?v=5eqRuVp65eY').sentence_tokenize()
print(x)