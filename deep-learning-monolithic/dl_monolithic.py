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
os.environ['PYTHONHASHSEED'] = str(SEED)
random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)

# Define data directories
healthy_brain_dir = 'healthy_brain_images'
npd_brain_dir = 'synthetic_NPD'

# Define image dimensions and batch size
img_width, img_height = 224, 224
batch_size = 32

# Load and label images
X = []
y = []






for folder, label in [(healthy_brain_dir, 0), (npd_brain_dir, 1)]:
    for filename in os.listdir(folder):
        if filename.endswith(".png"):
            img = tf.keras.preprocessing.image.load_img(
                os.path.join(folder, filename),
                target_size=(img_width, img_height)
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





# Define the CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(img_width, img_height, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
train_generator = train_datagen.flow(X_train, y_train, batch_size=batch_size)
test_generator = test_datagen.flow(X_test, y_test, batch_size=batch_size)

model.fit(train_generator, epochs=15, validation_data=test_generator)

# Evaluate the model on test data
y_pred = model.predict(test_generator)
y_pred_binary = np.round(y_pred)


accuracy = accuracy_score(y_test, y_pred_binary)
precision = precision_score(y_test, y_pred_binary)

print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print("counter: ", Counter(y_test))
