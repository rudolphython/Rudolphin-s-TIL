1. **Static File**
   * 정적파일
   * 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주는 파일(CSS, 이미지, 자바스크립트 등)
   * static file의 경로는 기본 폴더까지만 설정되어 있음



2. **load**
   * 사용자 정의 템플릿 태그 세트를 로드, 로드하는 라이브러리, 패키지에 등록된 모든 태그와 필터를 로드
   * static을 사용하기 위해서는 해당 태그에 load가 있어야 함



3. **STATIC_ROOT**
   * 배포를 위해 정적 파일을 수집하는 디렉토리의 **절대 경로**
   * 모든 정적파일을 한 곳에 모아 넣는 경로
   * settings.py 에서 디버그 값이 True인 경우, 해당 값은 작용되지 않음
   * 실 서비스 환경 배포 시 사용할 예정
   * ex) 나의 장고 프로젝트가 다른 서버에서 작동되기 위해서는 해당 서버가 모든 경로 주소를 알고 있어야 함



4. **STATIC_URL**

   * **app/static/경로 및 STATICFILES_DIRS 추가 경로들을 탐색**
   * 실제 파일이나 디렉토리는 아니지만, URL로만 쓰임
   * 경로를 만들어줌 -> 기존의 경로에 추가 경로를 붙여서..

   ```python
   STATIC_URL = '/static/'
   ```

   ```html
   {% extends 'base.html' %}
   {% load static %}
   
   
   {% block content %}
     <h2>DETAIL</h2>
     <img src="{% static 'articles/tot.png' %}" alt="sample image">
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

   



5. **STATICFILES_DIRS**

   * app/static/ 디렉토리 경로를 사용하는 것(기본 경로) 외에 추가적인 정적 파일 경로 목록을 정의하는 리스트
   * 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성

   ```python
   STATIC_URL = '/static/'
   STATICFILES_DIRS = [
       BASE_DIR / 'static',
   ]
   
   # base.html 처럼 static 폴더와 그 안에 폴더를 만들어준 다음, 없는 경로이나 STATICFILES_DIRS의 경로를 써줘야 함.
   ```

   ```html
   {% load static %}
   
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <meta http-equiv="X-UA-Compatible" content="IE=edge">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
     <title>Document</title>
   </head>
   <body>
     <img src="{% static 'images/son.jpg' %}" alt="second sample image">
     <div class="container">
       {% block content %}
       {% endblock content %}
     </div>
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
   </body>
   </html>
   ```

   

6. **Media file**

   * 사용자가 웹에서 업로드하는 정적 파일
   * 유저가 업로드 한 모든 정적 파일



7. **Imagefield**
   * 이미지 업로드에 사용하는 모델 필드
   * 파일필드를 상속 받는 서브 클래스, 파일필드의 모든 속성 및 메서드가 가능
   * 이미지필드는 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사
   * 이미지필드 인스턴스는 최대 길이가 100자인 문자열로 생성(이미지 경로 문자열)
   * upload_to : 실제 이미지가 저장되는 경로 저장
   * blank=True : 이미지 필드에 빈 값이 허용되도록 설정(이미지를 선택적으로 업로드)
     * 비워둔다면 빈 문자열이 저장(유효성 검사 통과)



8. **FileField**

   * 파일 업로드에 사용하는 모델 필드, 2개의 선택 인자(upload_to)

     * upload_to : 업로드 디렉토리와 파일 이름을 설정하는 2가지 방법 제공

       -> 2가지 방법으로 사용 가능(문자열 값이나 경로 지정, 함수 호출)

       

9. **MEDIA_ROOT**(!= STATIC_ROOT)

   * 사용자가 업로드 한 파일들을 보관할 디렉토리의 절대 경로
   * 미디어 루트가 있어야 이미지의 파일 경로들이 저장이 됨!

   ```python
   # crud\settings.py
   
   MEDIA_ROOT = BASE_DIR / 'media'
   ```

   

10. **MEDIA_URL**

    * 미디어 루트에서 제공되는 미디어를 처리하는 URL
    * 업로드 된 파일의 주소를 만들어 주는 역할

    ```python
    # crud\settings.py
    
    MEDIA_URL = '/media/'
    ```

    * urls.py 에서 추가 경로를 작성해야 함!

    ```python
    from django.contrib import admin
    from django.urls import path, include
    from django.conf import settings
    from django.conf.urls.static import static
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('articles/', include('articles.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # static이라는 함수를 쓸 때 주소(URL)와 실제 파일 경로(실제 위치)
    ```



11. **pillow**
    * 사용 전 설치 필수!
    * 파이썬 라이브러리 중 이미지 처리 기능 역할



12. **Null option**

    * 기본 값 : False
    * 문자열 기반 필드가 아니라면(datefield같은) 써도 됨!!
    * True이면 장고는 빈 값을 DB에 NULL 저장
    * '데이터가 없음을 표현' -> 빈 문자열과 다름
    * 문자열 기반 필드(charfield, textfield)에는 사용하는 것을 피해야 함 -> 빈 문자열이 이미 그 기능을 대체하는 데 null까지 추가되면 혼동만 주니까~!

    * blank는 유효성 검사 적용, null은 데이터베이스에 영향
    * null은 유효성 검사를 통과하지 못한다~!



13. 폼 -> 인코딩 속성

    * multipart/form-data : 파일 업로드 시 반드 시 사용 -> 뷰 함수 처리해라~

    ```python
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>CREATE</h1>
      <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="작성">
      </form>
      <a href="{% url 'articles:index' %}">[back]</a>
    {% endblock content %}
    ```

    

14. **뷰함수에서 request.FILES 처리 후..**
    * media/images 생성 확인
    * 경로를 DB에 저장한 것임(media_root ~)



15. **accept**="image/*"

    * 이미지 파일이 선택될 수 있도록 유도

    * 고유 파일 유형 지정자

    * 필터링 역할은 아님!!(파일 검증은 아니라는 것!)

      

16. **이미지 접근**

    ```html
    {% extends 'base.html' %}
    {% load static %}
    
    
    {% block content %}
      <h2>DETAIL</h2>
      <img src="{% static 'articles/tot.png' %}" alt="sample image">
      <h3>{{ article.pk }} 번째 글</h3>
      <img src="{% static 'article.images.url' %}" alt="{{ article.images }}">
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

    

17. **이미지 수정**

    ```html
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>UPDATE</h1>
      <form action="{% url 'articles:update' article.pk %}" method="POST" enctype='multipart/form-data'>
        {% csrf_token %}
        {{ form.as_p }}
        <button>수정</button>
      </form>
      <hr>
      <a href="{% url 'articles:index' %}">[back]</a>
    {% endblock content %}
    ```

    ```python
    @require_http_methods(['GET', 'POST'])
    def update(request, pk):
        article = get_object_or_404(Article, pk=pk)
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'articles/update.html', context)
    ```

    

18. Detail 이미지 접근

    ```html
    {% extends 'base.html' %}
    {% load static %}
    
    
    {% block content %}
      <h2>DETAIL</h2>
      <img src="{% static 'articles/tot.png' %}" alt="sample image">
      <h3>{{ article.pk }} 번째 글</h3>
      {% if article.image %}
        <img src="{% static 'article.images.url' %}" alt="{{ article.images }}">
      {% else %}
        <img src="{% static 'images/son.jpg' %}" alt="default image">
      {% endif %}
        
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



19. **upload_to argument 심화**

    ```python
    # articles/models.py
    
    from django.db import models
    
    def articles_image_path(instance, filename):
        return f'user_{instance.pk}/{filename}'
    
    # Create your models here.
    class Article(models.Model):
        title = models.CharField(max_length=10)
        content = models.TextField()
        # image = models.ImageField(upload_to='%Y/%m/%d/', blank=True)
        # image = models.ImageField(upload_to='images/', blank=True)
        image = models.ImageField(upload_to=articles_image_path, blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    
        def __str__(self):
            return self.title
    ```

    

20. **이미지 크기 변경하기**

    * 실제 원본 이미지를 서버에 그대로 업로드하는 것은 서버의 부담이 큰 작업

    * 업로드가 될 때 이미지 자체를 리사이징

      ```bash
      $ pip install django-imagekit
      # settings.py에서 등록 필요
      ```



21. 이미지 크기 변경(썸네일 활용)

    ```python
    from django.db import models
    from imagekit.models import ProcessedImageField, ImageSpecField
    from imagekit.processors import ResizeToFill
    
    def articles_image_path(instance, filename):
        return f'user_{instance.pk}/{filename}'
    
    # Create your models here.
    class Article(models.Model):
        title = models.CharField(max_length=10)
        content = models.TextField()
        # image = models.ImageField(upload_to='%Y/%m/%d/', blank=True)
        # image = models.ImageField(upload_to='images/', blank=True)
        # image = models.ImageField(upload_to=articles_image_path, blank=True)
        # image = ProcessedImageField(
        #     upload_to='thumbnails/',
        #     processors=[ResizeToFill(100, 50)],
        #     format='JPEG',
        #     options={'quality': 60})
        image = models.ImageField(upload_to='origins/')
        image_thumbnail = ImageSpecField(
            source='image',
            processors=[ResizeToFill(100, 50)],
            format='JPEG',
            options={'quality': 90})
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    
        def __str__(self):
            return self.title
    ```

    ```html
    {% extends 'base.html' %}
    {% load static %}
    
    
    {% block content %}
      <h2>DETAIL</h2>
      <img src="{% static 'articles/tot.png' %}" alt="sample image">
      <h3>{{ article.pk }} 번째 글</h3>
      {% if article.image %}
        <img src="{% static 'article.image_thumbnail.url' %}" alt="{{ article.image_thumbnail }}">
      {% else %}
        <img src="{% static 'images/son.jpg' %}" alt="default image">
      {% endif %}
        
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

    

