import urllib.request

# 需要爬取的网址
url = "https://www.douban.com/"

# 请求
request = urllib.request.Request(url)

# 爬取结果
response = urllib.request.urlopen(request)

data = response.read()

# 设置解码方式
data = data.decode('utf-8')

# 保存在当前路径的my.html文件中
urllib.request.urlretrieve(url, './python/my.html')

# 首先先创建一个文件对象，打开方式为w
# f = open("test.html", "w")
# f.write(data)

# 打印结果
print(data)

# 打印爬取网页的各类信息

print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())