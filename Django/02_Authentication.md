# ❗ 사용자 인증

### ✔  Authentication

- 인증된(로그인) 사용자만 서비스를 이용할 수 있다.



### ✔ HTTP

- 웹에서 이루어지는 모든 데이터 교환의 기초

- 데이터(HTML문서 등)들을 가져올 수 있게 해주는 규약

- 비연결지향(connectionless)과 무상태(stateless)의 특징을 가지고 있음.

  ❔비연결지향❔

  - 서버는 사용자가 작성한 데이터를 주고 연결을 끊음
  - 사용자 또한 서버로부터 데이터를 받고 연결을 끊음

  ❔무상태❔

  - 연결을 끊으면, 사용자의 상태 정보가 유지되지 않음
  - 클라이언트와 서버가 주고 받은 정보들은 독립적



### ✔ 쿠키

- 서버(django)가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각

  ex) 사용자가 로그인하면, 서버가 로그인 정보(쿠키)를 사용자(브라우저)에게 전달

- 브라우저(클라이언트)는 쿠키를 로컬에 KEY-VALUE 형식으로 저장

- 쿠키를 저장했다가 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송

- 브라우저에서 쿠키(로그인)만 강제로 지우면(로그아웃) DB에는 남아있다.



### ✔ 세션

- 사이트와 특정 브라우저 사이의 '상태'를 유지시켜주는 것

- 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급한다.

  ex) 로그인 했다는 정보를 전달(session)

  - 클라이언트는 발급 받은 session id를 쿠키에 저장한다.
  - 클라이언트가 다시 서버에 접속하면 요청과 함께 쿠키를 서버에 전달

  ⏰ 쿠키의 수명

  - ``settings.py`` 에``SESSION_COOKIE_AGE =`` 으로 수명 지정 가능(기본값은 2주)

- 개발자도구에서 session 지우기 = DB의 ``django_session`` 테이블에서 행 하나 삭제 = **로그아웃**



### 1. App 생성

- ``python manage.py startapp accounts``



### 2. App 등록 및 url 설정

- ``settings.py`` 에 ``INSTALLED_APPS = ['accounts',]`` 추가

```python
# 프로젝트/urls.py

urlpatterns = [
    path('accounts/', include('accounts.urls')),
]
```



```python
# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('change_password/', views.change_password, name='change_password'),
]
```



### 💥 skeleton 코드 사용시

- ``python manage.py migrate``
  - 안하면, DB 반영이 안되고 ``django.db.utils.OperationalError: no such table: auth_user`` 발생



### ❌ 로그인 사용자에 대한 접근 제한

#### ✔ is_authenticated

- User model의 속성
- 사용자가 인증되었는지 여부를 알 수 있음
- 인증된 ``User`` 인스턴스는 항상 ``True`` / ``AnonymousUser``는 항상 ``False``
  - ``{{ request.user }}`` 



#### ✔ login_required

- 사용자가 비로그인 상태면, ``/accounts/login/``으로 ``redirect``

- 사용자가 로그인 상태면, 정상적으로 View 함수 실행

- 인증 성공 시, 사용자가 ``redirect`` 되어야하는 경로는 `next`라는 쿼리 문자열 매개변수로 저장

  ex) /accounts/login/?next=/articles/create/

  ❔`next`❔

  - 로그인이 정상적으로 진행되면 기존에 요청했던 주소로 ``redirect`` 해주기 위해 주소를 keep
  - 별도로 처리해주지 않으면 View에 설정한 redirect 경로로 이동



### 3. 회원가입

- ``signup``  (CREATE)
- ``UserCreationForm``
  - username, password1, password2 필드를 가짐

```python
@require_http_methods(['GET', 'POST'])
def signup(request):

    if request.user.is_authenticated:   # 이미 로그인(인증)된 user라면 회원가입 로직을 수행할 수 없도록 처리
        return redirect('articles:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()	# save 메서드가 user 정보를 return 해주기 때문
            # print(type(user)) # <class 'django.contrib.auth.models.User'>
            auth_login(request, user)   # 회원가입과 동시에 로그인하는 기능
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)
```



### 4. 회원탈퇴

- DB에서 사용자를 삭제하는 것과 같음 (DELETE)

```python
@require_POST
def delete(request):
    if request.user.is_authenticated:   # 이미 로그인(인증)된 user만
        request.user.delete()           # user 정보를 DB에서 삭제 (회원 탈퇴)
        auth_logout(request)            # 탈퇴 이후에 유저의 session 정보 삭제 + (clearsessions cron job)
    return redirect('articles:index')
```



### 5. 회원정보수정

- DB에서 사용자 정보를 수정하는 것과 같음(UPDATE)
- ModelForm을 다시 사용하며, ``UserChangeForm``을 사용
- 그러나, ``UserChangeForm``을 사용하면, 일반 사용자가 접근해서는 안될 정보들(fields)까지 모두 수정이 가능해짐
- 따라서, ``UserChangeForm``을 상속받아 ``CustomUserChangeForm``을 사용해야함

