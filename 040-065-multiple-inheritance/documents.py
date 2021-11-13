# Create the Document class
class Document:
    # Add constructor

    # Add a path method, which returns the path

    def save(self, path, extention)
        return self.path() + self.name + extention

    # Add the str method that returns
    def __str__(self):
        return "This is a Document"


class PDF:
    def __init__(self, name):
        # complete the constructor

    # Override the save method


    # Override the str method


class TEXT:
    def __init__(self, name):
        # complete the constructor


    # Override the save method


    # Override the str method



pdf = PDF(name="slides-show")
txt = PDF(name="slides-content")

print(txt, txt.save("/home/txt/"))
print(pdf, pdf.save("/home/pdf/"))
