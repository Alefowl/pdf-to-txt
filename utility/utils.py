import fitz


def set_fitz(align : str, ligatures : bool, dehy : bool) -> int:
  """Function for settings for fitz.
  Args:
      align (str): Text alignment, can be J - justify, L - left,
      R - right, C - center.
      ligatures (bool): Remove all ligatures in the text.
      dehy (bool): Remove all dehyphinated lines from the text.
  """
  
  flags : int = 0
  flags |= fitz.TEXT_PRESERVE_LIGATURES if ligatures else 0
  flags |= fitz.TEXT_DEHYPHENATE if dehy else 0
  
  match align:
    case 'J':
      flags |= fitz.TEXT_ALIGN_JUSTIFY
    case 'L':
      flags |= fitz.TEXT_ALIGN_LEFT
    case 'R':
      flags |= fitz.TEXT_ALIGN_RIGHT
    case 'C':
      flags |= fitz.TEXT_ALIGN_CENTER
    case _:
        pass

  return flags


def get_pdf(filename : str) -> fitz.open:
  pdf = fitz.open(filename=filename)
  return pdf


def close_pdf(pdf : fitz.open) -> None:
  pdf.close()
