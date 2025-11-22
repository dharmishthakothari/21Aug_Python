class Book:
    def __init__(self,title,author,isbn,price,qty):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.qty=qty
        self.price=price
    
    def displayBook(self):
        print(f"{self.title} - {self.author} - {self.isbn}")

    def calculatePrice(self):
        return self.price*self.qty

book1=Book("Who will cry when you die","Robin Sharma",23456,200,10)
book2=Book("Focus","Stephn",909090,120,12)

book1.displayBook()
book2.displayBook()
print(f"{book1.title} total_price is {book1.calculatePrice()}")