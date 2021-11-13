class Document:
    def __init__(self, name):
        self.name = name

    def path(self, path):
        return path

    def save(self, path, extention):
        return self.path(path) + self.name + extention

    def __str__(self):
        return "This is a Document"


class PDF(Document):
    def __init__(self, name):
        super().__init__(name)

    def save(self, path):
        return self.path(path) + self.name + ".pdf"

    def __str__(self):
        return "This is a PDF Document"


class TEXT(Document):
    def __init__(self, name):
        super().__init__(name)

    def save(self, path):
        return self.path() + self.name + ".txt"

    def __str__(self):
        return "This is a Text Document"


pdf = PDF(name="slides-show")
txt = PDF(name="slides-content")

print(txt, txt.save("/home/txt/"))
print(pdf, pdf.save("/home/pdf/"))
