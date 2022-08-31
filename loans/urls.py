from rest_framework import routers
from loans.views import LoanViewset

router = routers.DefaultRouter()

router.register(r'loans', LoanViewset)
