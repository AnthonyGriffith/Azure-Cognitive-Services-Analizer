import datetime
import os
import threading
from pydoc import doc

from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Global variables
credential = AzureKeyCredential("ef2f87788e5647a19b14cae72ad4f899")
endpoint = "https://textsentimental.cognitiveservices.azure.com/"
text_analytics_client = TextAnalyticsClient(endpoint, credential)
TEXTS_PATH = "../media/texts/"


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


def startAnalyze(documents):
    response = text_analytics_client.analyze_sentiment(documents, language="en")
    for i in response:
        if i.is_error:
            print(i)
    result = [doc for doc in response if not doc.is_error]

    # Showing results
    show_results(result)


if __name__ == "__main__":
    # Opening multiple files
    start_time = datetime.datetime.now()
    documents = analyze_folder(TEXTS_PATH)
    print(len(documents))
    if len(documents) > 8:
        lista1 = []
        lista2 = []
        for i in range(len(documents)):
            if i % 2 == 0:
                lista1.append(documents[i])
            else:
                lista2.append(documents[i])
        thread1 = threading.Thread(target=startAnalyze, args=(lista1,))
        thread2 = threading.Thread(target=startAnalyze, args=(lista2,))
        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()
    # Api call for the text analysis
    else:
        startAnalyze(documents)
    end_time = datetime.datetime.now()
    print('Duration: {}'.format(end_time - start_time))
