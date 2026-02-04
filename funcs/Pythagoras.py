import numpy as np

def hypotenuse(a,b):
  '''
  Function calculates the hypotenuse of a right angled triangle
  
  
  '''
  return np.sqrt((a**2) + (b**2))

print('The hypotenuse of a right-angled triangle with side lengths of {0} and {1} is {2:.f}'.format(a, b, hypotenuse(a,b)))


  
