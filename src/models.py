from data_processing import processing
from sklearn.feature_extraction.text import TfidfVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class YouTubeCommentAnalyzer:

    def __init__(self, website):
       
        self.comments = processing.DataCleaning(website).sentence_tokenize() 
        self.labels = ['positive', 'neutral', 'negative']

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

        return sentiment_labels
  
x = YouTubeCommentAnalyzer('https://www.youtube.com/watch?v=5eqRuVp65eY').analyze_sentiment()
print(x)