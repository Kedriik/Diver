import requests
import urllib.request
import time
import numpy as np
from PIL import Image
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self):
        
class Node:
    def __init__(self):
        self.node_score = 0

class Tree:
    def ___init___(self, node):
        self.root = node
    
class Page:
    def __init___(self):
        self.images =[]
        self.links  = []
        self.info   = []
url      = "http://www.google.com"
response = requests.get(url)

start_page = BeautifulSoup(response.text, "html.parser")
links = []
page_links = start_page.findAll('a')
for i in range(len(page_links)):
    links.append(page_links[i]['href'])
print(links)
