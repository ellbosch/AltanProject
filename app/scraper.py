from bs4 import BeautifulSoup
import requests

def scrape_me(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	title = soup.find('title')
	return title