# -*- coding:utf-8 -*-
import markdown
import os
import json


def getJSONData(path):
    with open(path) as f:
        return json.loads(f.read())


def saveFile(path, content):
    with open(path, "a+", encoding="utf-8") as f:
        f.write(content)


def readFile(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


TEMP_PREFIX = """ 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>专栏</title>
    <style>
        %s  
    </style>
</head>
<body>
"""

TEMP_SUFFIX = """
</body>
</html>
"""

extensions = [  # 根据不同教程加上的扩展
    'markdown.extensions.extra',
    'markdown.extensions.codehilite',  # 代码高亮扩展
    'markdown.extensions.toc',
    'markdown.extensions.tables',
    'markdown.extensions.fenced_code',
]


def removeScheme(content):
    index = content.find("---", 4)
    return content[index + 3:]


def mdToHtml(cid, name):
    fname = "./htmls/%s.html" % name
    if os.path.exists(fname):
        os.remove(fname)
    articles = getJSONData("./datas/%s/articles.json" % cid)

    cssContent = readFile("./css/code.css")
    cssContent += readFile("./css/extend.css")

    # print("cssContent",cssContent)

    saveFile(fname, TEMP_PREFIX % cssContent)

    for art in articles:
        article = getJSONData("./datas/%s/%s.json" % (cid, art["article_id"]))
        html = "<h1>%s</h1>" % (article["article_info"]["title"])
        html += markdown.markdown(
            removeScheme(article["article_info"]["mark_content"]), extensions=extensions)
        saveFile(fname, html)
        # break

    saveFile(fname, TEMP_SUFFIX)
