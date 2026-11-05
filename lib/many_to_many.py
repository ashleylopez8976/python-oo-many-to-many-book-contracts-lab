class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [
            contract for contract in Contract.all
            if contract.author is self
        ]

    def books(self):
        # Include each related book only once.
        return list(dict.fromkeys(
            contract.book for contract in self.contracts()
        ))

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [
            contract for contract in Contract.all
            if contract.book is self
        ]

    def authors(self):
        # Include each related author only once.
        return list(dict.fromkeys(
            contract.author for contract in self.contracts()
        ))


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Store the contract only after all values pass validation.
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError("author must be an Author instance")
        self._author = author

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise TypeError("book must be a Book instance")
        self._book = book

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        self._date = date

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        if type(royalties) is not int:
            raise TypeError("royalties must be an integer")
        self._royalties = royalties

    @classmethod
    def contracts_by_date(cls, date):
        return [
            contract for contract in cls.all
            if contract.date == date
        ]