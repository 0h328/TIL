# ๋ชจ๋ธ ๊ด๊ณ



## ๐ 1 : N ๊ด๊ณ 

- Article (1) : Comment (N)

- ์ฒซ ๋ฒ์งธ ์ธ์๋ ์ฐธ์กฐํ๋ model class
- ๋ ๋ฒ์งธ ์ธ์๋ on_delete ์ต์
  - ์ธ๋ ํค๊ฐ ์ฐธ์กฐํ๋ ๊ฐ์ฒด๊ฐ ์ฌ๋ผ์ก์ ๋ ์ธ๋ ํค๋ฅผ ๊ฐ์ง ๊ฐ์ฒด๋ฅผ ์ด๋ป๊ฒ ์ฒ๋ฆฌํ  ์ง๋ฅผ ์ ์
    - CASCADE : ๋ถ๋ชจ ๊ฐ์ฒด(์ฐธ์กฐ ๋ ๊ฐ์ฒด)๊ฐ ์ญ์  ๋์ ๋ ์ด๋ฅผ ์ฐธ์กฐํ๋ ๊ฐ์ฒด๋ ์ญ์ 

```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
```

- ``ForeignKeyField``๋ 'article_id'์ ๊ฐ์ด ์์ฑ๋จ.
- ์ญ์ฐธ์กฐ (1์ด N์ ์ ๊ทผ - 'comment_set')
  - ``article.comment``๊ฐ ์๋ ``article.comment_set``์ผ๋ก ์ ๊ทผ / ``dir(article)``์ ํตํด ์ ๊ทผ๋ฒ ํ์ธ
  - ์ธ ๋ฒ์งธ ์ธ์์ 'related_name'์ผ๋ก ์ฌ์ฉํ  ์ด๋ฆ์ ์ง์ ํ  ์ ์์ -> ์ง์  ํ migration
  - ``article.comment_set``์ ์ฌ์ฉํ  ์ ์๊ณ , ``article.comments``๋ก ๋์ฒด๋จ.

```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
```

- ์ฐธ์กฐ (N์ด 1์ ์ ๊ทผ - 'article')
  - ``comment.article``๋ก ์ ๊ทผ 



### ๐ Foreign Key (์ธ๋ํค)

- RDB์์ ํ ํ์ด๋ธ์ ํ๋ ์ค ๋ค๋ฅธ ํ์ด๋ธ์ ํ์ ์๋ณํ  ์ ์๋ ํค
- ์ฐธ์กฐํ๋ ํ์ด๋ธ์์ 1๊ฐ์ ํค๋ ์ฐธ์กฐ๋๋ ํ์ด๋ธ์ ๊ธฐ๋ณธ ํค(PK)๋ฅผ ๊ฐ๋ฆฌํด
- ์ฐธ์กฐํ๋ ํ์ด๋ธ์ ํ 1๊ฐ๋ ์ฐธ์กฐ๋๋ ํ์ด๋ธ์ ํ ๊ฐ์ ๋์
  - ์ฐธ์กฐํ๋ ํ์ด๋ธ์ ํ ์ฌ๋ฌ๊ฐ๊ฐ ์ฐธ์กฐ๋๋ ํ์ด๋ธ์ ๋์ผํ ํ ์ฐธ์กฐ ๊ฐ๋ฅ

![image-20211129191105071](03_model-relation.assets/image-20211129191105071.png)

- ํค๋ฅผ ์ฌ์ฉํ์ฌ ๋ถ๋ชจ ํ์ด๋ธ์ ์ ์ผํ ๊ฐ์ ์ฐธ์กฐ (์ฐธ์กฐ ๋ฌด๊ฒฐ์ฑ)
  - ์ฐธ์กฐ ๋ฌด๊ฒฐ์ฑ - DB ๊ด๊ณ ๋ชจ๋ธ์์ ๊ด๋ จ๋ 2๊ฐ์ ํ์ด๋ธ ๊ฐ์ ์ผ๊ด์ฑ
- ์ธ๋ ํค์ ๊ฐ์ด ๋ฐ๋์ ๋ถ๋ชจ ํ์ด๋ธ์ ๊ธฐ๋ณธ ํค(PK)์ผ ํ์๋ ์์ง๋ง ์ ์ผํ ๊ฐ์ด์ด์ผ ํจ.



### โ ๋๊ธ ์กฐํ

```python
# articles/views.py

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
```

