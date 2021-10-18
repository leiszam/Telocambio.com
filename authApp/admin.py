from django.contrib import admin
from .models.user import User
from .models.profile import Profile
from .models.product import Product
from .models.exchange import Exchange
from .models.favorite import Favorite

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Exchange)
admin.site.register(Favorite)
