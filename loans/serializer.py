from rest_framework import serializers
from loans.models import Book

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'