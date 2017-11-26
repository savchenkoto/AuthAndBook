from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('bookshelf.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^',
        RedirectView.as_view(
            pattern_name='bookshelf:books',
            permanent=False
    ))
]