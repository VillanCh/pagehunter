#!/usr/bin/env python3
# coding:utf-8
import subprocess
from setuptools import setup, find_packages


def get_git_revision_short_hash():
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])


setup(
    name='pagehunter',
    # See https://www.python.org/dev/peps/pep-0440/
    version="1.{}".format(get_git_revision_short_hash()),
    description='PageHunter - Web 页面的相似度处理 from sqlmap',
    author='v1ll4n',
    author_email='v1ll4n@qq.com',
    url='http://pagehunter.com',
    install_requires=[],
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
)
