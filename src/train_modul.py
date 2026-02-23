import face_recognition
import os
import pickle

dataset_path = "dataset"
encodings = []
names = []

for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)

    for image_name in os.listdir(person_path):
        image_path = os.path.join(person_path, image_name)

        image = face_recognition.load_image_file(image_path)
        face_enc = face_recognition.face_encodings(image)

        if face_enc:
            encodings.append(face_enc[0])
            names.append(person)

data = {"encodings": encodings, "names": names}

with open("encodings/encodings.pickle", "wb") as f:
    pickle.dump(data, f)

print("Training complete ✅")