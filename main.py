def morning (func):
  def wrapper(*args_for_func):
    return ' '.join((func(*args_for_func), 'good morning'))
  return wrapper


@morning 
def greet(name):
    print(greet('Mary'))



