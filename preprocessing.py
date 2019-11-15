from scipy.io import loadmat
from sklearn.decomposition import PCA
import numpy as np
import math

import pdb

def run():
    preprocessed_data = [] 
    labels = []

    for i in range(1, 10):
        filename = 'p' + str(i)
        data = loadmat(filename)
        meta = data['meta'][0][0]
        info = data['info'][0]
        images = data['data']

        total_trials = 360 

        for j in range(total_trials):
            image = get_image(images, j)
            epoch = get_epoch(info, j)
            label = get_label(info, j)

            if epoch == 0 or epoch == 1 or epoch == 2:
                preprocessed_data.append(image)
                labels.append(label)

    pca = PCA(n_components=100)
    return pca.fit_transform(preprocessed_data), labels

def get_image(images, index):
    image = images[index][0][0]

    # truncate the image so each patient image is same length
    max_image_size = 19750
    # center image truncation
    margin = (len(image) - max_image_size) / 2
    truncated_image = image[math.floor(margin):][:(len(image)-math.floor(margin)-math.ceil(margin))]

    return truncated_image

def get_epoch(info, index):
    return info[index][4][0][0]

def get_label(info, index):
    categories = [
            'manmade',
            'building',
            'buildpart',
            'tool',
            'furniture',
            'animal',
            'kitchen',
            'vehicle',
            'insect',
            'vegetable',
            'bodypart',
            'clothing'
            ]
    category = info[index][0][0]
    label = categories.index(category)
    return label
