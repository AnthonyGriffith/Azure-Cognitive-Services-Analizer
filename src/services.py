from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face import FaceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


def getFaceClient():
    # Access key for azure cognitive services and endpoint to get access to acs.
    key = "b06e373b24034716a22c1038926bced0"
    endpoint = "https://apifaceemotion.cognitiveservices.azure.com/"
    # Authentication with FaceClient.
    face_client = FaceClient(endpoint, CognitiveServicesCredentials(key))
    return face_client


def getTextAnalyticsClient():
    # Credentials for the Azure Language API
    credential = AzureKeyCredential("ef2f87788e5647a19b14cae72ad4f899")
    endpoint = "https://textsentimental.cognitiveservices.azure.com/"
    text_analytics_client = TextAnalyticsClient(endpoint, credential)
    return text_analytics_client
