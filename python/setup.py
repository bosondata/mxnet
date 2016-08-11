# pylint: disable=invalid-name, exec-used
"""Setup mxnet package."""
from __future__ import absolute_import
import os.path
import subprocess
from setuptools import setup, Extension


subprocess.Popen("make -j$(nproc)",
                 stdin=subprocess.PIPE,
                 stderr=subprocess.PIPE,
                 stdout=subprocess.PIPE,
                 shell=True).communicate()
# We can not import `mxnet.info.py` in setup.py directly since mxnet/__init__.py
# Will be invoked which introduces dependences
LIB_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'mxnet/lib')
__version__ = '0.7.0'


setup(name='mxnet',
      version=__version__,
      description=open('README.md').read(),
      install_requires=[
          'numpy',
      ],
      zip_safe=False,
      packages=['mxnet', 'mxnet.module'],
      package_data={'mxnet': ['lib/libmxnet.so', 'lib/libmxnet-centos.so', 'lib/libmxnet-ubuntu.so']},
      url='https://github.com/dmlc/mxnet')
