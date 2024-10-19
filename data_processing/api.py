import os
from googleapiclient.discovery import build 
from dotenv import load_dotenv
import isodate

load_dotenv()

API_KEY = os.getenv("API_KEY")
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_video_comments(video_id, max_results=100):

    comments = []
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=max_results,
        textFormat='plainText'
    )
    
    while request:
        response = request.execute()
    
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
            
        request = youtube.commentThreads().list_next(request, response)

    return comments

def get_video_details(video_id):

    request = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        id=video_id
    )
    response = request.execute()

    if response['items']:
        video_info = response['items'][0]
        print(video_id)
        title = video_info['snippet']['title']
        duration = isodate.parse_duration(video_info['contentDetails'].get('duration', 0))
        
        likes = video_info['statistics'].get('likeCount', 0)
        dislikes = video_info['statistics'].get('dislikeCount', 0)
        views = video_info['statistics'].get('viewCount', 0)
        comment_count = video_info['statistics'].get('commentCount', 0)

        results = {
            'title': title,
            'likes': likes,
            'duration': duration,
            #'dislikes': dislikes,
            'views': views,
            'comment_count': comment_count
        }
        
        return results
    else:
        return None
    

def get_playlist_videos(playlist_id):
    request = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=500
    )
    
    response = request.execute()
    print(response)
    
    video_urls = []
    for item in response['items']:
        video_id = item['snippet']['resourceId']['videoId']
        video_urls.append(f'https://www.youtube.com/watch?v={video_id}')
    
    return video_urls


    