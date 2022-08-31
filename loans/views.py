from rest_framework import viewsets
from loans.models import Loan

from loans.serializer import LoanSerializer

class LoanViewset(viewsets.ModelViewSet):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()