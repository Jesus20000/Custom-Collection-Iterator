```markdown
# 📚 Custom Collection Iterator (Python)

This project demonstrates the **Iterator Design Pattern** by building a digital archive system for managing a book collection. It allows you to create and traverse a custom collection of books using your own iterator.

## 🔧 Technologies Used

- Python 3.x  
- Object-Oriented Programming  
- Iterator Design Pattern

## 🧠 Design Pattern: Iterator

The Iterator pattern allows sequential access to elements in a collection without exposing the underlying representation. This project separates the logic of storing books (`BookCollection`) from the logic of traversing them (`BookIterator`).

## 🗂️ Project Structure

```

custom-collection-iterator/
├── book.py              # Book class
├── book\_iterator.py     # Custom iterator for books
├── book\_collection.py   # Manages list of books
├── main.py              # Client script to demonstrate usage
├── README.md            # This file

```

## 🚀 Features

- Define books with title, author, and category  
- Add books to a custom collection  
- Iterate through the collection using a custom iterator  
- Easily extendable for filters (e.g., by author, year, category)

## 📌 Example Output

```

Library Collection:
'1984' by George Orwell \[Dystopia]
'The Hobbit' by J.R.R. Tolkien \[Fantasy]
'Clean Code' by Robert C. Martin \[Programming]

````

## 📦 How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/custom-collection-iterator.git
cd custom-collection-iterator
````

2. Run the program:

```bash
python main.py
```

## ✨ Possible Extensions

* Add filtering iterators (e.g., by category or author)
* Add sorting before iteration (alphabetical, by year, etc.)
* Implement reverse iteration
* Add pagination for large collections
