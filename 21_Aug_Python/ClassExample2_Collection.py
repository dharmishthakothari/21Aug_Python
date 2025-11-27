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

def searchBook(authur_name,lstBook):
    for i in lstBook:
        if i.author==authur_name:
            i.displayBook()


book1=Book("Who will cry when you die","Robin Sharma",23456,200,10)
book2=Book("Focus","Stephn",909090,120,12)
book3=Book("Python","Robin Sharma",23456,200,10)
book4=Book("Proramming in c ","Stephn",909090,120,12)

lst_books=[book1,book2,book3,book4,Book("Django","Ste",23232323,230,23)]
searchBook(authur_name='Robin Sharma',lstBook=lst_books)
