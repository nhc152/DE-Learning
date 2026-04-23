import html.parser
import sys
import re

class HTMLFilter(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.lines = []

    def handle_starttag(self, tag, attrs):
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'p', 'li', 'button', 'a']:
            prefix = ""
            if tag.startswith('h') and len(tag) == 2 and tag[1].isdigit():
                prefix = "#" * int(tag[1]) + " "
            self.lines.append("\n" + prefix)

    def handle_endtag(self, tag):
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'p', 'li']:
            self.lines.append("\n")

    def handle_data(self, data):
        text = data.strip()
        if text:
            self.lines.append(text + " ")

parser = HTMLFilter()
with open(sys.argv[1], 'r', encoding='utf-8') as f:
    parser.feed(f.read())

output = re.sub(r'\n\s*\n', '\n', "".join(parser.lines))

with open(sys.argv[2], 'w', encoding='utf-8') as f:
    f.write(output)
