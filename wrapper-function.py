
#@wraps
#Implement the functools.wraps decorator, which is used to preserve the name and docstring of a decorated function. 
# Your decorator must not modify the behavior of the decorated function. Here's an example :
#
#def identity(func):
#  @wraps(func)
#  def wrapper(*args, **kwargs):
#    """Wraps func"""
#    return func(*args, **kwargs)
#  return wrapper
#
#@identity
#def return_one():
#  """Return one"""
#  return 1
#  
#return_one.__name__ == 'return_one' # If wraps hadn't been used, __name__ would be equal to 'wrapper'
#return_one.__doc__ == 'Return one' # If wraps hadn't been used, __doc__ would be equal to 'Wraps func'
#Note: of course, you may not use the functools module for this kata.

def wraps(original_func): 
    def decorator(wrapped_func): 
        wrapped_func.__name__ = original_func.__name__ if hasattr(original_func, '__name__') else "wrapper"
        wrapped_func.__doc__ = original_func.__doc__    if hasattr(original_func, '__doc__') else "Wraps func"
        return wrapped_func
    return decorator

@wraps
def return_one():
    """Return one"""
    return 1

print(return_one.__name__)  # Output: example_function
print(return_one.__doc__)   # Output: This is an example function.