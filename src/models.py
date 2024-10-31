from data_processing import processing
import os
from data_processing import api
from sklearn.feature_extraction.text import TfidfVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import Counter
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor, as_completed

class YouTubeCommentAnalyzer:

    def __init__(self, video_id):

        self.max_workers = os.cpu_count()
        self.data_cleanner = processing.DataCleaning(video_id)
        self.analyser = SentimentIntensityAnalyzer()
        self.comments = self.data_cleanner.sentence_tokenize() 
        self.sentiment_data = self.analyze_sentiment()
        self.video_detalis = self.data_cleanner.otherapidata
        

    def vectorize_data(self, max_features=5000):

        self.vectorizer = TfidfVectorizer(max_features=max_features)
        tfidf_matrix = self.vectorizer.fit_transform(self.comments)
        
        return tfidf_matrix
    
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
            print(self.max_workers)
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
        print(sentiment_count)
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
        data['Engagement'] = round((int(data['likes']) * 0.499 + int(data['views']) * 0.002 + int(data['comment_count']) * 0.499) / 3, 1) #vievs are not as important as likes or comments 

        return data
    
     
    