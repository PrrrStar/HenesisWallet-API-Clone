from django.urls import path, include
from .views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('wallets', MasterWalletList.as_view(), name=MasterWalletList.name),
    path('wallets/<masterWalletId>', MasterWalletDetail.as_view(), name=MasterWalletDetail.name),
    path('wallets/<masterWalletId>/balance', MasterWalletBalance.as_view(), name=MasterWalletBalance.name),
    path('wallets/<masterWalletId>/nonce', MasterWalletNonce.as_view(), name=MasterWalletNonce.name),
    path('wallets/<masterWalletId>/name', MasterWalletNameUpdate.as_view(), name=MasterWalletNameUpdate.name),
    path('wallets/<masterWalletId>/passphrase', MasterWalletUpdatePassphraseUpdate.as_view(), name=MasterWalletUpdatePassphraseUpdate.name),
    path('wallets/<masterWalletId>/transfer', MasterWalletTransfer.as_view(), name=MasterWalletTransfer.name),
    
]