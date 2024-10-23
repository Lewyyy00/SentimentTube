from src.models import *
from src.data_collector import *
from flask import Flask, render_template, request 


app = Flask(__name__, template_folder=os.path.join('src', 'templates'))

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route("/", methods=['POST'])
def collected_list():

    query = request.form.get('query', '')
    videos = api.get_youtube_search_result(query)
    disc_results = {}

    for i in videos:
        result = YouTubeCommentAnalyzer(i).data_connector()
        key = f"https://www.youtube.com/watch?v={i}"
        disc_results[key] = result['Result']


    return render_template('index.html', disc_results=disc_results)

if __name__ == '__main__':
    app.run(debug=True)