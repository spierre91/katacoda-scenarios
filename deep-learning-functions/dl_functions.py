#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 11:41:03 2023

@author: sadrach.pierre
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 15:39:49 2023

@author: sadrach.pierre
"""

import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import train_test_split
from collections import Counter
import random

SEED = 42

random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)

# Define data directories
HEALTHY_BRAIN_DIR = 'healthy_brain_images'
NPD_BRAIN_DIR = 'synthetic_NPD'
IMG_WIDTH, IMG_HEIGHT = 224, 224
BATCH_SIZE = 32

def load_images_from_directory(directory, label, img_width, img_height):
    images = []
    labels = []
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            img = tf.keras.preprocessing.image.load_img(
                os.path.join(directory, filename),
                target_size=(img_width, img_height)
            )
            img_array = tf.keras.preprocessing.image.img_to_array(img)
            images.append(img_array)
            labels.append(label)
    return np.array(images), np.array(labels)





def create_cnn_model(input_shape):
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    return model




def compile_and_train_model(model, train_generator, test_generator, epochs):
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    model.fit(train_generator, epochs=epochs, validation_data=test_generator)

def evaluate_model(model, test_generator, y_test):
    y_pred = model.predict(test_generator)
    y_pred_binary = np.round(y_pred)
    accuracy = accuracy_score(y_test, y_pred_binary)
    precision = precision_score(y_test, y_pred_binary)
    print(f'Accuracy: {accuracy:.2f}')
    print(f'Precision: {precision:.2f}')
    print("counter: ", Counter(y_test))






def main():
    X = []
    y = []   
    for folder, label in [(HEALTHY_BRAIN_DIR, 0), (NPD_BRAIN_DIR, 1)]:
        for filename in os.listdir(folder):
            if filename.endswith(".png"):
                img = tf.keras.preprocessing.image.load_img(
                    os.path.join(folder, filename),
                    target_size=(IMG_WIDTH, IMG_HEIGHT)
                )
                img_array = tf.keras.preprocessing.image.img_to_array(img)
                X.append(img_array)
                y.append(label)
    
    # Convert lists to NumPy arrays
    X = np.array(X)
    y = np.array(y)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Data augmentation for training images
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True
    )

    # Data augmentation for testing/validation images (only rescaling)
    test_datagen = ImageDataGenerator(rescale=1./255)

    # Train the model
    train_generator = train_datagen.flow(X_train, y_train, batch_size=BATCH_SIZE)
    test_generator = test_datagen.flow(X_test, y_test, batch_size=BATCH_SIZE)

    # Define the CNN model
    model = create_cnn_model((IMG_WIDTH, IMG_HEIGHT, 3))

    # Compile and train the model
    compile_and_train_model(model, train_generator, test_generator, epochs=15)

    # Evaluate the model on test data
    evaluate_model(model, test_generator, y_test)

if __name__ == "__main__":
    main()

