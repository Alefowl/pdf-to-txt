from re import sub

def process(text : str, pattern : str) -> str:
  processed_data = ''
  word_buffer = ''
  line_length = 0

  text = sub(pattern, '', text)
  
  for char in text:
    if char == ' ':
      if line_length + len(word_buffer) > 160:
        processed_data += '\n' + word_buffer
        line_length = len(word_buffer)
      else:
        processed_data += word_buffer
        line_length += len(word_buffer)
        word_buffer = ''
    else:
      word_buffer += char
  return processed_data