import os
from googleapiclient.discovery import build 
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_comments(video_id, max_results=50):

    if API_KEY:
        pass
    else:
        print('does not work')
        
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=max_results,
        textFormat='plainText'
    )
    
    response = request.execute()
    
    comments = []
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)
    
    return comments

video_id = 'tTIYVQ0U_as'
comments = get_comments(video_id)
print(comments)