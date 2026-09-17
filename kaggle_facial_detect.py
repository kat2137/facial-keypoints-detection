import torchvision.models.resnet50
import torch
from torchvision.transforms import v2
import numpy as np
import matplotlib.pyplot as plt
import cv2

PIXSHAPE = 224
TESTSIZE = 60_000

test = cv2.open('data/test.csv')


for image in data:
    image = image.reshape(PIXSHAPE, PIXSHAPE)
    shape_check = image.shape
print(f"Shape of the image: {shape_check}")

#x_train, x_test, y_train, y_test = x[:TESTSIZE], x[TESTSIZE:], y[:TESTSIZE], y[TESTSIZE:]
