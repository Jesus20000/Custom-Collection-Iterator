from book import Book
from book_collection import BookCollection

def main():
    collection = BookCollection()
    collection.add_book(Book("1984", "George Orwell", "Dystopia"))
    collection.add_book(Book("The Hobbit", "J.R.R. Tolkien", "Fantasy"))
    collection.add_book(Book("Clean Code", "Robert C. Martin", "Programming"))

    print("📚 Library Collection:")
    for book in collection:
        print(book)

if __name__ == "__main__":
    main()