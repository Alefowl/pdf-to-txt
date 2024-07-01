# Python std.
from typing import List, Dict
import argparse
import re

# Imported library.
import fitz


# Util function.
def replace(text : str, numbers : bool, braces : bool) -> str:
  if numbers:
    text = re.sub(r'\d+', '', text)
  if braces:
    text = text.replace("[", "(").replace("]", ")")
    text = text.replace("{", "(").replace("}", ")")
  
  return text


# Main function.
def convert(filename : str, output : str, symbol : str, upper_limit : int,
           low_cutoff : int, high_cutoff : int, nums : bool, braces : bool,
           ligatures : bool, align : str, dehy : bool) -> None:
    
  pdf_file = fitz.open(filename)
  text  : str = ""
  lines : List[str] = []
    
  fitz.TEXT_PRESERVE_LIGATURES = 1 if ligatures else 0
  fitz.TEXT_DEHYPHENATE = 1 if dehy else 0
  
  match align:
    case 'J':
      fitz.TEXT_ALIGN_JUSTIFY = 1
      fitz.TEXT_ALIGN_LEFT    = 0
      fitz.TEXT_ALIGN_RIGHT   = 0
      fitz.TEXT_ALIGN_CENTER  = 0
    case 'L':
      fitz.TEXT_ALIGN_JUSTIFY = 0
      fitz.TEXT_ALIGN_LEFT    = 1
      fitz.TEXT_ALIGN_RIGHT   = 0
      fitz.TEXT_ALIGN_CENTER  = 0
    case 'R':
      fitz.TEXT_ALIGN_JUSTIFY = 0
      fitz.TEXT_ALIGN_LEFT    = 0
      fitz.TEXT_ALIGN_RIGHT   = 1
      fitz.TEXT_ALIGN_CENTER  = 0
    case 'C':
      fitz.TEXT_ALIGN_JUSTIFY = 0
      fitz.TEXT_ALIGN_LEFT    = 0
      fitz.TEXT_ALIGN_RIGHT   = 0
      fitz.TEXT_ALIGN_CENTER  = 1
    case _:
      pass
    
  with open(output, 'w+', encoding='utf-8') as file:
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
        file.write(text)
        text = ""
  
  pdf_file.close()
  
  return None


if __name__ == '__main__':
  parser = argparse.ArgumentParser(
      prog="PDF to Text converter.",
      description="Converts PDF file to valid TXT file for easier upload."
  )
  # Filename.
  parser.add_argument('-filename', metavar='-F', nargs='?', 
                      type=str, help="Path to a pdf file.",
                      required=True)
  # Output filename.
  parser.add_argument('-output', metavar='-O', nargs='?',
                      type=str, help='Name of the txt file.',
                      default='output.txt')
  # Errored symbol.
  parser.add_argument('-symbol', metavar='-S', nargs='?',
                      type=str, help="If program has troubles processing text.",)
  # Upper limit.
  parser.add_argument('-upper', metavar='-U', nargs='?',
                      type=int, help="Upper limit of nummber of characters in chapter names.",
                      default=25)
  
  # Low page cutoff.
  parser.add_argument('-lcut', metavar='-L', nargs='?',
                      type=int, help="Pages from the start of pdf that are not needed.",
                      default=0)
  
  # High page cutoff.
  parser.add_argument('-hcut', metavar='-H', nargs='?',
                      type=int, help='Pages at the end of the pdf that are not needed.')
  
  # Deletes all the numbers.
  parser.add_argument('-nums', metavar='-N', nargs='?',
                      type=bool, help='Deletes all the numbers in the text.',
                      default=False)
  
  # Replaces braces [], {} with ().
  parser.add_argument('-braces', metavar='-B', nargs='?',
                      type=bool, help='Replaces all [] with ().', default=False)
  
  # Replace the ligatures.
  parser.add_argument('-ligatures', metavar='-L', nargs='?',
                      type=bool, help='Replaces ligatures.', default=True)
  
  # Text alignment.
  parser.add_argument('-align', metavar='-A', nargs='?',
                      type=str, help='Specifies text alignment. L for left\n, C for center\n,' +
                      'R for right\n, J for justify', default='J')
  
  # Dehypenate the text.
  parser.add_argument('-dehy', metavar='-D', nargs='?',
                      type=bool, help='Ignore hyphens at line ends and join with next line', 
                      default=True)
  
  args = parser.parse_args()
  
  convert(filename=args.filename, output=args.output, 
          symbol=args.symbol, upper_limit=args.upper,
          low_cutoff=args.lcut, high_cutoff=args.hcut,
          nums=args.nums, braces=args.braces, ligatures=args.ligatures,
          align=args.align, dehy=args.dehy)
