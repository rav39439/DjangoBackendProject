from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    description = models.CharField(max_length=600)

    published_year =  models.TextField()
    def __str__(self):
        return self.title


# class Review(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
#     username = models.CharField(max_length=100)
#     comment = models.TextField()
#     bookid = models.IntegerField() 
#     created_at = models.DateTimeField(auto_now_add=True)



#     def __str__(self):
#         return f"Review by {self.username} on {self.book.title}"

class Review(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    username = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.TextField()

    bookid = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ No default manually added

    def __str__(self):
        return f"Review by {self.username} on {self.book.title}"
# Create your models here.
