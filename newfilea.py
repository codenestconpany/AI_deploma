from abc import ABC, abstractmethod


class Media(ABC):

    @abstractmethod
    def get_details(self):
        pass


class Book(Media):

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.__price = price

    def get_details(self):
        print("----- Book Details -----")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.__price}")

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be greater than zero")
class Magazine(Media):

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_details(self):
        print("----- Magazine Details -----")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
        
media_list = []

choice = input("Enter type (book/magazine): ")

title = input("Enter title: ")
author = input("Enter author: ")
price = float(input("Enter price: "))


if choice == "book":
    book = Book(title, author, price)
    media_list.append(book)

elif choice == "magazine":
    magazine = Magazine(title, author, price)
    media_list.append(magazine)
for i in media_list:
    i.get_details()                      