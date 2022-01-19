from django.urls import path
from django.conf.urls.static import static
from blog import views as blog_views

app_name = 'blog'

urlpatterns = [
    path('', blog_views.render_posts, name='posts'),
    path('<int:post_id>', blog_views.post_detail, name='post_detail')
]