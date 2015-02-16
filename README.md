CN Region
==========

这个脚本从[http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/index.html](中国统计局) 官方网站
下载数据并保存到sqlite3数据库。

## 安装

```
$ pip install cnregion
```

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