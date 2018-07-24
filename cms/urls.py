from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    # 書籍
    path('book/', views.book.list, name='book/list'),   # 一覧
    path('book/add/', views.book.edit, name='book/add'),  # 登録
    path('book/mod/<int:book_id>/', views.book.edit, name='book/mod'),  # 修正
    path('book/del/<int:book_id>/', views.book.delete, name='book/del'),   # 削除

    # 感想
    path('impression/<int:book_id>/', views.impression.ImpressionList.as_view(), name='impression/list'),  # 一覧
    path('impression/add/<int:book_id>/', views.impression.edit, name='impression/add'),        # 登録
    path('impression/mod/<int:book_id>/<int:impression_id>/', views.impression.edit, name='impression/mod'),  # 修正
    path('impression/del/<int:book_id>/<int:impression_id>/', views.impression.delete, name='impression/del'),   # 削除
]
