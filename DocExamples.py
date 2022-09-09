from bs4 import BeautifulSoup
import requests

# Find and Find All Examples
print('Find Examples:')

url = "http://quotes.toscrape.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# First Heading(h1) Text

print(soup.find('h1').text)
print()

# returns the text from the anchor tag with class `tag`

print(soup.find('a', {'class': 'tag'}).text)
print()

# returns the first div tag with the class `tags`

print(soup.find('div', {'class': 'tags'}))
print()

print('Find All Examples:')

# Return all the h1 tags in a list

print(soup.find_all('h1'))
print()

# Return all the div with the class tags in a list

print(soup.find_all('div', {'class': 'tags'}))
print()

# Print out all the tags in the web page

tags = soup.find_all(class_="tags")
lst = []
for tag in tags:
    lst.append(tag.text.replace("\n", " ").strip())
    lst2 = [tag.replace("  ", "") for tag in lst]
print(lst2)
print()

# Select Example

print('Select Examples:')

# Initialize soup object through get request

url = "https://webscraper.io/test-sites/e-commerce/allinone"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# Return all p tags in list format

print(soup.select('p'))
print()

# Return the text from all the divs with the class title

print(soup.select('.title'))
print()

# Price Scraping Example

name = soup.select(".title")

for i in range(0, len(name)):
    price = soup.select(".price")[i].text
    name = soup.select(".title")[i].get_text()
    description = soup.select(".description")[i].get_text()
    print(name)
    print(description)
    print(price, end="\n\n")
print()

# Link Examples

url = "https://webscraper.io/test-sites/e-commerce/allinone"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

print('Link Examples:')

# Scrape all links from webpage

for a_tag in soup.findAll("a"):
    href = a_tag.attrs.get("href")
    if href != "":
        print(href)
print()

# Scrape links from a particular selector

div = soup.find('div', {'class': 'col-sm-4 col-lg-4 col-md-4'})
a = div.find('a')
link = a.attrs.get("href")
print(link)
print()
