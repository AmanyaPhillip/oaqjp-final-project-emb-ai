import requests
import json

def emotion_detection(text_to_analyze):
    #Define the URL for the emotion detector API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    #Create the payload with the text to be to be analysed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    #set the headers with the required model ID for the API
    myobj = { "raw_document": { "text": text_to_analyze } }

    #Make the Post request to the API with the payload and header
    response = requests.post(url, json = myobj , headers = header)

    #parse the response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    # If the response status code is 400, set label and score to None
    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        emotion = None

    data = {
        "anger": anger,
        "disgust":disgust,
        "fear":fear,
        "joy":joy,
        "sadness":sadness
    }
    
    if data['anger'] is None :
        data['dominant_emotion'] = None
    else:
        largest_value = 0
        for name, value in data.items():
            if value > largest_value:
                largest_value = value
                largest_variable_name = name
        data['dominant_emotion'] = largest_variable_name
    return data