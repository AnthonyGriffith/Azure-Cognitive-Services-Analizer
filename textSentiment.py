from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import os

credential = AzureKeyCredential("ef2f87788e5647a19b14cae72ad4f899")
endpoint = "https://textsentimental.cognitiveservices.azure.com/"
text_analytics_client = TextAnalyticsClient(endpoint, credential)
documents = []


def analyzeFile(file):
    global documents
    text_file = open("./media/texts/" + file, "r", encoding="utf8")
    parsed_text = text_file.read()
    text_file.close()
    documents.append(parsed_text)


# Opening multiple files
files = os.listdir("./media/texts")
for f in files:
    analyzeFile(f)

response = text_analytics_client.analyze_sentiment(documents, language="en")
result = [doc for doc in response if not doc.is_error]

for doc in result:
    print("Overall sentiment: {}".format(doc.sentiment))
    print("Scores: positive={}; neutral={}; negative={} \n".format(
        doc.confidence_scores.positive,
        doc.confidence_scores.neutral,
        doc.confidence_scores.negative,
    ))
