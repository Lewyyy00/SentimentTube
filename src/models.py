from data_processing import processing
from data_processing import api
from sklearn.feature_extraction.text import TfidfVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import Counter
import matplotlib.pyplot as plt

class YouTubeCommentAnalyzer:

    def __init__(self, website):
       
        self.comments = processing.DataCleaning(website).sentence_tokenize() 
        self.labels = ['positive', 'neutral', 'negative']
        self.sentiment_data = self.analyze_sentiment()
        self.video_detalis = api.get_video_details()

    def vectorize_data(self, max_features=5000):

        self.vectorizer = TfidfVectorizer(max_features=max_features)
        tfidf_matrix = self.vectorizer.fit_transform(self.comments)
        
        return tfidf_matrix
    
    def analyze_sentiment(self):
      
        analyzer = SentimentIntensityAnalyzer()
        sentiment_labels = []

        for comment in self.comments:
            sentiment_scores = analyzer.polarity_scores(comment)
            if sentiment_scores['compound'] >= 0.05:
                sentiment_labels.append('positive')
            elif sentiment_scores['compound'] <= -0.05:
                sentiment_labels.append('negative')
            else:
                sentiment_labels.append('neutral')

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

    def data_connector(self):
        data = self.video_detalis()
        data["Result"] = self.sentiment_data

        return data