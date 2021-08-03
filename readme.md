

## 功能介绍
把掘金**某个专栏或者文章**内容下载到本地，并生成pdf文件。

生成的pdf功能支持：
1. 大纲目录
2. 代码高亮
3. 文章图片
4. 链接点击

其他：
1. 支持自定义pdf显示的样式

## 预览
[我的掘金前端周栏.pdf](./pdfs/我的掘金前端周栏.pdf)     
[前端基础进阶.pdf](./pdfs/前端基础进阶.pdf)     

## 思路

1. 通过专栏ID获取专栏信息，文章列表和文章详情
2. 下载JSON格式的数据到本地
3. 把markdown语法的文章内容转为html格式，并生成html文件
4. 借助`wkhtmltopdf.exe`生成pdf文件



## 开发环境
1.  windows 10
2.  Python 3.9.1

## 使用

请注意运行环境 windows以及Python版本

1. 下载 [wkhtmltopdf](https://wkhtmltopdf.org/), 并配置环境变量
2. 下载本地项目，进入项目文件
3. 执行命令 
acid: 专栏ID或者文章ID
type: 默认为专栏`c`，如果是文章请输入`a`
```python   
python main.py [acid] [type]

```

## 已知问题
1. 中文路径问题
    那就使用英文路径吧，文件名是中文没问题


## 预览
项目`pdfs\前端基础进阶.pdf`是已经生成好的pdf文件。


### 参考引用

[python+markdown+Pygments高亮代码](https://blog.csdn.net/JONE_WUQINGJIANG/article/details/100511760)
