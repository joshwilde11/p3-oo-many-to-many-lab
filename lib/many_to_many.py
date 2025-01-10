class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        Author.all_authors.append(self)

    def contracts(self):
        related_contracts = []
        for contract in Contract.all_contracts:
            if contract.author == self:
                related_contracts.append(contract)
        return related_contracts

    def books(self):
        related_books = []
        for contract in self.contracts():
            related_books.append(contract.book)
        return related_books

    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total

class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        related_contracts = []
        for contract in Contract.all_contracts:
            if contract.book == self:
                related_contracts.append(contract)
        return related_contracts

    def authors(self):
        related_authors = []
        for contract in self.contracts():
            related_authors.append(contract.author)
        return related_authors

class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @property
    def author(self):
        return self._author

    @property
    def book(self):
        return self._book

    @property
    def date(self):
        return self._date

    @property
    def royalties(self):
        return self._royalties

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author")
        self._author = value

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book")
        self._book = value

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        self._date = value

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("royalties must be a number")
        self._royalties = value

    def get_date(self):
        return self.date

    @classmethod
    def contracts_by_date(cls, date):
        related_contracts = []
        for contract in cls.all_contracts:
            if contract.date == date:
                related_contracts.append(contract)
        return related_contracts