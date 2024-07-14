import argparse
import re


def replace(filename : str, pattern) -> None:
    text : str = ""
    with open(filename, '+r', encoding='utf-8') as file:
        text = file.read()
    text = re.sub(pattern, '', text);
    with open(f"{filename}.txt", '+w', encoding='utf-8') as file:
        file.write(text)    
    return None
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-pattern', type=str,
                        nargs='?')
    
    parser.add_argument('-filename', type=str,
                        nargs='?', required=True)
    
    args = parser.parse_args()
    
    replace(filename=args.filename, pattern=args.pattern)
