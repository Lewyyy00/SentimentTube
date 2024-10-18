from src.models import *
from src.data_collector import *

x = YouTubeCommentAnalyzer('https://www.youtube.com/watch?v=5eqRuVp65eY').data_connector()

csv_writer = DataCollector('youtube_data.csv')
csv_writer.write_to_csv(x)