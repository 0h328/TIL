# ๐ ๊ฐ๋จํ ๊ฒ์ํ์ ๋ง๋ค๊ธฐ ์ํ ๊ณผ์ 



### โ MTV

- M(odel) - T(emplate) - V(iew)

![](https://mdn.mozillademos.org/files/13931/basic-django.png)

### โ Form 

- ์ ํจ์ฑ ๊ฒ์ฆ ๋ฐ ๊ฒ์ฆ ๊ฒฐ๊ณผ ์ ๊ณต

### โ ModelForm

- Formํด๋์ค๋ฅผ ์์๋ฐ๊ณ , Model๊ณผ ๊ด๋ จ๋์ด์์๋ ์ฌ์ฉ

### โ Form vs ModelForm

- Form : ๋ชจ๋ธ์ ์ฐ๊ด๋์ง ์์ ๋ฐ์ดํฐ๋ฅผ ๋ฐ์๋ ์ฒ๋ฆฌ (์ฌ์ฉ์์๊ฒ ๋ฐ๊ณ ์ํ๋ ์ ๋ณด ์ฌ์ ์)
- ModelForm : ๋ชจ๋ธ์ ์ฐ๊ด๋ ๋ฐ์ดํฐ๋ฅผ ๋ฐ์๋ ์ฒ๋ฆฌ (์ฌ์ ์ํ์X)


### 1. ๋ชจ๋ธ๋ง

- ``models.py``์ DB ์ปฌ๋ผ ๋ฐ ์ด๋ค ํ์์ผ๋ก ์ ์ํ  ๊ฒ์ธ์ง ์์ฑ

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True) : ์ต์ด ์์ฑ ์๊ฐ์ ํ์. ๋ฐ์ดํฐ๊ฐ ์๋์ผ๋ก ๊ธฐ๋ก๋จ.
    # updated_at = models.DateTimeField(auto_now=True)	: ์ต์ข ์์  ์๊ฐ์ ํ์. ๋ฐ์ดํฐ๊ฐ ์๋์ผ๋ก ๊ธฐ๋ก๋จ.
```



### 2. Migrations

- ๋ชจ๋ธ ๋ณ๊ฒฝ์ ๋ฐ๋ฅธ ์ค๊ณ๋ ๋ง๋ค๊ธฐ

  ``python manage.py makemigrations``

- ์ค๊ณ๋๋ฅผ ์ค์  DB์ ๋ฐ์ํ๊ธฐ

  ``python manage.py migrate``



### 3. ํผ ์์ฑ

- ๋ชจ๋ธ ์ ๋ณด๋ฅผ ์๊ณ  ์๋ ๊ฒฝ์ฐ.. ์ฆ, ๋ชจ๋ธ๊ณผ ์ฐ๊ด์๋ ๋ฐ์ดํฐ๋ฅผ ์ฒ๋ฆฌํ๊ธฐ ์ํด์๋ **ModelForm**์ ์ ์ธํ๋ค.
- Widgets๊น์ง ์ ์ฉํ๊ธฐ(Widget์ ๋จ๋์ ์ผ๋ก ์ฌ์ฉX - Form fields์ ํ ๋น๋์ด ์ฌ์ฉ)

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
    	label='์ ๋ชฉ',
    	widget=forms.TextInput(
        	attrs={
                'class': 'my-title form-control',
                'placeholder': '์ ๋ชฉ์ ๋ฃ์ผ์์ค',
                
            }
        ),
    )
    content = forms.CharField(
    	label='๋ด์ฉ',
    	widget=forms.Textarea(
        	attrs={
                'class': 'my-content form-control',
                'placeholder': '๋ด์ฉ์ ๋ฃ์ผ์์ค',
                
            }
        ),
        error_messages={
            'required': '๋ด์ฉ์ ์์ฑํ์์ค'
        }
    )
    
    class Meta: # ์ด๋ค ๋ชจ๋ธ์ ๊ธฐ๋ฐ์ผ๋ก ํผ์ ์์ฑํ  ๊ฒ์ธ์ง์ ๋ํ ์ ๋ณด๋ฅผ ์ง์ ํ๋ 
        model = Article # ๋ชจ๋ธ ์ ๋ณด๋ฅผ ์ ๋ฌ (ํด๋น ๋ชจ๋ธ๋ก ํผ ์์ฑ, ์ ํจ์ฑ ๊ฒ์ฌ, DB ์ ์ฅ)
        fields = '__all__'
```



### 4. HTTP ์์ฒญ์ View์ ์ ๋ฌํ๊ธฐ ์ํ url ์์ฑ

- ์ฌ๋ฌ ์ฑ ๊ด๋ฆฌ๋ฅผ ์ํด ํ๋ก์ ํธ ``urls.py``์๋ ``include``๋ฅผ ํตํด ์ฌ๋ฌ ์ฑ ์ฐธ์กฐ

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

- ๊ฐ ์ฑ์๋ ``urls.py`` ์์ฑ

```python
from django.urls import path
from . import views

app_name = 'articles'

# variable routing ์ฌ์ฉ = URL์ ํน์ ํ ์์๋ฅผ ๋ณ์ํ์์ผ์ ๋๊ฒจ์ค <int:pk>
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
]
```



### 5. HTTP ์์ฒญ์ ๋ฐ๊ณ  ์๋ตํ๊ธฐ ์ํด View ์์ฑ

