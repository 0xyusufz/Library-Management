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
    

    def add_members(self):
        name = input("enter the name")
        email = input("enter the email")

        member = {
            "id" : self.generate_id("M"),
            "name": name,
            "email": email,
            "borowed": []
        }
        self.data["members"].append(member)
        Library.save_data()
    
    def list_members(self):
        if not self.data["members"]:
            print("Sorry no members found")
            return
        for i,j in enumerate(self.data["members"]):
            print(f"{i+1}. {j["id"]:25} {j["name"][:20]:25} {j["email"]:25} {j["borowed"]}")
    
    def borrow(self):
        self.list_members()
        member_id = input("enter the member id:- ").strip()
        for i in Library.data["members"]:
            if i["id"] == member_id:
                break
            else:
                print(f"no member found of id- {member_id}")
                return
        self.list_books()
        book_id = input("enter the book id:-").strip()
        for i in Library.data["books"]:
            if i["book_id"] == book_id:
                if i["available_copies"] == 0:
                    print("no copies available,sorry")
                    return
                elif i["available_copies"] > 0:
                    print(f"total copies avaible is {i["available_copies"]}")
                borrow_copies = int(input(f"enter a total book you want to borrow, ypu can borrow max {i["available_copies"]}"))
                if borrow_copies > i["available_copies"]:
                    print(f"you cant borrow {borrow_copies} copies , pls enter max {i["available_copies"]}:- ")
                else:
                    i["available_copies"] -= borrow_copies
                    for j in Library.data["members"]:
                        if j["id"] == member_id:
                            book_entry = {
                                "book_id": i["book_id"],
                                "book_name": i["book_name"],
                                "borrowed_copies": borrow_copies,
                                "borrow on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            }
                            j["borowed"].append(book_entry)
                            Library.save_data()
                            print(f"borrowed {borrow_copies} of book name {i["book_name"]}")
                            return
        print(f"no book found of id- {book_id} ")
    

    def return_book(self):
        self.list_members()
        member_id = input("enter the member id")
        for i in Library.data["members"]:
            if i["id"] == member_id:
                print(f"total book borrowed is {len(i["borowed"])}")
                for x,j in enumerate(i["borowed"]):
                    print(f"{x+1}. {j["book_id"]:25} name:- {j["book_name"]:25} borrowed copies:-{j["borrowed_copies"]}\t \t borrow on :- {j["borrow on"][:11]:25}")
                book_id = input("enter a book id to return")
                for k in i["borowed"]:
                    if k["book_id"] == book_id:
                        print(f"total copies available is {k["borrowed_copies"]}")
                        return_copy = int(input("how much you want to return?"))
                        if return_copy >0 and return_copy <= k["borrowed_copies"]:
                            for l in Library.data["books"]:
                                if l["book_id"] == book_id:
                                    l["available_copies"] += return_copy
                            if return_copy == k["borrowed_copies"]:
                                i["borowed"].remove(k)
                                self.save_data()
                                return
                            else:
                                k["borrowed_copies"] -= return_copy
                                self.save_data()
                                return
                        else:
                            print("enter a valid number")
                    else:
                        print("book not found")
            else:
                print("no member found")
        
























hello = Library()





while True:
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
    elif choice == 3:
        hello.add_members()
    elif choice == 4:
        hello.list_members()
    elif choice == 5:
        hello.borrow()
    elif choice == 6:
        hello.return_book()
    elif choice == 0:
        break