import numpy as np
from PIL import Image
import os, cv2


# Method to train custom classifier to recognize face
def train_classifer(data_dir):
    # Read all the images in custom data-set
    path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
    faces = []
    ids = []

    # Store images in a numpy format and ids of the user on the same index in imageNp and id lists
    for image in path:
        img = Image.open(image).convert('L')
        imageNp = np.array(img, 'uint8')
        id = int(os.path.split(image)[1].split(".")[1])
        faces.append(imageNp)
        ids.append(id)

    ids = np.array(ids)

    # Train and save classifier
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, ids)
    recognizer.write("classifier.yml")

# check existance  of .DS_Store file in data directory
exists = os.path.isfile('/Users/sahilgoyal/Desktop/face_recogination/data/.DS_Store')
if exists:
	os.system("sh test.sh")

train_classifer('data')
