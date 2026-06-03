import cloudscraper

scraper = cloudscraper.create_scraper()
r = scraper.get('https://soufeel.com')
print(r.status_code)
print(r.text)
