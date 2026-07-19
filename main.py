import json
import random
import string
from pathlib import Path
from datetime import datetime

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