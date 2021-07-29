import download
import mdToHtml
import subprocess


def genPdf(title):
    # TODO:: 需要配置全局路径
    exePath = "wkhtmltopdf.exe"
    sourcePath = "./htmls/%s.html" % title
    targetPath = "./pdfs/%s.pdf" % title
    cmd = '"%s" --outline-depth 2 --footer-center [page] "%s" "%s"' % (
        exePath, sourcePath, targetPath)
    print(cmd)
    subprocess.call(cmd)


# C_ID = '6979380367216082957'
C_ID = '6977915766267969549'


def downloadAndGenPdf(cid):
    download.downloadColumn(cid)
    column = mdToHtml.getJSONData("./datas/%s/column.json" % cid)
    title = column["column_version"]["title"]
    print("开始生成html文件")
    mdToHtml.mdToHtml(cid, title)
    print("生成html文件完毕")
    print("开始生成%s.pdf" % title)
    genPdf(title)
    print("%s.pdf生成完毕" % title)


downloadAndGenPdf(C_ID)
