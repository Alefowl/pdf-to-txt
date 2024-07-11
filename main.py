# Python std.
from typing import List, Dict
import argparse
import re

# Imported library.
import fitz

from src.utils import ( set_fitz, get_pdf, close_pdf )
from src.automatic import ( convert )
from src.interactive import ( start )

def main(filename : str, output : str, symbol : str, upper_limit : int,
           low_cutoff : int, high_cutoff : int, nums : bool, braces : bool,
           ligatures : bool, align : str, dehy : bool, mode : bool, ocr : bool) -> None:
  
  # Settings for fitz.
  set_fitz(align=align, ligatures=ligatures, dehy=dehy)
  
  # Get pdf file.
  pdf = get_pdf(filename=filename, ligatures=ligatures, align=align, dehy=dehy)
  
  if (mode):
    start(pdf, output)
  else:
    convert(pdf_file=pdf, output=output, symbol=symbol, upper_limit=upper_limit, 
            low_cutoff=low_cutoff, high_cutoff=high_cutoff, nums=nums, braces=braces)
  
  # Close the pdf file.
  close_pdf(pdf)
  
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
  
  # Use interactive mode.
  parser.add_argument("-mode", metavar='-M', nargs='?', 
                      type=bool, help='Use interactive mode.',
                      default=False)
  
  # OCR
  parser.add_argument('-ocr', metavar='-R', nargs='?',
                      type=bool, help='Use OCR for pdf.',
                      default=False)
  
  args = parser.parse_args()
  
  main(filename=args.filename, output=args.output, 
            symbol=args.symbol, upper_limit=args.upper,
            low_cutoff=args.lcut, high_cutoff=args.hcut,
            nums=args.nums, braces=args.braces, ligatures=args.ligatures,
            align=args.align, dehy=args.dehy, mode=args.mode, ocr=args.ocr)
