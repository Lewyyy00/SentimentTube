import api
import re 
import emoji
from urllib.parse import urlparse
from nltk.corpus import stopwords

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
    

x = DataCleaning('').clean_data()
