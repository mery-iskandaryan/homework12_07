import time
def memoize(origin_function):
	def wrapper_function(*args, **kwargs):
		cache = {}
		if origin_function(*args, **kwargs) not in cache:
			cache[args] = origin_function(*args, **kwargs)

		return cache[args]
	return wrapper_function



