from django.urls import path
from .views import project_list
from .views import ProjectCreateView, ProjectEditView, ProjectDeleteView

urlpatterns =[
        path('', project_list, name='portfolio_list'),
        path('add_portfolio/', ProjectCreateView.as_view(), name='add_portfolio'),
        path('edit_project/<int:pk>/', ProjectEditView.as_view(), name='edit_project'),
        path('delete_project/<int:pk>/', ProjectDeleteView.as_view(), name='delete_project'),

    ]
