import numpy as np

def hypotenuse(a,b):
  '''
  Function calculates the hypotenuse of a right angled triangle

  data types:
  a: float
  b: float
  output: float
  '''
  print('The hypotenuse of a right-angled triangle with side lengths of {0:.2f} and {1:.2f} is {2:.2f}'.format(a, b, np.sqrt((a**2) + (b**2))))
  return  np.sqrt((a**2) + (b**2))

