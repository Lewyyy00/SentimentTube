from src import models
import csv
import os

class DataCollector:

    def __init__(self, csv_filename='youtube_data.csv'):
       
        self.csv_filename = csv_filename

        if not os.path.isfile(self.csv_filename):
            with open(self.csv_filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['original_comment', 'likes', 'views', 'number of comments', 'positive comments', 'neutral comments', 'negative comments'])

    def transform_data_to_row():

        pass

    def add_record(self, original_comment, cleaned_comment, sentiment):
        
        with open(self.csv_filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([])