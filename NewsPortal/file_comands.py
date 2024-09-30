#from django.contrib.auth.models import User
#from your_app.models import Author, Category, Post, Comment

#user1 = User.objects.create_user('user1', password='password123')
#user2 = User.objects.create_user('user2', password='password456')

#author1 = Author.objects.create(user=user1)
#author2 = Author.objects.create(user=user2)


#category_1 = Category.objects.create(name = "Политика")
#category_2 = Category.objects.create(name = "Медицина")
#category_3 = Category.objects.create(name = "История")
#category_4 = Category.objects.create(name = "Фантастика")



#article_column_1 = Post.objects.create(author = author1, type = 'ac', title = 'Статья 1', content = 'Содержание 1-ой статьи..." )
#article_column_2 = Post.objects.create(author = author1, type = 'ac', title = 'Статья 2', content = 'Содержание 2-ой статьи..." )
#news_column = Post.objects.create(author = author2, type = 'nc', title = 'Новость', content = 'Содержание новостной ленты..." )


#article_column_1 = PostCategory.objects.add(category_1, category_3)
#article_column_1 = PostCategory.objects.add(category_2, category_3)
#news_column = PostCategory.objects.add(category_4)


#comment1 = Comment.objects.create(post=article_column_1, user=user2, content="Комментарий к 1-ой статье"
#comment2 = Comment.objects.create(post=article_column_2, user=user2, content="Комментарий ко 2-ой статье"
#comment3 = Comment.objects.create(post=news_column, user=user1, content="Комментарий к новостной колонке"



#comment1.like()
#comment2.dislike()
#comment2.like()

#article_column_1.like()
#article_column_2.like()
#news_column.dislike()




#user1.update_rating()
#user2.update_rating()