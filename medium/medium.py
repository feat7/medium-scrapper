#!/usr/bin/python3

from selenium import webdriver
from bs4 import BeautifulSoup
import bleach
import sqlite3
import os.path

def main():

	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	db_path = os.path.join(BASE_DIR, "data.db")

	db = sqlite3.connect(db_path)
	print("Connected to database successfully.")


	url = input('Enter url of medium post: ')


	driver = webdriver.Chrome()

	driver.get(url)

	content_element = driver.find_element_by_class_name("postArticle--full")
	content_html = content_element.get_attribute("innerHTML")

	soup = BeautifulSoup(content_html, 'html.parser')

	author = soup.find('div', {"class":"u-flex1"}).find('a')

	title = soup.find('h1', { "class":"graf--title" })
	subtitle = soup.find('h2', {"class":"graf--subtitle"})


	p_tags = soup.find_all('p')

	content = ''

	for p in p_tags:
		content += bleach.clean(p, tags=['a', 'img'], strip=True)

	title = title.text or 'none'

	try:
		subtitle = subtitle.text or 'none'
	except AttributeError:
		subtitle = ''

	try:
		author = author.text or 'none'
	except AttributeError:
		author = ''

	db.execute("INSERT INTO `medium_posts` (title,subtitle,author,post) VALUES (?, ?, ?, ? )",
		(title, subtitle, author, content))

	db.commit()
	print("Post ", title, " successfully added to database!")

	db.close()

	driver.close()


if __name__ == '__main__' : main()
