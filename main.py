import asyncio
import io
import glob
import json
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
# To install this module, run:
# python -m pip install Pillow
from PIL import Image, ImageDraw, ImageFont
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, FaceAttributeType

# This key will serve all examples in this document.

KEY = "b06e373b24034716a22c1038926bced0"
# This endpoint will be used in all examples in this quickstart.
ENDPOINT = "https://apifaceemotion.cognitiveservices.azure.com/"
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))





# Detect a face in an image that contains a single face
single_face_image_url = 'https://cdn.searchenginejournal.com/wp-content/uploads/2019/07/google-to-capture-and-learn-about-our-emotions-on-a-smartphone-camera.png'
single_image_name = os.path.basename(single_face_image_url)
# We use detection model 3 to get better performance.
detected_faces = face_client.face.detect_with_url(url=single_face_image_url, detection_model='detection_01', return_face_attributes=[FaceAttributeType.emotion, FaceAttributeType.gender])

if not detected_faces:
    raise Exception('No face detected from image {}'.format(single_image_name))

# Convert width height to a point in a rectangle
def getRectangle(faceDictionary):
    rect = faceDictionary.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height

    return ((left, top), (right, bottom))

def drawFaceRectangles():
    # Download the image from the url
    response = requests.get(single_face_image_url)

    img = Image.open(BytesIO(response.content))


    # For each face returned use the face rectangle and draw a red box.
    print('Drawing rectangle around face... see popup for results.')
    draw = ImageDraw.Draw(img)
    for face in detected_faces:
        dimentions = getRectangle(face)
        y = dimentions[0][1]
        draw.rectangle(dimentions, outline='white')

        emotionJson = json.loads(json.dumps(face.face_attributes.emotion.__dict__))

        del emotionJson['additional_properties']
        font = ImageFont.truetype("resources/Roboto-Bold.ttf", 12)
        draw.text((dimentions[0][0], y), face.face_attributes.gender.upper(), align="left", font=font, fill="red")
        y += 12
        for emotion in emotionJson:
            if(emotionJson[emotion] != 0.0):
                draw.text((dimentions[0][0], y), emotion, align="left", font=font, fill="yellow")
                y += 12



    img.save("C:\\Users\\andre\\Desktop\\maeFeliz2.jpg")
    # Display the image in the default image browser.
    img.show()

# Uncomment this to show the face rectangles.
drawFaceRectangles()



