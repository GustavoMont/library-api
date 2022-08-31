from rest_framework import viewsets
from loans.models import Loan

from loans.serializer import LoanSerializer
from permissions.loans import LoansPermissions
from rest_framework.permissions import IsAuthenticated

class LoanViewset(viewsets.ModelViewSet):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()
    permission_classes = [IsAuthenticated,LoansPermissions]