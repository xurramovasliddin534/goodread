# from django.db import models

# from django.contrib.auth.models import User

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     isbn = models.CharField(max_length=17)

# def __str__(self):
#         return self.title 
# # nomini chiqarish

# class Author(models.Model):
#       first_name = models.CharField(max_length=200)
#       last_name = models.CharField(max_length=200)
#       email = models.EmailField()
#       bio = models.TextField()
      
#       def __str__(self):
#             return f'{self.first_name} {self.last_name}'
# class BookAuthor(models.Model):
#       book = models.ForeignKey(book, on_delete=models.CASCADE)   
#       author = models.ForeignKey(author, on_delete=models.CASCADE)

#       def __str__(self):
#             f"{self.book.title} by {self.author.first_name} {self.author.last_name}"


# class BookReview(models.Model):
#       user = models.ForeignKey(User, on_delete=models.CASCADE)
#       book = models.ForeignKey(book, on_delete=models.CASCADE)
#       commit = models.TextField()
#       stars_given =models.ImageField()

#       def __str__(self):
#             return f"{self.stars_given} star for {self.book.title} by {self.user.username}"
from django.db import models

from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    isbn = models.CharField(max_length=17)
    
    def __str__(self):
        return self.title 

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    bio = models.TextField()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)   # TO'G'RILANDI: book → Book
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # TO'G'RILANDI: author → Author
    
    def __str__(self):
        return f"{self.book.title} by {self.author.first_name} {self.author.last_name}"  # TO'G'RILANDI: return qo'shildi

class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # TO'G'RILANDI: book → Book
    comment = models.TextField()  # TO'G'RILANDI: commit → comment (odatdagi nomlanish)
    stars_given = models.IntegerField(
        validators =[MinValueValidator(1), MaxValueValidator((5))] 
    )  # TO'G'RILANDI: ImageField → IntegerField
    
    def __str__(self):
        return f"{self.stars_given} star for {self.book.title} by {self.user.username}"