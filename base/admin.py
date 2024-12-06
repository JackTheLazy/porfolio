from django.contrib import admin


from .models import Whatiknow
from .models import Contact
from .models import Address
from .models import Email
from .models import Education



class WhatiknowAdmin(admin.ModelAdmin):
    Whatiknow=('whatIKnow')
admin.site.register(Whatiknow,WhatiknowAdmin)

class ContactAdmin(admin.ModelAdmin):
    contact=('contact')
admin.site.register(Contact,ContactAdmin)

class AddressAdmin(admin.ModelAdmin):
    address=('address')
admin.site.register(Address,AddressAdmin)

class EmailAdmin(admin.ModelAdmin):
    email=('email')
admin.site.register(Email,EmailAdmin)

class Educationdmin(admin.ModelAdmin):
    education=('education')
admin.site.register(Education,Educationdmin)