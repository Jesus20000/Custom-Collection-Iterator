# 📚 Custom Collection Iterator

This project demonstrates the **Iterator Design Pattern** in Python by building a digital archive system for managing a book collection. It separates the logic of storing books from the logic of traversing them using a custom iterator.

## 🛠️ Technologies Used

- Python 3.x  
- Object-Oriented Programming  
- Iterator Design Pattern

## 🧠 Design Pattern: Iterator

The **Iterator Pattern** provides a way to access elements of a collection sequentially without exposing the underlying structure. It supports clean iteration over complex objects such as a book collection.

## 📁 Project Structure

- `book.py` – Defines the Book class with title, author, and category  
- `book_iterator.py` – Implements the custom iterator logic  
- `book_collection.py` – Manages the list of books and returns the iterator  
- `main.py` – Demonstrates how to use the book collection and iterate through it  
- `README.md` – Project documentation (this file)

## 🚀 Features

- Add books to a custom collection  
- Iterate through books using a custom iterator  
- Clean, modular, and extensible object-oriented design  
- Easily adaptable for filtering and sorting

## 📌 Sample Output

```

Library Collection:
'1984' by George Orwell \[Dystopia]
'The Hobbit' by J.R.R. Tolkien \[Fantasy]
'Clean Code' by Robert C. Martin \[Programming]

````

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/custom-collection-iterator.git
cd custom-collection-iterator
````

2. Run the main script:

```bash
python main.py
```

