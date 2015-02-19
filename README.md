CN Region
==========

这个脚本从[中国统计局](http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/index.html)官方网站
下载数据并保存到sqlite3数据库。

## 安装

```
$ pip install cnregion
```

## HTTP API

该项目提供一个公开的API，可以无需搭建自己的服务器。

format参数可以选择[json,jsonp]，如果选择jsonp，`/jsonp/provinces/?callback=call_provinces`有效。

### GET /{format}/provinces/

```
HTTP/1.1 200

[
    {
        "id": 11,
        "name": "北京"
]
```

###

## 使用

```
$ cnregion 

usage: region_fetch.py [-h] [--skip-province SKIP_PROVINCE] [--verbose]
                       sqlite3

从国家统计局网站下载最新的行政区

positional arguments:
  sqlite3               SQLite文件位置

optional arguments:
  -h, --help            show this help message and exit
  --skip-province SKIP_PROVINCE
                        跳过省份的第x个
  --verbose, -v         打印日志内容
```

## Dockerfile 开发环境

```
$ docker build .
Removing intermediate container bc39e330f294
Successfully built 2202867a5e91
$ docker run -t -i --rm -v /Users/goku/workspace/cnregion:/cnregion \
> 2202867a5e91 /bin/bash
root@5bb9c06986d7:/# python /cnregion/cli.py
```
