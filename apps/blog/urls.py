from django.urls import path
from . import views

app_name = "blog"

# urlpatterns = [
#     path('', views.posts, name = "posts"),
#     # path('add/', views.addArticle, name = "add"),
#     # path('<int:id>/', views.detail, name = "detail"),
#     # path('update/<int:id>', views.updateArticle, name = "update"),
#     # path('delete/<int:id>', views.deleteArticle, name = "delete"),
#     # path('comment/<int:id>', views.addComment, name = "comment"),
# ]

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    # path('blog/', views.PostList.as_view(), name='post_list'),
    # path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # path('categoria/<int:pk>/', views.CategoriaListView.as_view(), name='categoria_list'),
    # path('producto/<int:pk>/', views.ProductoDetail.as_view(), name='producto_detail'),
    # path('service/<int:pk>/', views.ServiceDetail.as_view(), name='service_detail'),

    # path('producto/busqueda/', views.BusquedaListView.as_view(), name='producto_search'),
]