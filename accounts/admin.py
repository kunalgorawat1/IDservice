from django.contrib import admin
#from accounts.models import Userprofile   uncomment to get the old back
from accounts.models import Students, User  ##remove to get the old back
# Register your models here.
class UserPofileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info' )

    def user_info(self, obj):
        return obj.Description

#admin.site.register(Userprofile, UserPofileAdmin)    uncomment to get the old backends
admin.site.register(Students, UserPofileAdmin)    ##remove to get the old bca
admin.site.register(User)    ##remove to get the old bca
