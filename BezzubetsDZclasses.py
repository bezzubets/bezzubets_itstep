# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, произво-
# дителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реа-
# лизуйте доступ к отдельным полям через методы класса.

# class cars:
#     print('Представление автомобиля:')
#     def __init__(self):
#         self.model=''
#         self.year=0
#         self.color=''
#         self.factory=''
#         self.price=0
#     def input(self):
#         self.model=input('Введите название модели: ')
#         self.year=int(input('Введите год выпуска: '))
#         self.color=input('Введите цвет автомобиля: ')
#         self.factory=input('Введите завод-производитель: ')
#         self.price=int(input('Введите стоимость автомобиля: '))
#     def set_model(self,model):
#         self.model = model
#     def set_year(self,year):
#         self.year=year
#     def set_color(self,color):
#         self.color=color
#     def set_factory(self,factory):
#         self.factory=factory
#     def set_price(self,price):
#         self.price=price
#     def get_model(self):
#         return self.model
#     def get_year(self):
#         return self.year
#     def get_color(self):
#         return self.color
#     def get_factory(self):
#         return self.factory
#     def get_price(self):
#         return self.price
#     def show(self):
#         print(self.model)
#         print(self.year)
#         print(self.color)
#         print(self.factory)
#         print(self.price)
#
# car=cars()
# car1=cars
# car2=cars()
# car.model='Ford'
# car.year=2017
# car.color='White'
# car.factory='Koeln, Germany'
# car.price=15000
# car.show()
# print('Представление вашего автомобиля:')
# car2.input()
# car2.show()
# print('Представление автомобиля Toyota:')
# car1.set_model(car1,model="Toyota")
# car1.set_year(car1,year=2000)
# car1.set_color(car1,color='Black')
# car1.set_factory(car1,factory='Japan')
# car1.set_price(car1,price=14000)
# car1.show(car1)
# print('Получаем информацию об автомобиле:')
# car2.get_model()
# car2.get_year()
# print('Название автомобиля: ',car2.model,'Год выпуска: ',car2.year)

# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

# class books:
#     print('Информация о книге: ')
#     def __init__(self):
#         self.name=''
#         self.year=0
#         self.publisher=''
#         self.genre=''
#         self.author=''
#         self.price=0
#     def input(self):
#         self.name=input('Введите название книги: ')
#         self.year=int(input('Введите год выпуска: '))
#         self.publisher=input('Издатель: ')
#         self.genre=input('Жанр книги: ')
#         self.author=input('Автор книги: ')
#         self.price = int(input('Стоимость книги: '))
#     def set_name(self,name):
#         self.name = name
#     def set_year(self,year):
#         self.year=year
#     def set_publisher(self,publisher):
#         self.publisher=publisher
#     def set_genre(self,genre):
#         self.genre=genre
#     def set_author(self,author):
#         self.author=author
#     def set_price(self, price):
#         self.price = price
#     def get_name(self):
#         return self.name
#     def get_year(self):
#         return self.year
#     def get_publisher(self):
#         return self.publisher
#     def get_genre(self):
#         return self.genre
#     def get_author(self):
#         return self.author
#     def get_price(self):
#         return self.price
#     def show(self):
#         print(self.name)
#         print(self.year)
#         print(self.publisher)
#         print(self.genre)
#         print(self.author)
#         print(self.price)
#
# book=books()
# book1=books
# book2=books()
# book.name='Золотой теленок'
# book.year=1988
# book.publisher='Современная литература'
# book.genre='Юмор. Сатира.'
# book.author='И.Ильф, Евг.Петров.'
# book.price=60
# book.show()
# print('Введите информацию о книге:')
# book2.input()
# book2.show()
# print('Загружаем информацию о книге:')
# book1.set_name(book1,name='12 стульев')
# book1.set_year(book1,year=1988)
# book1.set_publisher(book1,publisher='Современная литература')
# book1.set_genre(book1,genre='Юмор. Сатира.')
# book1.set_author(book1,author='И.Ильф, Евг.Петров.')
# book1.set_price(book1,price=60)
# book1.show(book1)
# print('Получаем информацию о книге:')
# book1.get_name(book1)
# book1.get_author(book1)
# print('Название книги: ',book1.name,'Автор: ',book1.author)

# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

# class stadiums:
#     print('Информация о стадионе: ')
#     def __init__(self):
#         self.name=''
#         self.year=0
#         self.country=''
#         self.city=''
#         self.capacity=0
#     def input(self):
#         self.name=input('Введите название стадиона: ')
#         self.year=int(input('Введите год открытия: '))
#         self.country=input('Страна местонахождения: ')
#         self.city=input('Город: ')
#         self.capacity=int(input('Вместимость стадиона: '))
#     def set_name(self,name):
#         self.name = name
#     def set_year(self,year):
#         self.year=year
#     def set_country(self,country):
#         self.country=country
#     def set_city(self,city):
#         self.city=city
#     def set_capacity(self,capacity):
#         self.capacity=capacity
#     def get_name(self):
#         return self.name
#     def get_year(self):
#         return self.year
#     def get_country(self):
#         return self.country
#     def get_city(self):
#         return self.city
#     def get_capacity(self):
#         return self.capacity
#     def show(self):
#         print(self.name)
#         print(self.year)
#         print(self.country)
#         print(self.city)
#         print(self.capacity)
#
# stadium=stadiums()
# stadium1=stadiums
# stadium2=stadiums()
# stadium.name='Металлист'
# stadium.year=1925
# stadium.country='Украина'
# stadium.city='Харьков'
# stadium.capacity=38000
# stadium.show()
# print('Введите информацию о стадионе:')
# stadium2.input()
# stadium2.show()
# print('Загружаем информацию о Стадионе:')
# stadium1.set_name(stadium1,name='Динамо')
# stadium1.set_year(stadium1,year=1953)
# stadium1.set_country(stadium1,country='Украина')
# stadium1.set_city(stadium1,city='Харьков')
# stadium1.set_capacity(stadium1,capacity=4500)
# stadium1.show(stadium1)
# print('Получаем информацию о стадионах:')
# stadium.get_name()
# stadium1.get_name(stadium1)
# stadium2.get_name()
# print(stadium.name,stadium1.name,stadium2.name)