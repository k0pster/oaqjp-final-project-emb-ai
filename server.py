""" server.py - Running Emotional Detection App using Flask """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    """ sent_analyzer - return dominant emotion in provided text"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        msg = "Invalid text! Please try again!"
    else:
        msg = f"For the given statement, the system response is 'anger': {anger}, "\
        f"'disgust': {disgust},'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "\
        f"The dominant emotion is {dominant_emotion}."
    return msg

@app.route("/")
def render_index_page():
    """ render_index_page - redendering index.html on WEB"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
