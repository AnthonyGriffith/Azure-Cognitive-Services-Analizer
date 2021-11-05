from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import os

# Credentials for the Azure Language API
credential = AzureKeyCredential("ef2f87788e5647a19b14cae72ad4f899")
endpoint="https://textsentimental.cognitiveservices.azure.com/"
text_analytics_client = TextAnalyticsClient(endpoint, credential)

# Global variables
TEXTS_PATH = "./media/texts/"

# Funtion to get all the texts from a folder
def analyze_folder(path):
    documents = []
    files = os.listdir(path)
    for f in files:
        text_file = open(path + f, "r", encoding="utf8")
        analized_text = text_file.read()
        text_file.close()
        documents.append(analized_text)
    return documents

def show_results(result):
    for doc in result:
        print("Overall sentiment: {}".format(doc.sentiment))
        print("Scores: positive={}; neutral={}; negative={} \n".format(
            doc.confidence_scores.positive,
            doc.confidence_scores.neutral,
            doc.confidence_scores.negative,
        ))

if __name__ == "__main__":
    # Opening multiple files
    documents = analyze_folder(TEXTS_PATH)

    # Api call for the text analysis
    response = text_analytics_client.analyze_sentiment(documents, language="en")
    result = [doc for doc in response if not doc.is_error]

    # Showing results
    show_results(result)



