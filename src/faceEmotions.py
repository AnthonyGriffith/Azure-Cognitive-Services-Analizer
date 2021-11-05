import io
import json
import os

from PIL import Image, ImageDraw, ImageFont
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import FaceAttributeType

# Access key for azure cognitive services and endpoint to get access to acs.
KEY = "b06e373b24034716a22c1038926bced0"
ENDPOINT = "https://apifaceemotion.cognitiveservices.azure.com/"
# Authentication with FaceClient.
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))


# Convert width height to a point in a rectangle
def getRectangle(face_dictionary):
    rect = face_dictionary.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height

    return (left, top), (right, bottom)


def drawFaceRectangles(img, detected_faces, image_num):
    # For each face returned use the face rectangle and draw a red box.
    print('Drawing rectangle around face... see popup for results.')
    draw = ImageDraw.Draw(img)
    for face in detected_faces:
        dimensions = getRectangle(face)
        y = dimensions[0][1]
        draw.rectangle(dimensions, outline='white')
        emotion_json = json.loads(json.dumps(face.face_attributes.emotion.__dict__))
        del emotion_json['additional_properties']
        font = ImageFont.truetype("resources/Roboto-Bold.ttf", 12)
        draw.text((dimensions[0][0], y), face.face_attributes.gender.upper(), align="left", font=font, fill="red")
        y += 12
        for emotion in emotion_json:
            if emotion_json[emotion] != 0.0:
                draw.text((dimensions[0][0], y), emotion, align="left", font=font, fill="yellow")
                y += 12
    # Save the img in a folder.
    img.save("results\\emotionsResults\\resultado"+str(image_num)+".png")
    # Display the image in the default image browser.
    img.show()


def startAnalyzeEmotions():
    # Path from image to analyze.
    images_path = "./media/images"
    files = os.listdir(images_path)
    image_num = 0
    for f in files:
        img = Image.open('{0}/{1}'.format(images_path, f))

        # Output let us to detect an image from a folder.
        output = io.BytesIO()
        img.save(output, format='JPEG')  # or another format
        output.seek(0)

        # Analyze the image with azure.
        detected_faces = face_client.face.detect_with_stream(image=output, detection_model='detection_01',
                                                             return_face_attributes=[FaceAttributeType.emotion,
                                                                                     FaceAttributeType.gender])
        if not detected_faces:
            raise Exception('No face detected from image {}'.format(img))
        image_num += 1
        drawFaceRectangles(img, detected_faces, image_num)


startAnalyzeEmotions()
# Uncomment this to show the face rectangles.
# drawFaceRectangles()
