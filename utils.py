import numpy as np
from PIL import Image
import tensorflow as tf


def preprocess_image(image_file):
    img = Image.open(image_file).convert("L")
    img = img.resize((28, 28))

    img_array = np.array(img)

    # Invert if background is white
    if np.mean(img_array) > 127:
        img_array = 255 - img_array

    img_array = img_array.astype("float32") / 255.0
    img_array = img_array.reshape(1, 784)

    return img_array


def load_model(model_path="model/mnist_pipeline.keras"):
    return tf.keras.models.load_model(model_path)


def predict_digit(model, image_file):
    processed = preprocess_image(image_file)
    predictions = model.predict(processed, verbose=0)

    digit = np.argmax(predictions[0])
    confidence = np.max(predictions[0])

    return digit, confidence
