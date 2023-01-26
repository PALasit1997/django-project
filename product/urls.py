from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    # path('polls/', views.index, name='index'),
    # # the 'name' value as called by the {% url %} template tag
    # path('<int:question_id>/', views.detail, name='detail'),
    # # path('specifics/<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('polls/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/details/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
]


