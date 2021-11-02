class Book:
    def __init__(self, title):
        self.title = title
        self.author = None

    def add_author(self, name):
        # add author property
        ...

    def add_chapter(self, number, title):
        # add properties chapter_number and chapter_title
        ...



class BookInfo(Book):
    def __init__(self, title, price, info=False):
        Book.__init__(self, title)
        # add properties price and info
        ...
        ...
        self.stars = 0

    def rating(self, stars):
        try:
            # check if existing stars are less than new stars
            # and if new stars are greater than 4
            # adjust new price by a 20% increase
            ...
                ...
            # update the stars property
            ...
        except Exception as e:
            print(e, "Please try again")


# Create a book object titled 'Two Scoops of Django'
...
# Add the author 'Greenfeld'
...
# Add a chapter 3, with title 'Async Views'
...

# Create a book_info object titled 'Two Scoops of Django'
# with a price of 10, and info set to True
...
# Give the book_info a rating of 5 stars
...

print("Book info: ", end=" ")
# Print book_info's title, stars and price
print(
    ..., str(book_info.stars) + " stars",
    ..., sep=", "
)
# Print all properties of book and book_info objects
print("Book properties: ", ...)
print("BookInfo properties: ", ...)
