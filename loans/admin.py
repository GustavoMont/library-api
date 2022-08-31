from django.contrib import admin

from loans.models import Loan

# Register your models here.
class Loans(admin.ModelAdmin):
    list_display = ('id', 'slug', 'book', 'user', 'return_date', 'is_late_returned', 'returned_at')
    list_display_links  = ('id', 'slug')
    exclude = ('returned_at',)
    search_fields = ('book, user',)

admin.site.register(Loan, Loans)