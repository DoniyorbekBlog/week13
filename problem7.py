import requests

url = 'https://openlibrary.org/search.json'

search_subject = 'python'

params = {
    'q': search_subject,
    'limit': 1000,
    'fields': 'title,author_name,first_publish_year,number_of_pages_median'
}

response = requests.get(url, params)

import pprint
import datetime

current_date = datetime.date.today()
print(current_date)
current_year = current_date.year
print(current_year)

thickest_book_page_count = 0
thickest_book_title = None

oldest_book_year = current_year
oldest_book_title = None

if response.status_code == 200:
    data = response.json()
    pprint.pprint(data)
    for book in data['docs']:
        if 'number_of_pages_median' not in book \
            or 'first_publish_year' not in book:
            continue
        num_of_pages = book['number_of_pages_median']
        first_publish_year = book['first_publish_year']
        title = book['title']
        if num_of_pages > thickest_book_page_count:
            thickest_book_page_count = num_of_pages
            thickest_book_title = title
        if first_publish_year < oldest_book_year:
            oldest_book_year = first_publish_year
            oldest_book_title = title
        
        print(title, first_publish_year, num_of_pages)
    print('---------')
    print(oldest_book_title, oldest_book_year)
    print(thickest_book_title, thickest_book_page_count)