class Book:
    
    def __init__(self, id, title, author, category, is_borrowed = False, borrowed_by = "", borrowed_date = None):
        self.id = id
        self.title = title
        self.author = author
        self.category = category
        self.is_borrowed = is_borrowed
        self.borrowed_by = borrowed_by
        self.borrowed_date = borrowed_date

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'category': self.category,
            'is_borrowed': self.is_borrowed,
            'borrowed_by': self.borrowed_by,
            'borrowed_date': self.borrowed_date,
            }

    @staticmethod
    def toConstruct(data):
        return Book(
            data['id'],
            data['title'],
            data['author'],
            data['category'],
            data['is_borrowed'],
            data['borrowed_by'],
            data['borrowed_date']
        )