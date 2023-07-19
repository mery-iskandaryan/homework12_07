def validation(origin_function):
	def wrapper(*args, **kwargs):
		if all(isinstance(i, int) for i in args):
			return origin_function(*args, **kwargs)
		else:
			raise Exception('Not valid arguments.')
	return wrapper

@validation
def hello(*args):
	print('Hello')

hello(58.5,1,2,3)