- ``ForeignKeyField``๋ฅผ ์์ฑ์๊ฐ ์ง์  ์๋ ฅํ๋ ์ํฉ์ด ๋ฐ์![image-20211129192555444](03_model-relation.assets/image-20211129192555444.png)
- CommentForm์์ ์ธ๋ ํค ํ๋ ์ถ๋ ฅ ์ ์ธ

```python
# articles/forms.py

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        exclude = ('article',)
```

```html
<!-- articles/detail.html -->

{% block content %}
<h4>๋๊ธ ๋ชฉ๋ก</h4>
{% if comments %}
	<p>{{ comments|length }}๊ฐ์ ๋๊ธ์ด ์์ต๋๋ค.</p>
{% endif %}
<ul>
    {% for comment in comments %}
    <li>๋๊ธ ์์ฑ ์ ์ : {{ comment.user }}</li>
    <li>๋๊ธ ๋ฒํธ: {{ comment.pk }}</li>
    <li>๋๊ธ ๋ด์ฉ: {{ comment.content }}</li>
    {% empty %}
    <p>๋๊ธ์ด ์์ต๋๋ค</p>
    {% endfor %}
</ul>
{% endblock %}
```



### โ ๋๊ธ ์์ฑ

```python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
]
```

```python
# articles/views.py

@require_POST
def comments_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)
```

- ``save(commit=False)``
  - ์์ง DB์ ์ ์ฅ๋์ง ์์ ์ธ์คํด์ค๋ฅผ ๋ฐํ
  - ์ ์ฅํ๊ธฐ ์ ์ ๊ฐ์ฒด์ ๋ํ ์ฌ์ฉ์ ์ง์  ์ฒ๋ฆฌ๋ฅผ ์ํํ  ๋ ์ ์ฉํ๊ฒ ์ฌ์ฉ

```html
<!-- articles/detail.html -->
<!-- ๋๊ธ ์์ฑ form -->

{% block content %}
  {% if reuqest.user.is_authenticated %} <!-- -->
    <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
      {% csrf_token %}
      {{ comment_form }}
      <input type="submit" value="๋๊ธ ์์ฑ">
    </form>
  {% else %}
    <a href="{% url 'accounts:login' %}">[๋๊ธ์ ์์ฑํ๋ ค๋ฉด ๋ก๊ทธ์ธํ์์ค]</a>
  {% endif %}
{% endblock %}
```



### โ ๋๊ธ ์ญ์ 

```python
# articles/urls.py

urlpatterns = [
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]
```

```python
# articles/views.py

@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)
```

```html
<!-- articles/detail.html -->
{% block content %}
{% if request.user == comment.user %}
	<form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method='POST'>
        {% csrf_token %}
        <input type="submit" value="DELETE">
	</form>
{% endif %}
{% endblock %}
```



### โ User ๋ชจ๋ธ ๋์ฒด

- Django ์ ํ๋ก์ ํธ ์์ ์, ์ปค์คํ ์ ์  ๋ชจ๋ธ ์ค์ ์ ๊ถ์ฅ
  - ๋ด์ฅ User ๋ชจ๋ธ์ด ์ ๊ณตํ๋ ์ธ์ฆ ์๊ตฌ์ฌํญ์ด ์ ์ ํ์ง ์์ ์ ์๊ธฐ ๋๋ฌธ
    - ex) username ๋์  email์ ์๋ณ ํ ํฐ์ผ๋ก ์ฌ์ฉํ๋ ๊ฒ์ด ๋ ์ ํฉํ ์ฌ์ดํธ
- ``AUTH_USER_MODEL``
  - User๋ฅผ ๋ํ๋ด๋๋ฐ ์ฌ์ฉํ๋ ๋ชจ๋ธ
  - ๊ธฐ๋ณธ ๊ฐ : 'auth.user'
- ๊ธฐ์กด์ django๊ฐ ์ฌ์ฉํ๋ User ๋ชจ๋ธ์ด์๋ auth ์ฑ์ User ๋ชจ๋ธ์ accounts ์ฑ์ User ๋ชจ๋ธ์ ์ฌ์ฉํ๋๋ก ๋ณ๊ฒฝ

```python
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```

```python
# accounts/models.py

form django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

```python
# accounts/admin.py

from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User

