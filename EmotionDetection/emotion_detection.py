# import requests

# def emotion_detector(text_to_analyze):
#     url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
#     headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#     payload = {"raw_document": {"text": text_to_analyze}}
#     response = requests.post(url, json = payload, headers=headers)
#     return response.text


import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json = payload, headers=headers)
    formatted_response = json.loads(response.text)

    emotions = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        'dominant_emotion': None
    }

    if response.status_code != 400:
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        dominant_score = 0
        for key, value in emotions.items():
            if value > dominant_score:
                dominant_emotion = key
                dominant_score = value
        emotions["dominant_emotion"] = dominant_emotion

    return emotions