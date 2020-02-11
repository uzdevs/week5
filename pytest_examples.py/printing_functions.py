def print_books(unprinted_books, completed_books):
    """
    Simulate printing each books until none are left.
    Move each books to complated_books afte printing.
    """
    while unprinted_books:
        current_books = unprinted_books.pop()
        print("Printing current book: " + current_books.title())
        completed_books.append(current_books)

def show_completed_books(completed_books):
    """Show all completed_books that we printed."""
    print("\nThe following books have been printed.")
    for completed_book in completed_books:
        print(completed_book)

