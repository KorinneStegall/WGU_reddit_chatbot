# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:53:06 2023

@author: korin
"""

import gzip
from io import StringIO


def compressFileToString(inputFile):
  """
  read the given open file, compress the data and return it as string.
  """
  stream = StringIO.StringIO('index.json')
  compressor = gzip.GzipFile(fileobj=stream, mode='w')
  while True:  # until EOF
    chunk = inputFile.read(8192)
    if not chunk:  # EOF?
      compressor.close()
      return stream.getvalue()
    compressor.write(chunk)