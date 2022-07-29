from django.contrib import admin

from empapp.models import EmployeeUserAuth,Address,Person

admin.site.register(EmployeeUserAuth)
admin.site.register(Address)
admin.site.register(Person)



