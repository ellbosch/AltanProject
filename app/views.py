from app import application, scraper
from flask import render_template, url_for

@application.route('/')
def home_page():
	return render_template('index.html')

@application.route('/scrape/<company>', methods=['GET'])
@application.route('/scrape')			# flask allows multiple urls to the same route!
def scrape_website(company=None):
	title = ""
	if company != None:

		company_url = "http://%s.com" % company
		title = scraper.scrape_me(company_url)
		print(title)

	return render_template('scraper.html', website_title=title)