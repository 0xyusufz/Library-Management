import json
import random
import string
from pathlib import Path
from datetime import datetime


class Library:

    database = "library.json"
    p = Path(database)
    data = {"books":[],"members":[]}

    # load exisiting data to json or create your json
    if p.exists():
        with open(database,"r") as f:
            content = f.read().strip()
            if content:
                data = json.loads(content)
    else:
        with open(database,"w") as f:
            json.dump(data,f,indent=4)




    @staticmethod
    def generate_id(Prefix ="B"):
        random_id = ""
        for i in range(5):
            random_id += random.choice(string.ascii_uppercase + string.digits)
        return f"{Prefix}-{random_id}"
    @classmethod
    def save_data(cls):
        with open(cls.database,"w") as f:
            json.dump(cls.data,f,indent=4,default= str)
    # ADDING A NEW BOOKS
    # instance method
    def add_book(self):
        book = input("enter your book name")
        author = input("enter a author name")
        copies = int(input("enter total number of copies"))
        book ={
            "book_id": self.generate_id(),
            "book_name": book,
            "author_name": author,
            "total_copies": copies,
            "available_copies": copies,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.data["books"].append(book)
        Library.save_data()

    def list_books(self):
        if not Library.data["books"]:
            print("Sorry no books found")
            return
        for i,j in enumerate(Library.data["books"]):
            print(f"{i+1}. {j["book_id"]:25} {j["book_name"][:20]:25} {j["author_name"][:20]:25} {j["available_copies"]}/{j["total_copies"]:>3}")




















hello = Library()






print("="*50)
print("Library Management System")
print("="*50)
print("1. Add Book")
print("2. List Books")
print("3. Add Members")
print("4. List Members")
print("5. Borrow Books")
print("6. Return Books")
print("0. Exit the Portal")
print("-"*50)
choice = int(input("What Task you want to perform:- "))


if choice == 1:
    hello.add_book()
elif choice == 2:
    hello.list_books()