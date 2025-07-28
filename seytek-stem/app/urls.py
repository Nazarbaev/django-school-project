from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (IndexView,
                    GalleryView,
                    BlogDetailsView,
                    CambridgeView,
                    EdupageView,
                    FaqView,
                 blog_index, achievements_index, stats_index)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("gallery/", GalleryView.as_view(), name="gallery"),
    path("blog/", blog_index, name="blog"),
    path('blog-details/<int:pk>/', BlogDetailsView.as_view(), name="blog-details"),
    path("cambridge/", CambridgeView.as_view(), name="cambridge"),
    path("edupage/", EdupageView.as_view(), name="edupage"),
    path("faq/", FaqView.as_view(), name="faq"),
    path("achievements/", achievements_index, name="achievements"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve media files in production (Render)
else:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]