from django.urls import path
from main.views import add_product_ajax, create_product_flutter, get_product_json, show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user, delete, increment, decrement, edit

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete/<int:id>', delete, name='delete'),
    path('increment/<int:id>', increment, name='increment'),
    path('decrement/<int:id>', decrement, name='increment'),
    path('edit/<int:id>', edit, name='edit'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]