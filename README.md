# SentimentTube
Have you ever felt like you were wasting a lot of time scrolling through YouTube results, not knowing which video is the most valuable? If the answer is yes, then you should check out this project!

SentimentTube is a Flask-based application designed to help users evaluate the quality and value of YouTube videos by analyzing sentiment from comments. Using Natural Language Processing (NLP) and sentiment analysis, the application processes comments, categorizes them as positive, neutral, or negative, and generates metrics that help determine the overall engagement and sentiment around a video.

## Table of Contents
1. [Project structure](#project-structure)
2. [Installation](#installation)
3. [Usage](#Usage)

## Project structure
```
SentimentTube/
├── data_processing/
│   ├── __init__.py     
│   ├── api.py             # Api processing
│   └── processing.py      # Contains data processing logic
├── src/ 
│   ├── static/     
│   │   └── styles.css     # CSS template for the main page   
│   ├── templates/
│   │   └── index.html     # HTML template for the main page              
│   ├── __init__.py     
│   ├── data_collector.py  # Save video's data into CSV (in progress)
│   └── models.py          # A set of methods used to perform sentiment analysis
├── .env                   # Api key storage location
├── README.md              # Project documentation 
├── requirements.txt       # Python dependencies
├── app.py                 # Main application file (Flask app)
└── .gitignore             # Git ignore file
```

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

## Usage
