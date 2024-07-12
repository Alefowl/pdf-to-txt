import fitz


def set_fitz(align : str, ligatures : bool, dehy : bool) -> None:
  """Function for settings for fitz.
  Args:
      align (str): Text alignment, can be J - justify, L - left,
      R - right, C - center.
      ligatures (bool): Remove all ligatures in the text.
      dehy (bool): Remove all dehyphinated lines from the text.
  """

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
  return None


def get_pdf(filename : str, ligatures : bool, align : str, dehy : bool):
  set_fitz(ligatures=ligatures, align=align, dehy=dehy)
  pdf = fitz.open(filename=filename)
  return pdf


def close_pdf(pdf) -> None:
  pdf.close()
