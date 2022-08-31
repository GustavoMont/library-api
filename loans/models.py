from datetime import datetime
from django.db import models
from book.models import Book
from users.models import User
from utils.time import calculate_return_date

# Create your models here.
class Loan(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now=True)
    return_date = models.DateField(default=calculate_return_date())
    returned_at = models.DateField(null=True, blank=True)
    returned = models.BooleanField(default=False)

    @property
    def is_late_returned(self):
        if self.returned_at == None:
            return False
        return self.returned_at > self.return_date

    @property
    def slug(self):
        return f'{self.__str__()}'

    @property
    def is_late(self):
        return datetime.today() > self.return_date

    def __str__(self):
        return f'{self.user}/{self.book}/{self.return_date}'