- ๋ชจ๋ธ์ ํตํด ์์ฒญ์ ๋ง๋ ๋ฐ์ดํฐ์ ์ ๊ทผ

```python
from django.shortcuts import render, redirect, get_object_or_404
# get_object_or_404 : ์กฐ๊ฑด์ ๋ง๋ ๋ฐ์ดํฐ๊ฐ ์์ ๊ฒฝ์ฐ, ๊ธฐ์กด http status code 500(๊ฐ๋ฐ์ํ) -> http 404(์ฌ์ฉ์ํ)์ผ๋ก raise
from django.views.decorators.http import require_http_methods, require_POST, require_safe
# ์์ฒญ method์ ๋ฐ๋ผ view ํจ์์ ์ ๊ทผ ์ ํ / ์์ฒญ์ด ์กฐ๊ฑด์ ์ด๊ธ๋๋ฉด 405 Method Not Allowed๋ฅผ return
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required	# ๋ก๊ทธ์ธ๋ ์ฌ์ฉ์๋ง [๊ธ ์์ฑ]์ด ๊ฐ๋ฅํ๋ค.
@require_http_methods(['GET', 'POST'])	# viewํจ์๊ฐ 'GET'๊ณผ 'POST' ์์ฒญ๋ง ํ์ฉํ๋๋ก ํ๋ ๋ฐ์ฝ๋ ์ดํฐ
def create(request):
    if request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid(): # 1. ์ ํจ์ฑ ๊ฒ์ฆ์ด ํต๊ณผ๋์ง ์์ผ๋ฉด, is_valid()์์ ์๋ฌ๋ฉ์์ง๊ฐ ํฌํจ๋์ด์๊ณ .
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()    # 2. ์๋ฌ๋ฉ์์ง๊ฐ ํฌํจ๋ ํผ์ ๋ค์
    context = {                 # 3. context์ ๋ด์์
        'form': form,
    }
    return render(request, 'articles/form.html', context)   # 4. ์ฌ์ฉ์๋ ์๋ฌ๋ฉ์์ง๊ฐ ๋ด๊ธด html์ ๋ณด๊ฒ๋๋ค.


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_POST	# viewํจ์๊ฐ POST method ์์ฒญ๋ง ํ์ฉํ๋๋ก ํ๋ ๋ฐ์ฝ๋ ์ดํฐ
def delete(request, pk):
    if request.user.is_authenticated:	# ์ฌ์ฉ์ ์ธ์ฆ์ด ๋ ์ํ์์๋ง [๊ธ ์ญ์ ]๊ฐ ๊ฐ๋ฅํ๋ค.
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect('articles:index')


@login_required	# ๋ก๊ทธ์ธ๋ ์ฌ์ฉ์๋ง [๊ธ ์์ ]์ด ๊ฐ๋ฅํ๋ค.
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/form.html', context)
```



### 6. Template ์์

- ์ฝ๋ ์ฌ์ฌ์ฉ์ฑ, ์ฌ์ดํธ์ ๋ชจ๋  ๊ณตํต ์์ ํฌํจ, ํ์ ํํ๋ฆฟ ์ฌ์ ์

  ``templates/base.html`` ์์ฑ

```html
{% load bootstrap5 %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  {% bootstrap_css %}
  <title>Document</title>
</head>
<body>
  <div class="container">
    {% block content %}
    {% endblock content %}
  </div>
  {% bootstrap_javascript %}
</body>
</html>
```

- ์ดํ, ``settings.py``์ ``TEMPLATES = [ {'DIRS' : [BASE_DIR / 'templates'] } ]``๋ฅผ ์์ฑํ์ฌ ๋๋ ํ ๋ฆฌ ์ธ ํํ๋ฆฟ ์ถ๊ฐ ๊ฒฝ๋ก๋ฅผ ์ค์ ํด์ผํจ



### 7. Templates ์์ฑ

- ``index.html`` (READ)

```html
{% extends 'base.html' %}
{% load bootstrap5 %}

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">[CREATE]</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[๊ธ์ ์์ฑํ๋ ค๋ฉด ๋ก๊ทธ์ธ ํด์ฃผ์ธ์!]</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <p>๊ธ ๋ฒํธ : {{ article.pk }}</p>
    <p>๊ธ ์ ๋ชฉ : {{ article.title }}</p>
    <p>๊ธ ๋ด์ฉ : {{ article.content }}</p>
    <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
    <hr>
  {% endfor %}
{% endblock content %}
```

- ``form.html`` (CREATE + UPDATE)

```html
{% extends 'base.html' %}
{% load bootstrap5 %}

{% block content %}
  <h1>CREATE</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}
```

- ``detail.html`` (READ)

```html
{% extends 'base.html' %}
{% load bootstrap5 %}

{% block content %}
  <h2>DETAIL</h2>
  <h3>{{ article.pk }} ๋ฒ์งธ ๊ธ</h3>
  <hr>
  <p>์ ๋ชฉ : {{ article.title }}</p>
  <p>๋ด์ฉ : {{ article.content }}</p>
  <p>์์ฑ์๊ฐ : {{ article.created_at }}</p>
  <p>์์ ์๊ฐ : {{ article.updated_at }}</p>
  <hr>
  <a href="{% url 'articles:update' article.pk %}">[UPDATE]</a>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <button>DELETE</button>
  </form>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}
```