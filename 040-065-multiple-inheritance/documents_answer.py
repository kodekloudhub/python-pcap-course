class Document:
    def __init__(self, name):
        self.name = name

    def path(self, path):
        return path

    def save(self, extention):
        self.path() + self.name + extention

    def __str__(self):
        return "This is a Document"


class PDF(Document):
    def save(self):
        self.path() + self.name + ".pdf"

    def __str__(self):
        return "This is a PDF Document"


class TEXT(Document):
    def save(self):
        self.path() + self.name + ".txt"

    def __str__(self):
        return "This is a Text Document"


pdf = PDF(name="slides-show")
txt = TEXT(name="slides-content")

print(pdf)
print(txt)
