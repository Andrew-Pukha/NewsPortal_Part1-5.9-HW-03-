from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum




class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        # 1. суммарный рейтинг каждой статьи автора умножается на 3
        post_rating = (Post.objects.filter(author=self).aggregate(Sum('rating'))['rating__sum'] or 0) * 3


        # 2. суммарный рейтинг всех комментариев автора
        comment_rating = Comment.objects.filter(user=self.user).aggregate(Sum('rating'))['rating__sum'] or 0

        # 3. суммарный рейтинг всех комментариев к статьям автора
        post_comments_rating = Comment.object.filter(post__author=self).aggregate(Sum('rating'))['rating__sum'] or 0

        # Итоговый рейтинг
        self.rating = post_rating + comment_rating + post_comments_rating
        self.save()
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)



class Post(models.Model):  #Реализация связи "многие ко многим"(для реализации данной связи требуется Смежная таблица):
    article_column = 'ac'
    news_column = 'nc'
    column_type = [
        (article_column, 'Статья'),
        (news_column, 'Новость'),
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=column_type, default=article_column)  #choices - атрибут, который ограничивает
                                                                                #название дожности(напр. директор или кассир) не позволяя
                                                                                #добавить в это поле любое иное рандомное значение (к аргументу choices всегда
                                                                                #должен идти кортеж с наимнованиями должностей).
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')  #указываем, что смежная таблица должна быть PostCategory.
    title = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.content[:124] + '...' if len(self.content) > 124 else self.content



#Смежная таблица связи "многие ко многим":
class PostCategory(models.Model):  #Реализация связи "один ко многим"(дважды):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  #Post - модель, на которую ссылаемся.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()                          #Текст комментария.
    created_at = models.DateTimeField(auto_now_add=True)  #Дата и время создания,
                                                          #auto_now_add - автоматически устанавливает в это поле дату создания объекта,
                                                          #если значение параметра True.
    rating = models.IntegerField(default=0)               #Рейтинг комментария.

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

