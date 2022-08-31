from datetime import datetime
from book.models import Book
from loans.admin import Loans
from loans.models import Loan
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from rest_framework.exceptions import ParseError

from users.models import User

@receiver(pre_save, sender=Loan)
def return_loan(sender, instance, **kwargs):
    book = Book.objects.get(pk=instance.book.id)
    if instance.returned and instance.returned_at == None:
        instance.returned_at = datetime.today()
        book.quantity += 1
        book.save()

@receiver(post_save, sender=Loan)
def create_loan(sender, instance, created, **kwargs):
    book = Book.objects.get(pk=instance.book.id)
    user = User.objects.get(pk=instance.user.id)
    if book.quantity == 0 or not book.available:
        raise ParseError('Livro não disponível para empréstimo')
    if not user.can_borrow:
        raise ParseError('Usuário penalizado')
    if created:
        book.quantity -= 1
        book.save()