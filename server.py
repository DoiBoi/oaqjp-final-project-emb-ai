"""Executing this module will render the page and start the emotion detection 
application to be executed over the Flask channel and deployed onlocalhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """Recieves the text to analyze from the HTML interface and calls the emotion 
detector method then formats and returns the result"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid input! Try again. "
    score = response[dominant_emotion]
    output = "For the given statement, the system response is:<br>"
    for key, value in response.items():
        output += "<br>" + key.capitalize() + ": " + str(value)
    output += f"<br><br>The dominant emotion is {dominant_emotion} with a score of {score}.<br>"
    return output

@app.route("/")
def render_index_page():
    """Renders index.html"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
