from django.conf.urls import url
from .views import CompanyList, GetMainoksiaForCompany

urlpatterns = [
    url(r"^company-list/", CompanyList.as_view(), name='company-list'),
    url(r"^mainoksia-list/(?P<company_id>.+)/$",
        GetMainoksiaForCompany.as_view(), name="mainoksia-list"),
]
