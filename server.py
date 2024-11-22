"""
This is the server file for the Flask app to run
the userinterface index.html on port 5000, and creates a route
to run the emotion detector function.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def sent_detector():
    """
        Route '/emotionDetector'

        arguments: 
            textToAnalyze:
                A string to analyze with the emotion_detector function
        
        Extracts the response and if the Dominant Emotion is None,
         then return "Invalid text! Please try again!", else returns a string 
         outputting the emotion predictions with the Dominant Emotion.

    """
    text_to_analyze = request.args.get('textToAnalyze')

    res = emotion_detector(text_to_analyze)

    #extract res data
    anger = res['anger']
    disgust = res['disgust']
    fear = res['fear']
    joy = res['joy']
    sadness = res['sadness']
    dominant_emotion = res['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': {anger}, " \
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. " \
        f"The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    """
        This renders the html file Index for the user interface
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
