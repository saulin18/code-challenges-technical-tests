# 5 kyu
# Context manager decorator
# Your task in this kata is to implement simple version of contextlib.contextmanager.

# The decorator will be used on a generator functions and use the part of function before yield as 
# context manager's "enter section" and the part after the yield as "exit section".

# If exception occurs inside the context of the with statement, the exception should be passed to 
# the generator via its throw method.
# Examples:
# @contextmanager
# def file_opened(file):
#     fp = open(file)
#     try:
#         yield fp
#     finally:
#         fp.close()

# with file_opened('a.txt') as fp:
#     print fp.readline()
    
# @contextmanager
# def transaction(connection):
#     connection.begin()
#     try:
#         yield
#     except:
#         connection.rollback()
#         raise
#     else:
#         connection.commit()

# with transaction():
#     # ...
#     raise Exception()
# Note: contextlib as been forbidden, write your own...

from typing import Generator
class MyContextManager:
    def __init__(self, generator: Generator):
        self.generator = generator
    
    def __enter__(self, *args, **kwargs):
        return next(self.generator)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            next(self.generator)
        except StopIteration:
            return None 
        except BaseException as e:
            self.generator.throw(exc_type, exc_val, exc_tb)

def contextmanager(f):
    def wrapper(*args, **kwargs):
        return MyContextManager(f(*args, **kwargs))
    return wrapper


        