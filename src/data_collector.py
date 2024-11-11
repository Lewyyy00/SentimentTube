from src.models import *
import datetime
from collections import Counter
import csv
import os

class DataCollector:

    """
    The DataCollector was designed to save data into a CSV file. It was created because, in the beginning, I planned to implement more ML elements 
    into the project, and I might still do so in the future. Right now, there is no use for this class in the current project.
    
    """

    def __init__(self, csv_filename='youtube_data.csv'):
       
        self.csv_filename = csv_filename
    
    def write_to_csv(self, data):
        
        title = data.get('title')
        likes = data.get('likes')
        duration = str(data.get('duration'))  
        views = data.get('views')
        comment_count = data.get('comment_count')
        result = data.get('Result')

        positive = result.get('positive', 0)
        neutral = result.get('neutral', 0)
        negative = result.get('negative', 0)

        with open(self.csv_filename, mode='a+', newline='', encoding='utf-8') as file:

            writer = csv.writer(file)
            file.seek(0)
            if file.read(1) == "":
                writer.writerow(['Title', 'Likes', 'Duration', 'Views', 'Comment Count', 'Positive', 'Neutral', 'Negative'])
            
            writer.writerow([title, likes, duration, views, comment_count, positive, neutral, negative])

    def delate_csv(self):

        csv_path = 'ML-project\data\youtube_data.csv'

        if(os.path.exists(csv_path) and os.path.isfile(csv_path)):
            os.remove(csv_path) 
            print("file deleted") 
        else: 
            print("file not found") 




