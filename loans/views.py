from rest_framework import viewsets
from loans.models import Loan

from loans.serializer import LoanSerializer
from permissions.loans import LoansPermissions
from rest_framework.permissions import IsAuthenticated

class LoanViewset(viewsets.ModelViewSet):
    serializer_class = LoanSerializer
    # queryset = Loan.objects.all() 
    model = Loan
    permission_classes = [IsAuthenticated,LoansPermissions]

    def get_queryset(self):
        user_group = list(self.request.user.groups.values())[0]
        if 'ADMIN' in user_group['name']:
            return Loan.objects.all() 
        return Loan.objects.filter(user=self.request.user)