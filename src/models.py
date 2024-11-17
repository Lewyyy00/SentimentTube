from data_processing import processing
import os
from data_processing import api
from sklearn.feature_extraction.text import TfidfVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import Counter
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor, as_completed
import math

class YouTubeCommentAnalyzer:

    """
    This class contains a set of methods that are used to perform sentiment analysis. It also calculates engagement metrics based on video details 
    and sentiment data to assess the video's potential quality.
    
    """

    WEIGHT_LIKES_VIEWS = 0.1 
    WEIGHT_POSITIVE = 1.5  
    WEIGHT_NEGATIVE = 1.5 
    WEIGHT_LOG_VIEWS = 0.002 #vievs are not as important as likes or comments 

    def __init__(self, video_id):

        self.max_workers = os.cpu_count()
        self.data_cleanner = processing.DataCleaning(video_id)
        self.analyser = SentimentIntensityAnalyzer()
        self.comments = self.data_cleanner.sentence_tokenize() 
        self.sentiment_data = self.analyze_sentiment()
        self.video_detalis = self.data_cleanner.otherapidata
        

    def vectorize_data(self, max_features=5000):

        vectorizer = TfidfVectorizer(max_features=max_features)        
        return vectorizer.fit_transform(self.comments)
    
    def analyze_sentiment(self):
        
        sentiment_labels = []

        def analyze_comment(comment):
            sentiment_scores = self.analyser.polarity_scores(comment)
            if sentiment_scores['compound'] >= 0.05:
                sentiment_labels.append('positive')
            elif sentiment_scores['compound'] <= -0.05:
                sentiment_labels.append('negative')
            else:
                sentiment_labels.append('neutral')

        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = {executor.submit(analyze_comment, comment): comment for comment in self.comments}

            for future in as_completed(futures):
                try:
                    result = future.result()  
                    sentiment_labels.append(result)
                except Exception as exc:
                    print(f'Comment generated an exception: {exc}')

        return Counter(sentiment_labels)
    

    def bar_chart_maker(self):

        sentiment_count = self.sentiment_data
        sentiments = list(sentiment_count.keys())
        counts = list(sentiment_count.values())

        plt.figure(figsize=(8, 6))
        plt.bar(sentiments, counts, color=['red', 'green', 'gray'])
        plt.title('Sentiment Distribution')
        plt.xlabel('Sentiment')
        plt.ylabel('Amount of comments')
        plt.show()
        plt.close()

    def data_connector(self):

        data = self.video_detalis
        data["Result"] = self.sentiment_data

        comment_count = int(data['comment_count']) if int(data['comment_count']) > 0 else 1
        views = int(data['views']) if int(data['views']) > 0 else 1
        likes = int(data['likes']) if int(data['likes']) > 0 else 1

        data['Engagement'] = round(((likes / views) * self.WEIGHT_LIKES_VIEWS + 
                                    (int(data['Result'].get('positive', 0)) / comment_count) * self.WEIGHT_POSITIVE + 
                                    (int(data['Result'].get('negative', 0)) / comment_count)) * self.WEIGHT_NEGATIVE + 
                                    math.log(views) * self.WEIGHT_LOG_VIEWS, 5) 

        return data
    
     
    