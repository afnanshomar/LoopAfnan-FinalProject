class library:
    def __init__(self,list_of_clients,list_of_librarians,list_of_books,list_of_borrowed_orders):
        self.clients=list_of_clients
        self.librarian=list_of_librarians
        self.book=list_of_books
        self.borrowing_order=list_of_borrowed_orders
      def valiablebook(self):
         print("the books avaliable now are :")
         for book in self.book :
             print("book is"+book)
      def borrowedbook(self,bookName):
          if bookName in self.borrowing_order:
              self.book.remove(bookName)
              print("please return book in 30 days")
              return True
          else:
              print("you borrowed a {bookName}")
              return False
      def returnbook(self,bookName):
          self.book.append(bookName)
          print("thanks for returning book")
class client:
    def requestbook(self):
        self.book=input("enter the name of the book you want to borrow")
        return self.book
    def returnbook(self):
        self.book=input("enter the name of book you want to return")
        return self.book
if __name__ =="__main__":
    mainlibrary=library["python","java","data","statistics"]
    client=client()
class client:
    def __init__(self,id,full_name,age,id_no,phone_number):
       self.id=id
       self.full_name=full_name
       self.age=age
       self.id_no=id_no
       self.phone_number=phone_number


class librarian(client):
    def __init_(self, emplyment_type):
        super(librarian).__init_subclass__(emplyment_type)
class book:
    def __int__(self,id,title,description,author,status):
     self.id=id
     self.title=title
     self.description=description
     self.author=author
     self.status=status
class borrowing_order:
    def __int__(self,id,date,client_id,book_id,status):
        self.__class__client=client_id
        self.__class__book=book_id
