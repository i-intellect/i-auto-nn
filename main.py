from framework.data import csv_data_provider as dp

data_provider_parameters = {
	'filepath': 'data/data.csv',
	'missing_values_processing_policy' : None
}
data_provider = dp(data_provider_parameters)

data_provider.load_data()
