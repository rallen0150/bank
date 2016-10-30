from django.conf.urls import url, include
from django.contrib import admin

from bank.views import IndexView, UserCreateView, BalanceCreateView, TransactionDetailView, \
                       TransferCreateView
from bank_api.views import BalanceListCreateAPIView, BalanceDetailUpdateDestroyAPIView

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^obtain-token/$', obtain_auth_token),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^balance/create/$', BalanceCreateView.as_view(), name="balance_create_view"),
    url(r'^account/(?P<pk>\d+)/$', TransactionDetailView.as_view(), name="transaction_detail_view"),
    url(r'^transfer/create/$', TransferCreateView.as_view(), name="transfer_create_view"),
    url(r'^balance/$', BalanceListCreateAPIView.as_view(), name="balance_list_create_api_view"),
    url(r'^balance/(?P<pk>\d+)/$', BalanceDetailUpdateDestroyAPIView.as_view(), name="balance_detail_update_destroy_api_view"),

]
