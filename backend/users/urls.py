from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

from .views import ( RegisterUser,
                    UpdateUser,
                    CustomAuthToken,
                    UpdateProfile,
                    )


urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('logout/', csrf_exempt(auth_views.LogoutView.as_view(next_page='/',
                                template_name= None)), name='logout'),
    path('update/<int:pk>/', UpdateProfile.as_view()),
    path('delete/<int:pk>/', UpdateUser.as_view()),
]