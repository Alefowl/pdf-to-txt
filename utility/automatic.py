# Imported libraries.
from sys import flags
import fitz

# Stl
from typing import ( List, Any )

from utility.formatting import replace


# None interactive mode.
def convert(pdf_file : fitz.open, output : str, upper_limit : int, flags : int,
  low_cutoff : int, high_cutoff : int, nums : bool, braces : bool) -> None:
  """Function for automatic pdf to text conversion.
  Args:
      pdf_file (_type_): path to pdf file.
      output (str): name of the output file.
      upper_limit (int): upper limit for number of characters diff between 
      the end of paragraph and beginning of a new one.
      low_cutoff (int): pages from the beginning of the pdf file that shouldn't be converted.
      high_cutoff (int): pages at the end of the pdf file that shouldn't be converted.
      nums (bool): replace all numbers with empty spaces.
      braces (bool): replace all {} and [] with ().
  """
  
  text   : str = ""
  buffer : str = ""
  lines  : List[Any] = []
  for page_num in range(low_cutoff,
                        high_cutoff if high_cutoff is not None else pdf_file.page_count):
      
    lines = pdf_file[page_num].get_text(flags=flags).split('\n')
      
    for i, line in enumerate(lines):
      # Chapter name probably.
      if 1 < len(line) <= upper_limit and line[0].isupper():
          buffer += f"{line}\n\n"
        # Not a chapter name.
      elif len(line) > 1:
          # Start of a paragraph ?
          if i + 1 < len(lines) and any(lines[i + 1]):
            # Probably
            if line.endswith(('.', '?', '!')) and lines[i + 1][0].isupper() and len(line) <= len(lines[i + 1]) - 6:
              buffer += f"{line}\n\n"
            # No
            else:
              buffer += f"{line}\n"
          # No  
          else:
            buffer += f"{line}\n"
        
    if len(buffer) != 0:
      # Delete numbers and braces from text.
      buffer = replace(buffer, nums, braces)
      text += buffer
      buffer = ""
  with open(output, '+w', encoding='utf-8') as f:
    f.write(text)
  
  return None
