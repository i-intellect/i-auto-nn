class base_model(object):
    
    def fill(self, parameters, training_set):
        raise NotImplementedError('Calling method of base_model class is not eligible')

    def predict(self):
        raise NotImplementedError('Calling method of base_model class is not eligible')

    def get_name(self):
    	return 'base'