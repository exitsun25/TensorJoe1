from bs4 import BeautifulSoup
import requests

class Wiki:
    def __init__(self, url):
        base_url = url
        con = requests.get(base_url)
        soup = BeautifulSoup(con.content, '')
