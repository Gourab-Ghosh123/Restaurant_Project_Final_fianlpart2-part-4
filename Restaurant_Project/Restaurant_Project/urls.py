from django.contrib import admin
from django.urls import path
from Base_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', Index, name='Index'),  # ✅ matches {% url 'Index' %}
    path('book_table/', Book_TableView, name='Book_Table'),  # ✅ matches {% url 'Book_Table' %}
    path('about/', AboutView, name='About'),                # ✅ matches {% url 'About' %}
    path('menu/', MenuView, name='Menu'),                   # ✅ matches {% url 'Menu' %}
    path('feedback/', FeedbackFormView, name='Feedback_Form'),  # ✅ matches {% url 'Feedback_Form' %}
    path('checkout/', CheckoutView, name='checkout'),       # ✅ matches {% url 'checkout' %}
    path('login/', LoginView, name='login'),                # ✅ matches {% url 'login' %}
    path('logout/', LogoutView, name='logout'),             # ✅ matches {% url 'logout' %}
    path('get-cart-items/', GetCartItemsView, name='get_cart_items'),  # JS fetch URL
    path('add-to-cart/', AddToCartView, name='add_to_cart'),            # JS POST URL
]

# ✅ Static and media config (if you're using DEBUG mode)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
