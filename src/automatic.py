import fitz
from utils import set_fitz, replace
from typing import List

# None interactive mode.
def convert(pdf_file, output : str, symbol : str, upper_limit : int,
           low_cutoff : int, high_cutoff : int, nums : bool, braces : bool) -> None:
  
  text  : str = ""
  lines : List[str] = []
  
  # with open(output, 'w+', encoding='utf-8') as file:
    
  for page_num in range(low_cutoff,
                        high_cutoff if high_cutoff is not None else pdf_file.page_count):
      
    lines = pdf_file[page_num].get_text().split('\n')
      
    for i, line in enumerate(lines):
      # Chapter name probably.
      if 1 < len(line) <= upper_limit and line[0].isupper():
          text += f"{line}\n\n"
        # Not a chapter name.
      elif len(line) > 1:
          # Start of a paragraph ?
          if i + 1 < len(lines) and any(lines[i + 1]):
            # Probably
            if line.endswith(('.', '?', '!')) and lines[i + 1][0].isupper() and len(line) <= len(lines[i + 1]) - 6:
              text += f"{line}\n\n"
            # No
            else:
              text += f"{line}\n"
          # No  
          else:
            text += f"{line}\n"
        
      if len(text) != 0:
        # Delete numbers and braces from text.
        text = replace(text, nums, braces)
        # Write text to the file.
        # file.write(text)
        text = ""
  
  pdf_file.close()
  
  return None


def convert_ocr(pdf_file, output : str, symbol : str, upper_limit : int,
           low_cutoff : int, high_cutoff : int, nums : bool, braces : bool) -> None:
  pass
