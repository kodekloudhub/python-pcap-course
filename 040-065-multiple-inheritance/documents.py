# Create the Document class
class Document:
    # Add constructor

    # Add the path method

    def save(self, extention)
        self.path() + self.name + extention

    # Add the str method


class PDF:
    def __init__(self, name):
        self.name = name

    def path(self, path):
       return path

    # Override the save method


    # Override the str method


class TEXT:
    def __init__(self, name):
        self.name = name

    def path(self, path):
       return path

    # Override the save method


    # Override the str method



pdf = PDF(name="slides-show")
pdf.path("/home/pdf/")
text = PDF(name="slides-content")
txt.path("/home/txt/")

print(pdf, pdf.save())
print(txt, txt.save())
