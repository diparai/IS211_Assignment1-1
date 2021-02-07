
class Book(object):
    author = ''
    title = ''

    def __init(self, author, title):
        self.author = author
        self.title = title

    
    def display(self):
        input('Enter the title number: ')
        author1 = 'John Steinbeck'
        author2 = 'Harper Lee'
        Title1 = 'Of Mice and Men'
        Title2 = 'To kill a Mockingbird'
        output = Title1 + ' written by ' + author1
        output = Title2 + ' written by ' + author2

        result = output.format(self.title, self.author)
        return result

Title1 = Book()
Title2 = Book()

print(Title1.display())
print(Title2.display())

