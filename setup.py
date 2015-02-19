#!-*- encoding:utf-8 -*-
import codecs
from setuptools import setup


with codecs.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="cnregion",
    version="2.6.9",
    license='http://www.apache.org/licenses/LICENSE-2.0',
    description="这个脚本从中国统计局官方网站下载最新的中国行政区域的数据",
    author='goku',
    author_email='kakarrot.sh@qq.com',
    url='https://github.com/gokush/cnregion',
    packages=[''],
    package_data={
        'cnregion': ['README.md',]
    },
    install_requires=[],
    entry_points="""
    [console_scripts]
    cnregion = region_fetch:main
    """,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    long_description=long_description,
)