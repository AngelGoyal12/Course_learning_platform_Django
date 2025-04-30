from django.urls import path
from .views import register, user_login, user_logout, dashboard, profile_view, admin_dashboard, user_dashboard, accept_order, reject_order

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),  
    path('user_dashboard/', user_dashboard, name='user_dashboard'),  
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),  
    path('profile/', profile_view, name='profile'),
    
path('admin/accept-order/<int:order_id>/', accept_order, name='accept_order'),
path('admin/reject-order/<int:order_id>/', reject_order, name='reject_order'),
]