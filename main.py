# Python stl.
import argparse

# Imported library.
import fitz

# Project files.
from utility.utils import ( set_fitz, get_pdf, close_pdf )
from utility.automatic import ( convert )


def main(filename : str, output : str, upper_limit : int, low_cutoff : int, 
    high_cutoff : int, nums : bool, braces : bool, ligatures : bool, 
    align : str, pattern : str) -> int:
  
  # Settings for fitz.
  set_fitz(align=align, ligatures=ligatures, dehy=True)
  
  # Get pdf file.
  try:
    pdf = get_pdf(filename=filename, ligatures=ligatures, align=align, dehy=True)
  except Exception as e:
    print(f"Error: {e}")
    return 1
  
  convert(pdf_file=pdf, output=output, upper_limit=upper_limit,
          low_cutoff=low_cutoff, high_cutoff=high_cutoff, nums=nums,
          braces=braces, pattern=pattern)
  
  # Close the pdf file.
  close_pdf(pdf)
  
  return 0


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
  # parser.add_argument('-symbol', metavar='-S', nargs='?',
  #                     type=str, help="If program has troubles processing text.",)
  # Derpicated.
  
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
    
  # OCR hard to do it atm.
  # parser.add_argument('-ocr', metavar='-R', nargs='?',
  #                     type=bool, help='Use OCR for pdf.',
  #                     default=False)
  
  # Pattern for dehyphination.
  parser.add_argument('-pat', metavar='-P', nargs='?',
                      type=str, help="Pattern for dehyphenation", default="-\n")
  
  args = parser.parse_args()
  
  main(filename=args.filename, output=args.output, 
      upper_limit=args.upper,
      low_cutoff=args.lcut, high_cutoff=args.hcut,
      nums=args.nums, braces=args.braces, ligatures=args.ligatures,
      align=args.align, pattern = args.pat)
