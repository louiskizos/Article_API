from django.urls import path
from .views import *





urlpatterns = [
    
    path('', ArticleListAPIView.as_view()),
    path('Insert-Article/', ArticleMixView.as_view()),
    path('Insert-Agent/', AgentMixView.as_view()),
    path('All-Agent/', AgentListAPIView.as_view()),
    path('All-New/', NewListAPIView.as_view()),
    path('Insert-New/', NewMixView.as_view()),
    path('Login/', LoginView.as_view()),
    
] 