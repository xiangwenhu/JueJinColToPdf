# -*- coding:utf-8 -*-
import requests
import json
import os

URL = {
    "column": "https://api.juejin.cn/content_api/v1/column/detail",
    "articles": "https://api.juejin.cn/content_api/v1/column/articles_cursor",
    "article": "https://api.juejin.cn/content_api/v1/article/detail"
}

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'authority': 'api.juejin.cn',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8'
}


def getColumn(cid):
    res = requests.get(URL.get("column") + "?column_id=" +
                       cid, headers=headers)
    return res.json()


def getArticleList(cid):
    data = {
        "column_id": cid,
        "cursor": "0",
        "limit": 20,
        "sort": 0
    }
    res = requests.post(URL.get("articles"),
                        data=json.dumps(data), headers=headers)
    return res.json()


def getArticleContent(aid):
    res = requests.post(URL.get("article"),
                        data=json.dumps({
                            "article_id": aid
                        }), headers=headers)
    return res.json()


def ensureDir(dir):
    os.makedirs(dir, mode=0o777, exist_ok=True)


def saveColumn(cid, content):
    folder = "./datas/%s" % cid
    file = "%s/%s.json" % (folder, "column")
    ensureDir(folder);
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)


def saveArticleList(cid, content):
    folder = "./datas/%s" % cid
    file = "%s/%s.json" % (folder, "articles")
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)


def saveArticleContent(cid, aid, content):
    folder = "./datas/%s" % cid
    file = "%s/%s.json" % (folder, aid)
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)


def downloadColumn(cid):

    column = getColumn(cid)
    print("获取专栏信息成功，专栏名称：", column["data"]["column_version"]["title"])
    saveColumn(cid, json.dumps(column["data"]))

    articleList = getArticleList(cid)
    print("articleList", articleList)
    saveArticleList(cid, json.dumps(articleList["data"]))

    articleIds = list(
        map(lambda item: item["article_id"], articleList["data"]))
    print("获取专栏文章列表成功：", articleIds)

    for artId in articleIds:
        artContent = getArticleContent(artId)
        saveArticleContent(cid, artId, json.dumps(artContent["data"]))
        print("文章ID为 %s 的文章下载完毕" % artId)
