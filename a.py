import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2

# Load your trained model
model = tf.keras.models.load_model("C:\\Users\\Lenovo\\Downloads\\resnet50_model_multilabel.keras")

def preprocess_image(image_file):
    img = image.load_img(image_file, target_size=(224, 224))
    img = image.img_to_array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # Convert to HSV
    img = np.expand_dims(img, axis=0)
    img = img / 255.0
    return img

def classes(predicted_class):
    class_mapping = {
        0: 'Apple_Leaf_Healthy',
    1: 'Apple_Rust_Leaf',
    2: 'Apple_Scab_Leaf',
    3: 'Bell_Pepper_Healthy_Leaf',
    4: 'Bell_Pepper_Leaf_Curl',
    5: 'Bell_Pepper_Leaf_Spot',
    6: 'Cashew_Anthracnose',
    7: 'Cashew_Gumosis',
    8: 'Cashew_Healthy',
    9: 'Cashew_Leaf_Miner',
    10: 'Cashew_Red_Rust',
    11: 'Cassava_Bacterial_Blight',
    12: 'Cassava_Brown_Spot',
    13: 'Cassava_Green_Miite',
    14: 'Cassava_Healthy',
    15: 'Cassava_Mosaic',
    16: 'Corn_Gray_Leaf_Spot',
    17: 'Corn_Leaf_Blight',
    18: 'Corn_Leaf_Healthy',
    19: 'Corn_Rust_Leaf',
    20: 'Grape_Healthy_Leaf',
    21: 'Grape_Leaf_Black_Rot',
    22: 'Peach_Healthy_Leaf',
    23: 'Peach_Bacterial_Spot',
    24: 'Potato_Healthy_Leaf',
    25: 'Potato_Leaf_Early_Blight',
    26: 'Potato_Leaf_Late_Blight',
    27: 'Raspberry_Healthy_Leaf',
    28: 'Soyabean_Healthy_Leaf',
    29: 'Soyabeen_Diseased_Leaf',
    30: 'Squash_Powdery_Mildew_Leaf',
    31: 'Strawberry_Angular_Leaf_Spot',
    32: 'Strawberry_Blossom_Blight',
    33: 'Strawberry_Graymold',
    34: 'Strawberry_Healthy_Leaf',
    35: 'Strawberry_Leaf_Scorch',
    36: 'Strawberry_Leafspot',
    37: 'Strawberry_Powdery_Mildew_Leaf',
    38: 'Tomato_Early_Blight_Leaf',
    39: 'Tomato_Leaf_Bacterial_Spot',
    40: 'Tomato_Leaf_Healthy',
    41: 'Tomato_Leaf_Late_Blight',
    42: 'Tomato_Leaf_Mosaic_Virus',
    43: 'Tomato_Mold_Leaf',
    44: 'Tomato_Septoria_Leaf_Spot',
    45: 'Tomato_Yellow_Leaf_Curl_Virus',
    46: 'Tomato__Spider_Mites_Two_Spotted_Spider_Mite'
    }
    predicted_class_name = class_mapping.get(predicted_class, 'Unknown Class')
    return predicted_class_name

def predict(image_file):
    img = preprocess_image(image_file)
    preds = model.predict(img)
    predicted_class = np.argmax(preds)
    predicted_class_name = classes(predicted_class)
    return predicted_class_name

def main():
    st.title("Image Classifier")

    # File uploader
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        predicted_class = predict(uploaded_file)
        st.write("Prediction:", predicted_class)

if __name__ == "__main__":
    main()
