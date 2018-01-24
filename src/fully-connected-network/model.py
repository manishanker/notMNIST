# Training and Validation on notMNIST Dataset
# Fully connected network implementation with tensorflow
# ========================================
# [] File Name : model.py
#
# [] Creation Date : January 2018
#
# [] Created By : Ali Gholami (aligholami7596@gmail.com)
# ========================================
import pickle as pickle
import numpy as np 
import tensorflow as tf

# Data destination path
pickle_file = "../../data/notMNIST.pickle"

# Load the data to the RAM
with open(pickle_file, "rb") as f:
    save = pickle.load(f)

    train_dataset = save['train_dataset'] 
    train_labels = save['train_labels']

    valid_dataset = save['valid_dataset']
    valid_labels = save['valid_labels']

    test_dataset = save['test_dataset']
    test_labels = save['test_labels']

    # Free some memory
    del save

    # Display the openend files 
    print("Training Set ", train_dataset.shape, train_labels.shape)
    print("Validation Set", valid_dataset.shape, valid_labels.shape)
    print("Test Set", test_dataset.shape, test_labels.shape)


# Reformat to the one-hot encoding mode
# def reformatData(dataset, labels):


    