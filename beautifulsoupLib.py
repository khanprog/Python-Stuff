import requests, bs4 


def getAmazonPrice(productUrl):
	
	res = requests.get(productUrl)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, "html.parser")
	element = soup.select('#mediaNoAccordion > div.a-row > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')

	price = element[0].text.strip()

	return price



price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')

print("The Price of Product is : " + price)