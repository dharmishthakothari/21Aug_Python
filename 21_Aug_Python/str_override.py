class Book:
    def __init__(self,title,author,isbn,price,qty):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.qty=qty
        self.price=price
    def __str__(self):
        return f"{self.title} - {self.author} - {self.isbn}"
    # def displayBook(self):
    #     print(f"{self.title} - {self.author} - {self.isbn}")
b=Book('ttt','tttt',22323,23,2)
print(b)
