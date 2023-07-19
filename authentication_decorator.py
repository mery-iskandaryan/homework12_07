passwords = ['12345','hello','bye']

def authentication(origin_function):
	def wrapper(password, *args, **kwargs):
		if password in passwords:
			return origin_function(password, *args, **kwargs)
		else:
			raise Exception('Please login to continue.')
		
	return wrapper


@authentication
def hello(password):
	print('hello')

print('With correct password.')
hello('12345')
print('\n\nWith incorrect password.')
hello('1245')
