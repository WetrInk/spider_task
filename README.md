Modules Acquired:
Requests (https://github.com/requests/requests)
BeautifulSoup (http://www.crummy.com/software/BeautifulSoup/)


这个爬虫借鉴了前一个的经验之后，写起来还是比较流畅的。
但是gb2312编码的问题还是困扰了我一段时间。改用requestsh后解决了（urllib.request好像解决起来比较麻烦，返回的HTTPResponse对象可选方法不多啊）。

但是面向编程还是用的不好。应该分拆出来的类全部弄进一个里去了（无奈）。