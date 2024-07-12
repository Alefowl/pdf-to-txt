import re


def replace(text : str, numbers : bool, braces : bool) -> str:
  """Replaces curly braces and blocky braces for round braces, and also replace all numbers.
  Args:
      text (str): text where replacement should happen.
      numbers (bool): replace all numbers in a text.
      braces (bool): replace all braces in a text.
  Returns:
      str: text
  """
  if numbers:
    text = re.sub(r'\d+', '', text)

  if braces:
    text = text.replace("[", "(").replace("]", ")")
    text = text.replace("{", "(").replace("}", ")")
  
  return text