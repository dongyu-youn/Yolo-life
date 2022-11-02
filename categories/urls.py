from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.CategoryViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "<int:pk>",
        views.CategoryViewSet.as_view(
            {
                "get": "retrieve", 
                # 전체에서 한개를 주는 메소드
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]