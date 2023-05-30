from django.urls import path,include,re_path
#
from .views import CheckView,ResultView,XresultView,DetailView,XSaveView,XChackesView

urlpatterns = [
    path('', CheckView,name='shcheck'),
    path('result/', ResultView,name='result'),
    path('xresult/', XresultView,name='xresult'),
    path('detail/',DetailView,name='detail'),
    path('detailsave/',XSaveView,name='detailsave'),
    path('detailchacks/',XChackesView,name='detailchacks'),
]
