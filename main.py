import pandas as pd
import sys
import csv
import numpy as np
import pickle
import operator
import re
import string
import matplotlib.pyplot as plt

from plot_keras_history import plot_history
from sklearn.model_selection import train_test_split
from sklearn.metrics import multilabel_confusion_matrix
from keras_contrib.utils import save_load_utils

from keras import layers
from keras import optimizers

from keras.models import Model
from keras.models import Input

from keras_contrib.layers import CRF
from keras_contrib import losses
from keras_contrib import metrics

import sys
import csv
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

dataset = 'SINGGALANG.tsv'
data = pd.read_csv(dataset, sep='\t', error_bad_lines=False, engine="python", names=['word', 'tag'], quoting=csv.QUOTE_NONE)
print(data.head())

