# coding: utf-8

import appex
import urllib.request
import os


def get_url(url):
  return urllib.request.urlopen(url)


def download_url(url, directory):
  os.makedirs(directory, mode=0o777, exist_ok=True)
  filename = url.split('/')[-1]
  path = directory + '/' + filename
  urllib.request.urlretrieve(url, path)
  return



def main():
  print('=================')
  url = 'https://twitter.com/dotHTM/status/967448762623897600'
  


def temp():
  if not appex.is_running_extension():
    print('this is meant to run as an extention')
  url_list = appex.get_urls()
  print(url_list)
  if url_list.count == 0:
    print('no urls to act on')
  for some_url in url_list:
    print(some_url)
    download_url(some_url, 'Downloads')


if __name__ == '__main__':
  main()

