import requests
import json


def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyse } }
    res = requests.post(url, json = obj, headers = header)

    if res.status_code == 200:
        formatted = json.loads(res.text)

        anger = formatted['emotionPredictions'][0]['emotion']['anger']
        disgust = formatted['emotionPredictions'][0]['emotion']['disgust']
        fear = formatted['emotionPredictions'][0]['emotion']['fear']
        joy = formatted['emotionPredictions'][0]['emotion']['joy']
        sadness = formatted['emotionPredictions'][0]['emotion']['sadness']

        emotions = {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness}

        max_emotion = max(emotions, key=emotions.get)

        emotions['dominant_emotion'] = max_emotion
    
    elif res.status_code == 400:
        emotions = {
            'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
            }


    return emotions