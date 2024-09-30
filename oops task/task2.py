

class Book():

    def __init__(self,title,author,yop):
        self.title=title
        self.author=author
        self.yop=yop
    def getBookInfo(self):
        print(f"Title:{self.title},Author:{self.author},Year of Publishing{self.yop}")

book=Book(author=input("Enter the author name"),title=input("Enter the Title"),yop=int(input("Enter theyear of publishing")))
book.getBookInfo() 