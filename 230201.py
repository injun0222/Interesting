'''
웹크롤링 공부
1. BeautifulSoup 모듈?
BeautifulSoup is a Python library used for web scraping and data extraction from HTML and XML files. It creates a parse tree from page source code that can be used to extract data in a hierarchical and more readable manner compared to using regular expressions. BeautifulSoup4 is the latest version of the library.

2. 사용법, 사용패턴
A common usage pattern of BeautifulSoup is as follows:

Import the library
Make a request to a website and get the HTML content
Pass the HTML content to BeautifulSoup to create a BeautifulSoup object
Use the BeautifulSoup object to extract data by searching for specific HTML tags, attributes, or text
Save or manipulate the extracted data as required

3. parser?
parse = 구문분석   -> parser = 구문분석자
"html.parser" in the argument of the BeautifulSoup constructor is the parser that the library will use to parse the HTML content. The parser is responsible for turning the raw HTML text into a parse tree that can be easily navigated and searched to extract data.

The "html.parser" argument specifies that BeautifulSoup should use the built-in HTML parser in Python's standard library. This parser is included in Python and does not require any additional installation.

Other parsers that can be used include:

"lxml": a fast and efficient parser that uses the lxml library
"lxml-xml": a parser that can handle both HTML and XML
"html5lib": a pure-Python parser that is lenient and can parse broken HTML
-> lxml 사용 가능할 때에는 lxml을 사용하자. 이게 가장 빠르다.


아래는 사용법에 따른 사용예제
'''
import requests
from bs4 import BeautifulSoup

# Make a request to a website
url = "https://www.example.com"
response = requests.get(url)

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the links on the page
links = soup.find_all("a")

# Print the href attribute of each link
for link in links:
    print(link.get("href"))
