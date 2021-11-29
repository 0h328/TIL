### 1. 가상환경 설정 및 활성화
- ``$ python -m venv venv``
- ``$ source venv/Scripts/activate``

### 2. ``django`` 설치
- ``$ pip install django``
- ``$ pip freeze > requirements.txt``
- ``$ touch .gitignore`` (venv는 git이 관리하면 안됨-확인 필수)

### ✔ skeleton 코드 사용시, 기존에 설치되어있는 패키지 확인 후
- ``$ pip install -r requirements.txt``

### 3. PJT 생성
- ``$ django-admin startproject <프로젝트명>``
- ``$ python manage.py runserver``

### 4. App 생성
- ``$ python manage.py startapp <app명>``

### 5. App 등록
- PJT/``settings.py``에 ``INSTALLED_APPS`` 에 ``'App명',`` 추가

### 6. 개발 시작