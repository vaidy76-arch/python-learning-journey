# Day 8 Practice: Book Class

class Book:
    """
    A class to represent a book
    
    Attributes:
        title (str): Book title
        author (str): Book author
        pages (int): Number of pages
        current_page (int): Current reading position
    """
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page=0        
    
    def read(self, pages):
        """
        Read a certain number of pages
        - Can't read more pages than remaining
        - Can't read negative pages
        """
        self.remaining_pages= self.pages-self.current_page
        if self.remaining_pages<pages:
            print (f"Can't read - only {self.remaining_pages} left")
        else:
            self.current_page += pages
        

        
    
    def progress(self):
        """
        Return reading progress as percentage
        """
        return 100 * (self.current_page/self.pages)
        
    
    def __str__(self):
        """
        Return string representation
        Format: "Title by Author (current_page/total_pages)"
        """
        return f"{self.title} by {self.author}({self.current_page}/{self.pages})"


# Test your Book class
book1 = Book("Python Mastery", "John Doe", 300)
print(book1)  # Should show: Python Mastery by John Doe (0/300)

book1.read(50)
print(f"Progress: {book1.progress()}%")  # Should show: 16.67%

book1.read(100)
print(book1)  # Should show current page 150

book1.read(200)  # Should give error - can't read more than 150 remaining