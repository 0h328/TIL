# 📝 간단한 게시판을 만들기 위한 과정



### ✔ MTV

- M(odel) - T(emplate) - V(iew)

![](https://mdn.mozillademos.org/files/13931/basic-django.png)

### ✔ Form 

- 유효성 검증 및 검증 결과 제공

### ✔ ModelForm

- Form클래스를 상속받고, Model과 관련되어있을때 사용

### ✔ Form vs ModelForm

- Form : 모델에 연관되지 않은 데이터를 받을때 처리 (사용자에게 받고자하는 정보 재정의)
- ModelForm : 모델에 연관된 데이터를 받을때 처리 (재정의필요X)


### 1. 모델링

- ``models.py``에 DB 컬럼 및 어떤 타입으로 정의할 것인지 작성

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True) : 최초 생성 시간을 표시. 데이터가 자동으로 기록됨.
    # updated_at = models.DateTimeField(auto_now=True)	: 최종 수정 시간을 표시. 데이터가 자동으로 기록됨.
```



### 2. Migrations

- 모델 변경에 따른 설계도 만들기

  ``python manage.py makemigrations``

- 설계도를 실제 DB에 반영하기

  ``python manage.py migrate``



### 3. 폼 작성

- 모델 정보를 알고 있는 경우.. 즉, 모델과 연관있는 데이터를 처리하기 위해서는 **ModelForm**을 선언한다.
- Widgets까지 적용하기(Widget은 단독적으로 사용X - Form fields에 할당되어 사용)

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
    	label='제목',
    	widget=forms.TextInput(
        	attrs={
                'class': 'my-title form-control',
                'placeholder': '제목을 넣으시오',
                
            }
        ),
    )
    content = forms.CharField(
    	label='내용',
    	widget=forms.Textarea(
        	attrs={
                'class': 'my-content form-control',
                'placeholder': '내용을 넣으시오',
                
            }
        ),
        error_messages={
            'required': '내용을 작성하시오'
        }
    )
    
    class Meta: # 어떤 모델을 기반으로 폼을 작성할 것인지에 대한 정보를 지정하는 
        model = Article # 모델 정보를 전달 (해당 모델로 폼 생성, 유효성 검사, DB 저장)
        fields = '__all__'
```



### 4. HTTP 요청을 View에 전달하기 위한 url 작성

- 여러 앱 관리를 위해 프로젝트 ``urls.py``에는 ``include``를 통해 여러 앱 참조

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

- 각 앱에도 ``urls.py`` 작성

```python
from django.urls import path
from . import views

app_name = 'articles'

# variable routing 사용 = URL의 특정한 요소를 변수화시켜서 넘겨줌 <int:pk>
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
]
```



### 5. HTTP 요청을 받고 응답하기 위해 View 작성

- 모델을 통해 요청에 맞는 데이터에 접근

```python
from django.shortcuts import render, redirect, get_object_or_404
# get_object_or_404 : 조건에 맞는 데이터가 없을 경우, 기존 http status code 500(개발자탓) -> http 404(사용자탓)으로 raise
from django.views.decorators.http import require_http_methods, require_POST, require_safe
# 요청 method에 따라 view 함수에 접근 제한 / 요청이 조건에 어긋나면 405 Method Not Allowed를 return
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


@login_required	# 로그인된 사용자만 [글 작성]이 가능하다.
@require_http_methods(['GET', 'POST'])	# view함수가 'GET'과 'POST' 요청만 허용하도록 하는 데코레이터
def create(request):
    if request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid(): # 1. 유효성 검증이 통과되지 않으면, is_valid()안에 에러메시지가 포함되어있고.
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()    # 2. 에러메시지가 포함된 폼을 다시
    context = {                 # 3. context에 담아서
        'form': form,
    }
    return render(request, 'articles/form.html', context)   # 4. 사용자는 에러메시지가 담긴 html을 보게된다.


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_POST	# view함수가 POST method 요청만 허용하도록 하는 데코레이터
def delete(request, pk):
    if request.user.is_authenticated:	# 사용자 인증이 된 상태에서만 [글 삭제]가 가능하다.
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect('articles:index')


@login_required	# 로그인된 사용자만 [글 수정]이 가능하다.
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



### 6. Template 상속

- 코드 재사용성, 사이트의 모든 공통 요소 포함, 하위 템플릿 재정의

  ``templates/base.html`` 생성

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

- 이후, ``settings.py``에 ``TEMPLATES = [ {'DIRS' : [BASE_DIR / 'templates'] } ]``를 작성하여 디렉토리 외 템플릿 추가 경로를 설정해야함



### 7. Templates 작성

- ``index.html`` (READ)

```html
{% extends 'base.html' %}
{% load bootstrap5 %}

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">[CREATE]</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[글을 작성하려면 로그인 해주세요!]</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <p>글 번호 : {{ article.pk }}</p>
    <p>글 제목 : {{ article.title }}</p>
    <p>글 내용 : {{ article.content }}</p>
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
  <h3>{{ article.pk }} 번째 글</h3>
  <hr>
  <p>제목 : {{ article.title }}</p>
  <p>내용 : {{ article.content }}</p>
  <p>작성시각 : {{ article.created_at }}</p>
  <p>수정시각 : {{ article.updated_at }}</p>
  <hr>
  <a href="{% url 'articles:update' article.pk %}">[UPDATE]</a>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <button>DELETE</button>
  </form>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}
```