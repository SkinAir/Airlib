`**xray_windows_amd64.exe webscan --listen 127.0.0.1:8800 --html-output v.html**`

[代理模式进行扫描 - xray 安全评估工具文档](https://docs.xray.cool/#/tutorial/webscan_proxy)

# x-ray

## 服务扫描

检测单个目标

```
./xray servicescan --target 127.0.0.1:8009
```

 检测多个目标

```
./xray servicescan --target-file 文件路径
```

其中文件内容为：

```
10.3.0.203:8009
127.0.0.1:8009
```



将结果输入到html/json报告中

```
./xray servicescan --target url --html-output xxx.html
```

```
./xrat servicescan --target url --json-output xxx.json
```

## 代理模式扫描

设置浏览器 http 代理为http://127.0.0.1:7777，然后使用浏览器访问网页，就可以自动分析代理流量并扫描。

```css
xray webscan --listen 127.0.0.1:7777 --html-output xxx.html
```



## 基础爬虫模式扫描

快速测试单个

```
xray webscan --url url --html-output xxx.html
```

 **使用基础爬虫爬取并对爬虫爬取的链接进行漏洞扫描**

```css
./x-ray webscan --basic-crawler http://url --html-output 输出.html
```



# rad 

radium



## 基本使用

```css
rad -t http://example.com
```

## 需要手动登录的情况

```cs
rad -t http://example.com -wait-login
```

将爬取的基本结果导出为文件

```
rad -t http://example.com -text-output result.txt
```

以上输出命令提取到的URL到`Method URL`result.txt：`GET http://example.com`

完成请求

```
rad -t http://example.com -full-text-output result.txt
```

导出完整请求为JSON

```
rad -t http://example.com -json result.json
```

与xray联动

社区版：设置上级代理为xray监听地址 运行xray：

```
xray webscan --listen 127.0.0.1:7777 --html-output proxy.html
```

运行角度：

```
rad -t http://example.com -http-proxy 127.0.0.1:7777
```

高级版对rad进行了深度融合，下载后可以一键使用：

```
xray webscan --browser-crawler http://example.com --html-output vuln.html
```





# AWVS联动

```
xray webscan --listen 127.0.0.1:7777 --html-output proxy.html
```

添加目标保存

设置代理

扫描
