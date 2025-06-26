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

    return response.text