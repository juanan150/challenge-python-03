# Resolve the problem!!
import re


def run():
    # Start coding here
    with open('encoded.txt', 'r',encoding='utf-8') as f:
        text = f.read()

    pattern = re.compile(r'[a-z]*')
    secret_text=''.join(pattern.findall(text))
    print(secret_text)

if __name__ == '__main__':
    run()