admin.site.register(User, UserAdmin)
```

- db.sqlite3 ํ์ผ ์ญ์  ๋ฐ migrations ํ์ผ ๋ชจ๋ ์ญ์  (0001_initail.py ...) ํ migrate ์ฌ ์งํ



- ํ์๊ฐ์ ์, ์๋์ ๊ฐ์ ์๋ฌ ๋ฐ์
  - UserCreationForm๊ณผ UserChangeForm์ ๊ธฐ์กด ๋ด์ฅ User ๋ชจ๋ธ์  ์ฌ์ฉํ ModelFrom์ด๊ธฐ ๋๋ฌธ์ ์ปค์คํ User ๋ชจ๋ธ๋ก ๋์ฒดํด์ผ ํจ

![image-20211129200138465](03_model-relation.assets/image-20211129200138465.png)

```python
# accounts/forms.py

from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        # models.py์์  User ๋ชจ๋ธ์ ๋ถ๋ฅด๋ฉด settings.AUTH_USER_MODEL
        # ๋๋จธ์ง ๋ชจ๋  ๊ณณ์์๋ get_user_model()
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)
```

- ์ด ํ, accounts/views.py์ signupํจ์์ ``UserCreationForm`` -> ``CustomUserCreationForm``
- ``settings.AUTH_USER_MODEL``
  - User ๋ชจ๋ธ์ ๋ํ ์ธ๋ ํค ๋๋ ๋ค๋๋ค ๊ด๊ณ๋ฅผ ์ ์ํ  ๋ ์ฌ์ฉ
- ``get_user_model()``
  - ํ์ฌ ํ์ฑํ๋ User ๋ชจ๋ธ์ ๋ฐํ
  - ์ปค์คํํ User ๋ชจ๋ธ์ด ์์ ๊ฒฝ์ฐ์ Custom User ๋ชจ๋ธ, ๊ทธ๋ ์ง ์์ผ๋ฉด User๋ฅผ ๋ฐํ

```PYTHON
# articles/models.py

form django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```



- makemigrations ์ดํ ๋ฐ์

![image-20211129201253904](03_model-relation.assets/image-20211129201253904.png)

- null ๊ฐ์ด ํ์ฉ๋์ง ์๋ user_id ํ๋๊ฐ ๋ณ๋์ ๊ฐ ์์ด article์ ์ถ๊ฐ๋๋ ค ํ๊ธฐ ๋๋ฌธ
- 1 + enter -> ํ์ฌ ํ๋ฉด์์ ๊ธฐ๋ณธ ๊ฐ์ ์ค์ ํ๊ฒ ๋ค
- 1 + enter -> ๊ธฐ์กด ํ๋์ ์ถ๊ฐ๋๋ user_id ํ๋์ ๊ฐ์ 1๋ก ์ค์ ํ๊ฒ ๋ค



- ๊ฒ์๊ธ ์ถ๋ ฅํ๋ ์์  ์, ๋ค์๊ณผ ๊ฐ์ ์๋ฌ ๋ฐ์

![image-20211129201438178](03_model-relation.assets/image-20211129201438178.png)

- CREATE

```python
# articles/views.py

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)   # commit=False ์ถ๊ฐ - ์ ์ฅ ๋ฉ์ถ๊ณ  ๊ฐ์ฒด ๋ฐํ
            article.user = request.user         # ์์ฑ์ ์ ๋ณด ์ถ๊ฐ  - ๋ก๊ทธ์ธํ ์ ์  ์ ๋ณด๋ฅผ ๋ฃ์ด์ฃผ๊ณ 
            article.save()                      # ์ ์ฅ ์ถ๊ฐ - ๋ค์ ์ ์ฅ
            return redirect('articles:detail', article.pk)
```

- DELETE

```python
@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)    
    if request.user.is_authenticated:
        if request.user == article.user:	# ์์ ์ด ์์ฑํ ๊ฒ์๊ธ๋ง ์ญ์ 
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail')
```

- UPDATE

```PYTHON
@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # update ํจ์๋ฅผ ์์ฒญํ ์ ์ ๊ฐ ๊ฒ์๊ธ์ ์์ฑํ ์ ์ ์ ๋์ผํ ๊ฒฝ์ฐ์๋ง ์์ ์ ํ  ์ ์๋๋ก ์กฐ๊ฑด ์ค์ 
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

- ํด๋น ๊ฒ์๊ธ์ ์์ฑ์๊ฐ ์๋ ๊ฒฝ์ฐ, ์์ /์ญ์  ๋ฒํผ ์ถ๋ ฅ๋์ง ์๋๋ก ์ฒ๋ฆฌ

