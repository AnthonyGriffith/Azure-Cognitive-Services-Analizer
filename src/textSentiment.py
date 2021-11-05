import os
from src.services import getTextAnalyticsClient
# Global variables


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


if __name__ == "__main__":
    # Opening multiple files
    documents = analyze_folder(TEXTS_PATH)

    # Api call for the text analysis
    response = getTextAnalyticsClient().analyze_sentiment(documents, language="en")
    result = [doc for doc in response if not doc.is_error]

    # Showing results
    show_results(result)
