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
        
  