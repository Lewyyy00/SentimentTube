# SentimentTube
Have you ever felt like you were wasting a lot of time scrolling through YouTube results, not knowing which video is the most valuable? If the answer is yes, then you should check out this project!

SentimentTube is a Flask-based application designed to help users evaluate the quality and value of YouTube videos by analyzing sentiment from comments. Using Natural Language Processing (NLP) and sentiment analysis, the application processes comments, categorizes them as positive, neutral, or negative, and generates metrics that help determine the overall engagement and sentiment around a video.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#Usage)

## Installation

1. Clone the repository from GitHub:

    ```bash
    git clone https://github.com/yourusername/SentimentTube.git
    cd SentimentTube
    ```

2. Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set Up API Keys:

* The application requires access to the YouTube Data API.
* Obtain an API key from Google Cloud Console.
* Make a .env file
* Store your API key in the .env file as shown below:

    ```bash
    API_KEY='your_youtube_api_key'
    ```

5. Start the Flask server:

    ```bash
    flask run
    ```

6. The application should now be running at `http://127.0.0.1:5000/`.