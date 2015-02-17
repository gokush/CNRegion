#!/usr/bin/env python
#! -*- encoding:utf-8

import sys
import json
import fetch
import sqlite3
import pinyin
import argparse
import requests_cache

from pdb import set_trace as bp
from model import *
from fetch import *


args = None

class Printer:
    def __init__(self, dump):
        self.dump = dump

    def province(self, province):
        if "txt" == self.dump:
            return " ".join((str(province.id), province.name.encode("utf-8"),))

def main():
    global args
    parser = argparse.ArgumentParser(description='从国家统计局网站下载最新的行政区')
    parser.add_argument('input', const="", default="", type=str, nargs="?")
    parser.add_argument("--sqlite3", type=str, help='SQLite文件位置')
    parser.add_argument("--mysql", type=str, help='mysql dsn')
    parser.add_argument('--mysql-host', type=str, help='mysql host')
    parser.add_argument('--mysql-port', type=str, help='mysql port')
    parser.add_argument('--mysql-user', type=str, help='mysql user')
    parser.add_argument('--mysql-password', type=str, help='mysql password')
    parser.add_argument('--mysql-database', type=str, help='mysql database')
    parser.add_argument('--skip-province', type=int, help='跳过省份的第x个')
    parser.add_argument('--verbose', '-v', action='count', help='打印日志内容')
    parser.add_argument('--dump', action='store', default='txt', \
        help='输出内容的格式 csv txt xml json jsonp')
    parser.add_argument('--dump-children', action='store_true', \
        help='打印子级内容')
    parser.add_argument('--region-type', action='store', default='province', \
        help='')
    parser.add_argument('--requests-cache', action='store', \
        default='/tmp/cnregion_requests_cache.sqlite')

    args = parser.parse_args(sys.argv[1:])
    requests_cache.install_cache(args.requests_cache)
    fetch.VERBOSE_LEVEL = args.verbose

    printer = Printer(args.dump)

    if args.region_type == "city":
    for province in fetch_provinces():
        print printer.province(province)

if "__main__" == __name__:
    main()