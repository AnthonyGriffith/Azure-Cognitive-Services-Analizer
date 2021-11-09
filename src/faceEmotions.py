import datetime
import io
import json
import os
import threading

from PIL import Image, ImageDraw, ImageFont
from azure.cognitiveservices.vision.face.models import FaceAttributeType
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face import FaceClient

key = "b06e373b24034716a22c1038926bced0"
endpoint = "https://apifaceemotion.cognitiveservices.azure.com/"
# Authentication with FaceClient.
face_client = FaceClient(endpoint, CognitiveServicesCredentials(key))
IMAGES_PATH = "../media/images"


# Convert width height to a point in a rectangle
def getRectangle(face_dictionary):
    rect = face_dictionary.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height

    return (left, top), (right, bottom)


def drawFaceRectangles(img, detected_faces, name):
    # For each face returned use the face rectangle and draw a red box.
    print('Drawing rectangle around face... see popup for results.')
    draw = ImageDraw.Draw(img)
    for face in detected_faces:
        dimensions = getRectangle(face)
        y = dimensions[0][1]
        draw.rectangle(dimensions, outline='white')
        emotion_json = json.loads(json.dumps(face.face_attributes.emotion.__dict__))
        del emotion_json['additional_properties']
        font = ImageFont.truetype("../resources/Roboto-Bold.ttf", 12)
        draw.text((dimensions[0][0], y), face.face_attributes.gender.upper(), align="left", font=font, fill="red")
        y += 12
        for emotion in emotion_json:
            if emotion_json[emotion] != 0.0:
                draw.text((dimensions[0][0], y), emotion, align="left", font=font, fill="yellow")
                y += 12
    # Save the img in a folder.
    name_split = name.split(".")
    img.save("../results\\emotionsResults\\resultado_" + name_split[0] + ".png")
    # Display the image in the default image browser.
    img.show()


def startAnalyzeEmotions(files):
    # Path from image to analyze.

    for f in files:
        img = Image.open('{0}/{1}'.format(IMAGES_PATH, f))

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

        # Uncomment this to show the face rectangles.
        drawFaceRectangles(img, detected_faces, f)


if __name__ == "__main__":

    start_time = datetime.datetime.now()
    files = os.listdir(IMAGES_PATH)
    print(len(files))
    if len(files) >= 4:
        lista1 = []
        lista2 = []
        for i in range(len(files)):
            if i % 2 == 0:
                lista1.append(files[i])
            else:
                lista2.append(files[i])
        thread1 = threading.Thread(target=startAnalyzeEmotions, args=(lista1,))
        thread2 = threading.Thread(target=startAnalyzeEmotions, args=(lista2,))
        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()
    # Api call for the text analysis
    else:
        startAnalyzeEmotions(files)
    end_time = datetime.datetime.now()
    print('Duration: {}'.format(end_time - start_time))
