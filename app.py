from src.models import *
from src.data_collector import *


x = api.get_playlist_videos('PLF3psEbJ1sPYg8Zqw__Jv48Cr6w9xUqss')

for i in x:

    y = YouTubeCommentAnalyzer(f"{i}").data_connector()

    csv_writer = DataCollector('youtube_data.csv')
    csv_writer.write_to_csv(y)