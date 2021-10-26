#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages
from lineplot.version import get_version

setup(
    name='lineplot-r',
    version=get_version(),
    description='An biovis plugin to draw an interactive line plot.',
    long_description='The line plot plugin will draw an interactive line plot by using ggplot2 library.',
    keywords='biovis-plugin, line-plot, interactive',
    url='https://github.com/biovis-report/lineplot-r',
    author='Jingcheng Yang',
    author_email='yjcyxky@163.com',
    license='MIT',
    python_requires='>=3.5',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'biovis.plugins': [
            'lineplot-r = lineplot.lineplot:LinePlotRPlugin'
        ]
    }
)
