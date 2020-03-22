#!/usr/bin/python

import datetime;  # This is required to include time module

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = float(price) # convert the price into a float

    def get_price(self, currency):
        exchange_rates = {
            'usd': 1.0,
            'eur': 0.93,
            'gbp': 0.86,
            'ghc': 55621.99
        }
        rate = exchange_rates[currency]
        return self.price * rate

current_datetime = datetime.datetime.now()
current_hour = current_datetime.hour

with open('books.csv') as f: # open a file
    lines = f.readlines() # read the lines of the file into an array

current_line = 0; 
for line in lines: # loop through the array containing the lines of the file
    if current_line == 0:
        current_line = 1
        continue # ignore the first line of the file

    title, author, price = line.split(',') # read the values from the line
    book = Book(title, author, price) # create an object to represent the book

    print('------')
    print(current_line)
    print('Title: ' + book.title)
    print('Author: ' + book.author)

    price_usd = str(book.price)
    price_eur = '%.2f' % book.get_price('eur')
    price_gbp = '%.2f' % book.get_price('gbp')
    print('Price USD: ' + price_usd)
    print('Price: EUR: ' + price_eur)
    print('Price: GBP: ' + price_gbp)

    current_line = current_line + 1
