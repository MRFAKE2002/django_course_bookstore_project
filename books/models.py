from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Book(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    cover = models.ImageField(upload_to='cover/', blank=True) # upload to file cover in Images and it can be empty
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])
    
class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) # if we dilate the user everything about this will be deleted
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments') 
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True)
    
    datetime_create = models.DateTimeField(auto_now_add=True) # it show time of creation in database
    
    def __str__(self):
        return self.text