```html
<!-- articles/index.html -->

  {% if user == article.user %}
    <a href="{% url 'articles:update' article.pk %}" class="btn btn-primary">[UPDATE]</a>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <button class="btn btn-danger">DELETE</button> 
    </form>
  {% endif %}
```



### โ User์ Comment ๋ชจ๋ธ ๊ด๊ณ

```python
# articles/models.py

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
```



- ์๋ ์๋ฌ ๋ฐ์ ์ด์  : ๋๊ธ ์์ฑ ์ ์์ฑ์ ์ ๋ณด(comment.user) ๋๋ฝ

![image-20211129202109236](03_model-relation.assets/image-20211129202109236.png)

```python
# articles/views.py

def comments_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)   # ๋๊ธ ์ ์ฅํ๋ ์์ ์ ์ด๋ค ๊ฒ์๊ธ์ ์ ์ฅ์ด ๋ ์ง ์ค์ ํด์ค
            comment.article = article
            comment.user = request.user	# ๋๊ธ ์์ฑ ์ ์์ฑ์ ์ ๋ณด(request.user) ์ถ๊ฐ ํ ๋๊ธ ์์ฑ ์ฌ์๋
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('articles:detail')
```

```python
# articles/views.py

def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:	# ์์ ์ด ์์ฑํ ๋๊ธ๋ง ์ญ์  ํ  ์ ์๋๋ก ์์ 
            comment.delete()
        return redirect('articles:detail', article_pk)
    return redirect('accounts:login')
```



## ๐ท M : N ๊ด๊ณ

- ์์ฌ (M) : ํ์ (N)
- ์์ฌ์๊ฒ ์ง์ฐฐ๋ฐ๋ ํ์, ํ์๋ฅผ ์ง์ฐฐํ๋ ์์ฌ
- ``ManyToManyField``
  - ``add()``, ``remove()``๋ฅผ ํตํด ๊ฐ์ฒด ์ถ๊ฐ, ์ ๊ฑฐ ๊ฐ๋ฅ
  - symmetrical
    - ``ManyToManyField``๊ฐ ๋์ผํ ๋ชจ๋ธ์ ๊ฐ๋ฆฌํค๋๋ ์ ์์์๋ง ์ฌ์ฉ

```python
class Doctor(models.Model):
    name = models.TextField()
    
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, related_name='patients') # doctor1.patients.all()
    name = models.TextField()
```



### โ Like

```python
# articles/models.py

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    """
    1:N
    article.user -> ๊ฒ์๊ธ์ ์์ฑํ ์ ์ 
    user.article_set -> ์ ์ ๊ฐ ์์ฑํ ๊ฒ์๊ธ ๋ชฉ๋ก

    M:N
    article.like_users -> ๊ฒ์๊ธ์ ์ข์์๋ฅผ ๋๋ฅธ ์ ์ 
    user.article_set -> ์ ์ ๊ฐ ์ข์์๋ฅผ ๋๋ฅธ ๊ฒ์๊ธ -> ์ด๊ฒ ๋ฌธ์ ! -> ์ด๋ฆ์ด ๊ฒน์น๋ค! -> related_name์ ํตํด ๋ณ๊ฒฝ ํ์! -> user.like_articles
    """

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```

```python
# articles/urls.py

urlpatterns = [
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
```

```python
# articles/views.py

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if article.like_users.filter(pk=request.user.pk).exists():	# exists()-์ฟผ๋ฆฌ์์ ํฌํจ๋์ด ์์ผ๋ฉด True, ๊ทธ๋ ์ง ์์ผ๋ฉด False
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')
```

```html
<!-- articles/index.html -->

  {% for article in articles %}
    <p>์ข์์ ์: {{ article.like_users.all|length }}</p>
    <div>
      <form action="{% url 'articles:likes' article.pk %}" method='POST'>
        {% csrf_token %}
        {% if request.user in article.like_users.all %}
          {% comment %} <input type="submit" value='์ข์์ ์ทจ์'> {% endcomment %}
          <button class='btn btn-link'>
            <i class="fas fa-heart" style='color: crimson;'></i>
          </button>
        {% else %}
          {% comment %} <input type="submit" value='์ข์์'> {% endcomment %}
          <button class='btn btn-link'>
            <i class="far fa-heart" style='color: black;'></i>          
          </button>
        {% endif %}
      </form>
    </div>
  {% endfor %}
```



