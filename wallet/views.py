from django.shortcuts import render

from .serializers import *
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import (generics, authentication, permissions, filters,)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):

        return Response({
            'master-wallet': reverse(MasterWalletList.name, request=request),
        })
class MasterWalletList(generics.ListAPIView):
    queryset            = MasterWallet.objects.all()
    serializer_class    = MasterWalletSerializer
    name                = '마스터 지갑 목록 조회하기'

class MasterWalletDetail(generics.RetrieveAPIView):
    queryset            = MasterWallet.objects.all()
    serializer_class    = MasterWalletSerializer
    lookup_field        = 'masterWalletId'
    name                = '마스터 지갑 정보 조회하기'

class MasterWalletBalance(generics.RetrieveAPIView):
    queryset            = Balance.objects.all()
    serializers         = BalanceSerializer
    lookup_field        = 'masterWalletId'
    name                = '마스터 지갑 잔고 조회하기'

class MasterWalletNonce(generics.RetrieveAPIView):
    queryset            = Nonce.objects.all()
    serializers         = NonceSerializer
    lookup_field        = 'masterWalletId'
    name                = '마스터 지갑 논스 조회하기'

class MasterWalletUpdate(generics.UpdateAPIView):
    queryset            = MasterWallet.objects.all()
    serializer_class    = MasterWalletSerializer
    lookup_field        = 'masterWalletId'
    name                = '마스터 지갑 이름 변경하기'

class MasterWalletNameUpdate(generics.UpdateAPIView):
    queryset            = MasterWallet.objects.all()
    serializer_class    = MasterWalletNameSerializer
    lookup_field        = 'masterWalletId'
    name                = '마스터 지갑 비밀번호 변경하기'

class MasterWalletUpdatePassphraseUpdate(generics.UpdateAPIView):
    queryset            = MasterWallet.objects.all()
    serializer_class    = MasterWalletSerializer
    lookup_field        = 'masterWalletId'
    name                = '마스터 지갑 이름 변경하기'

class MasterWalletTransfer(generics.RetrieveUpdateDestroyAPIView):
    queryset            = Transaction.objects.all()
    serializer_class    = TransactionSerializer
    lookup_field        = 'masterWalletId'
    name                = '마스터 지갑에서 코인/토큰 전송하기'

class MasterWalletContractCall(generics.RetrieveUpdateDestroyAPIView):
    queryset            = Transaction.objects.all()
    serializer_class    = TransactionSerializer
    lookup_field        = 'masterWalletId'
    name                = '마스터 지갑에서 스마트 컨트랙트 호출하기'

class MasterWalletFlush(generics.RetrieveAPIView):
    queryset            = Transaction.objects.all()
    serializer_class    = TransactionSerializer
    lookup_field        = 'masterWalletId'
    name                = '사용자 지갑 잔액을 모두 끌어오기'

class MasterWalletFlush(generics.RetrieveUpdateDestroyAPIView):
    queryset            = Transaction.objects.all()
    serializer_class    = TransactionSerializer
    lookup_field        = 'masterWalletId'
    name                = '사용자 지갑 잔액을 모두 끌어오기'
