import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []

    begin=0
    end=window_size
    for i in range(len(series) - window_size):
        X.append(series[begin:end])
        begin += 1
        end += 1
    y = series[window_size:]
    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    model = Sequential()
    model.add(LSTM(units=5, input_shape=(window_size, 1)))
    model.add(Dense(1))
    return model

### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    import string
    uniq = ''.join(set(text))
    punctuation = ['!', ',', '.', ':', ';', '?']
    alphabets = list(string.ascii_lowercase)
    good = punctuation + alphabets
    allowed = [x for x in uniq if x in good]
    for char in text:
        if char not in allowed:
            text = text.replace(char, ' ')

    return text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    import math
    begin = 0
    end = window_size
    inputs = []
    outputs = []
    for i in range(0,len(text) - window_size,step_size):
        inputs.append(text[begin:end])
        outputs.append(text[end])
        begin += step_size
        end = begin+window_size

    return inputs,outputs

# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    model = Sequential()
    model.add(LSTM(units=200, input_shape=(window_size, num_chars)))
    model.add(Dense(num_chars, activation='softmax'))
    return model
