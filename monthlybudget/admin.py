from django.contrib import admin

from monthlybudget.models import Transactions

class Trans_Detail(admin.ModelAdmin):
    list_display = ('id','date','description','category','amount',)
    search_fields =('id',)
# Register your models here.
admin.site.register(Transactions,Trans_Detail)