from django.db import models
from datetime import date


class User(models.Model):
    nick_name = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(default="", max_length=20)
    last_name = models.CharField(default="", max_length=20)
    birth_day = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(default="", max_length=50)
    password = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.nick_name

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})   

class Genre(models.Model):
    name = models.CharField(default="", unique=True, max_length=50)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Genre_detail", kwargs={"pk": self.pk})

DEFAULT_GENRE_ID = 1

class Book(models.Model):
    title = models.CharField(unique=True, max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, default=DEFAULT_GENRE_ID, on_delete=models.CASCADE)
    description = models.TextField(default="")
    last_upd = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    publish_date = models.DateField(auto_now=True, auto_now_add=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.comment_text

    def get_absolute_url(self):
        return reverse("Comment_detail", kwargs={"pk": self.pk})
