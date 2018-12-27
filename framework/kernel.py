from lstm import model_lstm
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import make_classification

class kernel():

    def __init__(self, params):
        self.model = model_lstm(params)

    def grid_search(self):
        grid = GridSearchCV(estimator=neural_network, param_grid=hyperparameters)

        grid_result = grid.fit(features, target)