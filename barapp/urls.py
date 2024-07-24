from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order', views.order, name='order'),
        path('review', views.review, name='review'),
                path('addtoshop', views.AddTOBarberSHop, name='addtobarber'),
                path('AboutBarber', views.AboutBarber, name='AboutBarber'),

    path('orders/', views.order_list, name='orders'),
        path('profile/', views.profile, name='profile'),

                path('weeklyreport/', views.weekly_report, name='week'),

         path('allreviews/', views.review_list, name='allrev'),

    path('like/<int:review_id>/', views.toggle_like, name='toggle_like'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('login', views.log_in, name='login'),
    path('reg', views.reg, name='reg'),
    path('logout', views.log_out, name='logout'),
    path('delall', views.deleteall, name='delall'),
    path('completed_orders/', views.completed_order_list, name='completed_orders'),


]