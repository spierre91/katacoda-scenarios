#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 12:05:59 2023

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
import random

SEED = 42

random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)


class ImageLoader:
    def __init__(self, img_width, img_height):
        self.img_width = img_width
        self.img_height = img_height

    def load_images_from_directory(self, directory, label):
        images = []
        labels = []
        for filename in os.listdir(directory):
            if filename.endswith(".png"):
                img = tf.keras.preprocessing.image.load_img(
                    os.path.join(directory, filename),
                    target_size=(self.img_width, self.img_height)
                )
                img_array = tf.keras.preprocessing.image.img_to_array(img)
                images.append(img_array)
                labels.append(label)
        return np.array(images), np.array(labels)


class CNNModel:
    def create_model(self, input_shape):
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

    def compile_and_train(self, model, train_generator, test_generator, epochs):
        model.compile(optimizer='adam',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])
        model.fit(train_generator, epochs=epochs, validation_data=test_generator)


class ModelEvaluator:
    def evaluate_model(self, model, test_generator, y_test):
        y_pred = model.predict(test_generator)
        y_pred_binary = np.round(y_pred)
        accuracy = accuracy_score(y_test, y_pred_binary)
        precision = precision_score(y_test, y_pred_binary)
        print(f'Accuracy: {accuracy:.2f}')
        print(f'Precision: {precision:.2f}')


class ImageClassifier:
    def __init__(self, img_width, img_height, batch_size, epochs):
        self.img_width = img_width
        self.img_height = img_height
        self.batch_size = batch_size
        self.epochs = epochs

    def train_model(self, X_train, X_test, y_train, y_test):
        train_datagen = ImageDataGenerator(
            rescale=1./255,
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            horizontal_flip=True
        )

        test_datagen = ImageDataGenerator(rescale=1./255)

        train_generator = train_datagen.flow(X_train, y_train, batch_size=self.batch_size)
        test_generator = test_datagen.flow(X_test, y_test, batch_size=self.batch_size)

        cnn_model = CNNModel()
        model = cnn_model.create_model((self.img_width, self.img_height, 3))
        cnn_model.compile_and_train(model, train_generator, test_generator, self.epochs)

        evaluator = ModelEvaluator()
        evaluator.evaluate_model(model, test_generator, y_test)


if __name__ == '__main__':
    HEALTHY_BRAIN_DIR = 'healthy_brain_images'
    NPD_BRAIN_DIR = 'synthetic_NPD'
    IMG_WIDTH, IMG_HEIGHT = 224, 224
    BATCH_SIZE = 32
    EPOCHS = 15

    img_loader = ImageLoader(IMG_WIDTH, IMG_HEIGHT)

    X_healthy, y_healthy = img_loader.load_images_from_directory(HEALTHY_BRAIN_DIR, 0)
    X_npd, y_npd = img_loader.load_images_from_directory(NPD_BRAIN_DIR, 1)

    X = np.concatenate([X_healthy, X_npd])
    y = np.concatenate([y_healthy, y_npd])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    classifier = ImageClassifier(IMG_WIDTH, IMG_HEIGHT, BATCH_SIZE, EPOCHS)
    classifier.train_model(X_train, X_test, y_train, y_test)
