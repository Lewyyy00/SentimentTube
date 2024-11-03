from src.models import *
from src.data_collector import *
from flask import Flask, render_template, request 
from collections import OrderedDict
from data_processing.api import *
import time

app = Flask(__name__, 
            static_folder=os.path.join('src', 'static'),  
            template_folder=os.path.join('src', 'templates')
            )

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def collected_list():

    query = request.form.get('query', '')
    max_results = int(request.form.get('max_results', 10))
    videos = YouTubeAPIClient.get_youtube_search_result(query, max_results=max_results)
    disc_results = {}

    for i in videos:
        start_time = time.time()

        result = YouTubeCommentAnalyzer(i).data_connector()
        key = f"https://www.youtube.com/watch?v={i}"
        disc_results[key] = result

        end_time = time.time() 
        iteration_time = end_time - start_time
        print(f"{i}: {iteration_time:.4f}s")

    print(disc_results)

    sorted_disc_results = OrderedDict(sorted(disc_results.items(), key=lambda x: x[1]['Engagement'], reverse=True))
    return render_template('index.html', disc_results=sorted_disc_results)

if __name__ == '__main__':
    app.run(debug=True)