### โ Profile 

```python
# accounts/urls.py

urlpatterns = [
    path('<username>/', views.profile, name='profile'),
]
```

```python
# accounts/views.py

def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }

    return render(request, 'accounts/profile.html', context)
```

```html
<!-- accounts/profile.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>{{ person.username }}์ ํ๋กํ ํ์ด์ง</h1>
  <hr>

  <h2>{{ person.username }}์ ํ๋ก์ฐ</h2>
  {% comment %} {% with followings=person.followings.all followers=person.followers.all %} {% endcomment %}
  <p>ํ๋ก์: {{ person.followings.all|length }}</p>
  <p>ํ๋ก์: {{ person.followers.all|length }}</p>

  {% comment %} 
  request.user -> ๋
  person -> ๋
  {% endcomment %}
  <div>
    {% if request.user != person %}
      <div>
        <form action="{% url 'accounts:follow' person.pk %}" method='POST'>
          {% csrf_token %}
          {% comment %} request.user ==> me {% endcomment %}
          {% if request.user in person.followers.all %}
            <button>์ธํ๋ก์ฐ</button>
          {% else %}
            <button>ํ๋ก์ฐ</button>
          {% endif %}    
        </form>
      </div>
    {% endif %}  
  </div>

  <h2>{{ person.username }}์ด ์์ฑํ ๊ฒ์๊ธ</h2>
  {% comment %} 
  person(user) -> 1
  article -> N

  1์ด N์ ์ง์  ๊ฐ์ ธ์ฌ ์ ์๊ธฐ ๋๋ฌธ์ _set์ ์ฌ์ฉ
  {% endcomment %}
  {% for article in person.article_set.all %}
    <p>{{ article.pk }}</p>
    <p>{{ article.title }}</p>
  {% endfor %}
  <hr>

  <h2>{{ person.username }}์ด ์์ฑํ ๋๊ธ</h2>
  {% for comment in person.comment_set.all %}
    <p>{{ comment.pk }}</p>  
    <p>{{ comment.content }}</p>  
  {% endfor %}

  <h2>{{ person.username }}์ด ์ข์์๋ฅผ ๋๋ฅธ ๊ฒ์๊ธ</h2>
  {% for article in person.like_articles.all %}
    <p>{{ article.pk }}</p>
    <p>{{ article.title }}</p>
  {% endfor %}

  <a href="{% url 'articles:index' %}">๋ค๋ก๊ฐ๊ธฐ</a>
{% endblock content %}
```

```html
<!-- base.html -->

<body>
  <div class="container">
    {% if request.user.is_authenticated %}
      <h3>Hello, {{ user }}</h3>
      <a href="{% url 'accounts:profile' request.user.username %}">์ ์  ํ๋กํ</a>
    {% else %}
      <a href="{% url 'accounts:login' %}">Login</a>
      <a href="{% url 'accounts:signup' %}">Signup</a>
    {% endif %}
```

```html
<!-- articles/index.html -->
<p>
    <b>์์ฑ์ : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></b>
</p>
```



### โ follow

```python
# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

```python
# accounts/urls.py

urlpatterns = [
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
```

```python
# accounts/views.py

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        you = get_object_or_404(get_user_model(), pk=user_pk)
        me = request.user
        if you != me:
            if you.followers.filter(pk=request.user.pk).exists():
                you.followers.remove(me)    # ์ธํ
            else:
                you.followers.add(me)       # ํ๋ก์ฐ
        return redirect('accounts:profile', you.username)

    return redirect('accounts:login')
```

```html
{% block content %}
  <p>ํ๋ก์: {{ person.followings.all|length }}</p>
  <p>ํ๋ก์: {{ person.followers.all|length }}</p>

  {% comment %} 
  request.user -> ๋
  person -> ๋
  {% endcomment %}
  <div>
    {% if request.user != person %}
      <div>
        <form action="{% url 'accounts:follow' person.pk %}" method='POST'>
          {% csrf_token %}
          {% comment %} request.user ==> me {% endcomment %}
          {% if request.user in person.followers.all %}
            <button>์ธํ๋ก์ฐ</button>
          {% else %}
            <button>ํ๋ก์ฐ</button>
          {% endif %}    
        </form>
      </div>
    {% endif %}  
  </div>
{% endblock %}
```

