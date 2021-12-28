# The information for abstract classes: https://www.youtube.com/watch?v=UDmJGvM-OUw

'''
Las abstract classes estan normalmente en las superclases, son solo declaradas,
siempre van seguidos de "pass", lo que esperan es utilizarlas dentro de las subclasses
y decir lo que hacen en ellas, basicamente, sabemos en la superclase,
que existira ese metodo para esa clase "global", pero de diferentes maneras
en las subclases, superclase = Computer, subclases = Laptop, Mobile, Tablet,

La super clase tiene una función que enseña algo.

Las subclases vuelven a escribir esta función, pero explicando que se hace en
cada una de ellas, porque la manera de enseñar algo cambia en las diferentes
subclases
'''


from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price
    def display(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Price: {}".format(self.price))
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()