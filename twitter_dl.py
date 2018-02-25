# coding: utf-8

import appex
import urllib.request
import os
import re
import urllib3
import photos

urllib3.disable_warnings()


def get_url(url):
  return urllib.request.urlopen(url)


def download_url(url, directory):
  os.makedirs(directory, mode=0o777, exist_ok=True)
  filename = url.split('/')[-1]
  path = directory + '/' + filename
  urllib.request.urlretrieve(url, path)
  return


def check_for_album_or_make(album_name):
  all_albums = photos.get_albums()
  found = False
  for some_album in all_albums:
    if found:
      continue
    elif some_album.title == album_name:
      found = True
      found_album = some_album
  if not found:
    found_album = photos.create_album(album_name)
  return found_album


def save_photos_url(url, directory):
  os.makedirs('tmp', mode=0o777, exist_ok=True)
  some_album = check_for_album_or_make(directory)
  filename = url.split('/')[-1]
  path = 'tmp/' + filename
  urllib.request.urlretrieve(url, path)
  saved_asset = photos.create_image_asset(path)
  saved_asset.location = {
    'latitude': 45.0,
    'longitude': -135.0,
    'altitude': 10.0
  }
  some_album.add_assets([saved_asset])
  return


def read_url(url):
  http = urllib3.PoolManager()
  r = http.request('GET', url)
  return r.data


def find_links(input_string):
  urlRegex = 'https?://[^"\'\\\\\s\n\r:]+'
  array = re.findall(urlRegex, str(input_string))
  link_hash = {}
  for i in array:
    if i in link_hash:
      link_hash[i] += 1
    else:
      link_hash[i] = 1
  return link_hash


def filter_images(link_hash):
  image_types = {'.jpg', '.jpeg', '.png', '.svg', '.tiff', '.gif'}
  found_images = {}
  if link_hash:
    for some_link in link_hash.keys():
      for some_type in image_types:
        if some_type in some_link:
          found_images[some_link] = 1
  return found_images.keys()


def filter_str_list(filter_string, string_list):
  pass_list = {}
  for line in string_list:
    if filter_string in line:
      pass_list[line] = 1
  return pass_list.keys()


def twitter_images(url):
  url = re.sub(r'(.*?)\?.*', r'\1', url)
  print("--- start images: " + url + " ---")
  if "mobile.twitter" in url:
    url = re.sub(r'(.*?)mobile\.twitter(.*?)', r'\1www.twitter\2', url)
  user = re.sub(r'.*?twitter.com/(\w*)/.*', r'\1', url)
  status = re.sub(r'.*?twitter.com/\w*/status/(\d*)', r'\1', url)
  doc = read_url(url)
  links = find_links(doc)
  images = filter_images(links)
  targets = filter_str_list('/media/', images)
  for i in targets:
    save_photos_url(i, user + ' - ' + status)
  print("--- start images: " + url + " ---")


def main():
  if not appex.is_running_extension():
    print('this is meant to run as an extention')
  url_list = appex.get_urls()
  if url_list.count == 0:
    print('no urls to act on')
  else:
    for some_url in url_list:
      if '/status/' in some_url:
        twitter_images(some_url)
    print(">>> ALL DONE <<<")


if __name__ == '__main__':
  main()

