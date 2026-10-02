# Wrap deck.html (artifact fragment) into a full index.html for Netlify
src = open("deck.html", encoding="utf-8").read()
head, body = src.split("<!--BODY-->", 1)
html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + head + '</head>\n<body>\n' + body + '</body>\n</html>\n')
open("index.html", "w", encoding="utf-8").write(html)
print("built index.html", len(html))
