from django.urls import path
from main.views import report_list

app_name = 'main'

urlpatterns = [
    path('report-list', report_list, name='report_list'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mood_tracking/', include('mood_tracking.urls')),
    # Include other app URLs here as needed
]