```python
# accounts/forms.py

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()	# 모델 정보
        fields = ('email', 'first_name', 'last_name',)
```



```python
@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)	# user가 변경할 데이터와 기존(회원가입시)에 등록한 데이터
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)	# 기존(회원가입시)에 등록한 데이터
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)
```



### 6. 로그인

- ``login`` (Session CREATE)
- ``AuthenticationForm``
  - 첫번째 인자로 ``request``
  - ``AuthenticationForm(forms.Form)``
    - 미리 설정된 모델X -> 모델 정보 필요X -> 로그인 정보는 DB에 저장X -> 유저가 인증되었는지만 확인 -> session 발급

```python
#1. 비로그인 상태에서 articles/create로 요청 시 login_required에 의해 accounts/login으로 redirect
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:	# 이미 로그인(인증)된 user라면 로그인 로직을 수행할 수 없도록 처리
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # form.get_user() -> django.contrib.auth.models.User # 폼을 통해 사용자가 만든 정보 : <User : asdf>
            auth_login(request, form.get_user())	
            # print(request.GET) # <QueryDict: {'next': ['/articles/create/']}>
            #4. next 파라미터에 지정된 value로 redirect된다.
            # 만약 next의 value값이 없다면 articles의 index로 redirect된다. (단축평가)
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        #2. login_required에 의해 GET 요청으로 들어오면
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    #3. form을 보여주고 로그인을 다시 한다. 이때 정상적으로 로그인이 된다면
    return render(request, 'accounts/auth_form.html', context)

# 이미 로그인(인증)된 user라면 로그인할 필요 X
# 로그인하는 기능
```



### 7. 로그아웃

- ``logout`` (Session DELETE)

```python
@require_POST
def logout(request):
    if request.user.is_authenticated:	# 로그인(인증)된 사용자만 로그아웃 로직을 수행할 수 있도록 처리
		auth_logout(request)
    return redirect('articles:index')
```



### 8. 비밀번호 변경

- ``PasswordChangeForm``
  - 첫번째 인자로 ``request.user``
- ``update_session_auth_hash``
  - 비밀번호 변경 시, 기존 세션과 불일치하여 로그인 상태를 유지할 수 없으므로 password hash로 session을 업데이트

```python
from django.contrib.auth import update_session_auth_hash

@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # 로그인이 풀렸다? -> 세션 정보가 삭제 되었거나 / 일치하지 않는다!
            # 비밀번호를 변경하여 업데이트된 세션을 기존 sessin db의 정보와 일치 시키자!
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)
```



### 9. Template 작성

```html
<!--accounts/auth_form.html-->
<!--템플릿 양식이 동일하기 때문에 하나의 템플릿을 작성 -->

{% extends 'base.html' %}
{% load bootstrap5 %}

{% block content %}
  {% if request.resolver_match.url_name == 'change_password' %}
    <h2>Change Password</h2>
  {% elif request.resolver_match.url_name == 'login' %}
    <h2>LOGIN</h2>
  {% elif request.resolver_match.url_name == 'signup' %}
    <h2>SIGN UP</h2>
  {% else %}
    <h2>User Info Change</h2>
  {% endif %}

  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons submit='Submit' reset='Cancel' %}{% endbuttons %}
  </form>
{% endblock %}
```



### 10. Template 상속

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
    {% if request.user.is_authenticated %}
      <a href="{% url 'accounts:logout' %}">[로그아웃]</a>
      <a href="{% url 'accounts:update' %}">[회원정보 수정]</a>
      <a href="{% url 'accounts:change_password' %}">[비밀번호 변경]</a>
      <form action="{% url 'accounts:delete' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="회원탈퇴" class="btn btn-danger">
      </form>
    {% else %}
      <a href="{% url 'accounts:login' %}">[로그인]</a>
      <a href="{% url 'accounts:signup' %}">[회원가입]</a>
    {% endif %}
  </div>

  <div class="container">
    {% block content %}
    {% endblock content %}
  </div>
  {% bootstrap_javascript %}
</body>
</html>
```



### ➕ user의 방문 횟수

- ``embed()``
  - ``from IPython import embed``
    - 나가기 : ``ctrl + d``

```python
# articles/views.py
@require_safe
def index(request):
    if request.session:	# 만약에 session 정보가 있다면 -> 로그인해서 요청을 보냈다면
        visits_num = request.session.get('visits_num', 0)
        request.session['visits_num'] = visits_num + 1
    else:	    # 그게 아니라면
        visits_num = 0

    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
        'visits_num': visits_num,
    }
    return render(request, 'articles/index.html', context)
```



```html
<!--articles/index.html-->
{% extends 'base.html' %}
{% load bootstrap5 %}

{% block content %}
  <h1>Articles</h1>
  <p>
    {{ request.user }}님의 방문 횟수: {{ visits_num }}
    {% if visits_num == 1 %} 
      time
    {% else %} 
      times
    {% endif %}
  </p>
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