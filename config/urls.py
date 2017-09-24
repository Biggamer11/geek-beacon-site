from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^gaming/$', TemplateView.as_view(template_name='pages/gaming.html'), name='gaming'),
    url(r'^geeksabroad/$', TemplateView.as_view(template_name='pages/geeksabroad.html'), name='geeksabroad'),
    url(r'^squirrels/$', TemplateView.as_view(template_name='pages/squirrels.html'), name='squirrels'),
    url(r'^stream/$', TemplateView.as_view(template_name='pages/stream.html'), name='stream'),
    url(r'^survey/$', TemplateView.as_view(template_name='pages/survey.html'), name='survey'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('geek_beacon.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^content/', include('content.urls', namespace='content')),
    url(r'^credits/$', TemplateView.as_view(template_name='pages/credits.html'), name='credits'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
