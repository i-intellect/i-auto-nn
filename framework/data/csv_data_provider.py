import pandas as pd
from dateutil.parser import parse as parse_timestamp
from framework.data.data_provider import data_provider

class csv_data_provider(data_provider):

	data_loaded = False
	data_divided = False
	parameters = {}

	def __init__(self, params):
		
		self.data_loaded = False
		self.parameters = params
		self.data = None

	def get_data(self, columns = None):
		if not self.data_loaded:
			self.load_data()

		iterable = columns
		if iterable is None:
			iterable = self.data
		
		result = pd.DataFrame()
		for col in iterable:
			result[col.replace('  ', ' ')] = self.data[col]
		
		return result

	def get_training_set(self, columns = None):
		if not self.data_divided:
			self.divide_data()

		iterable = columns
		if iterable is None:
			iterable = self.training_set
		
		result = pd.DataFrame()
		for col in iterable:
			result[col] = self.training_set[col]
		
		return result


	def get_testing_set(self, columns = None):
		if not self.data_divided:
			self.divide_data()
		
		iterable = columns
		if iterable is None:
			iterable = self.testing_set
		
		result = pd.DataFrame()
		for col in iterable:
			result[col] = self.testing_set[col]
		
		return result

	def load_data(self):
		data = pd.read_csv(self.parameters['filepath'], index_col = False, sep=';', header=0)
		self.shape = data.shape
		self.data = data

		if 'index_column' in self.parameters.keys():
			data.set_index(self.parameters['index_column'])

		self.data_loaded = True


	def divide_data(self):
		if not self.data_loaded:
			self.load_data()

		if self.parameters['testing_set_size'] > 0 and self.parameters['testing_set_size'] < 1:
			cnt = data.shape[0]
			testing_set_size = int(cnt*self.parameters['testing_set_size'])
			training_set_size = cnt - testing_set_size
			self.training_set = self.data[:training_cnt]
			self.testing_set = self.data[training_cnt:]

		elif self.parameters['testing_set_size'] >= 1: 
			tss = self.data.shape[0] - int(self.parameters['testing_set_size'])
			self.training_set = self.data[:tss]
			self.testing_set = self.data[tss:]
		else:
			raise ValueError('"testing_set_size" has wrong value: ' + str(params.testing_set_size))

		self.data_divided = True
