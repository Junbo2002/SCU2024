import re

data = '{"ID":10985280,"Title":"2012 m. "Radiocentro" Top 100","numtracks":66,"duration":13712}'

pattern = r'"Title":"[*]",'
match = re.search(pattern, data)
print(match)
if match:
    extracted_title = match.group(1)
    escaped_title = extracted_title.replace('"', '\\"')
    print(escaped_title)