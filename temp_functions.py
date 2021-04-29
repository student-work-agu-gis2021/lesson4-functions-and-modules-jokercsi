"""
script file (funcctions)
"""

def temp_classifier(temp_celsius):
  """
  this function is classify the tempertures in number.
  param: temp_celsisu : int, float
  return: 1,2,3: int
  """

  #classifying part
  if(temp_celsius < -2):
    return 0
  elif (temp_celsius >= -2 )and (temp_celsius < 2):
    return 1
  elif (temp_celsius >= 2 )and (temp_celsius < 15):
    return 2  
  else :
    return 3

def fahr_to_celsius(temp_fahreheit):
  """
    conversion formula from Fahrenheit to Celsius
    :return: converted_temp : number
  """
  converted_temp = (temp_fahreheit - 32) / 1.8
  return converted_temp