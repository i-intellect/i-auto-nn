from .base import base_model
import tensorflow as tf
from tensorflow.python.framework import dtypes
from tensorflow.contrib import learn

class model_lstm(base_model):

    def __init__(self, params):

        self.params = params

        def lstm_cells(layers):
            if isinstance(layers[0], dict):
                return [tf.nn.rnn_cell.DropoutWrapper(tf.nn.rnn_cell.BasicLSTMCell(layer['steps'],
                                                                                   state_is_tuple=True),
                                                      layer['keep_prob'])
                        if layer.get('keep_prob') else tf.nn.rnn_cell.BasicLSTMCell(layer['steps'],
                                                                                    state_is_tuple=True)
                        for layer in layers]
            return [tf.nn.rnn_cell.BasicLSTMCell(steps, state_is_tuple=True) for steps in layers]

        def dnn_layers(input_layers, layers):
            if layers and isinstance(layers, dict):
                return learn.ops.dnn(input_layers,
                                     layers['layers'],
                                     activation=layers.get('activation'),
                                     dropout=layers.get('dropout'))
            elif layers:
                return learn.ops.dnn(input_layers, layers)
            else:
                return input_layers

        def _lstm_model(X, y):
            stacked_lstm = tf.nn.rnn_cell.MultiRNNCell(lstm_cells(rnn_layers), state_is_tuple=True)
            x_ = learn.ops.split_squeeze(1, time_steps, X)
            output, layers = tf.nn.rnn(stacked_lstm, x_, dtype=dtypes.float32)
            output = dnn_layers(output[-1], dense_layers)
            return learn.models.linear_regression(output, y)

        return _lstm_model

    def fill(self, parameters, training_set):
        pass

    def predict(self):
        pass
