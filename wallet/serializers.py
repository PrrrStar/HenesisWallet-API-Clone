
from .models import *

from rest_framework import serializers

class MasterWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model   = MasterWallet
        fields  = '__all__'

class MasterWalletNameSerializer(serializers.ModelSerializer):
    class Meta:
        model   = MasterWallet
        fields  = ('name',)

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Balance
        fields  = '__all__'

class NonceSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Nonce
        fields  = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    signedMultiSigPayload = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='마스터 지갑에서 코인/토큰 전송하기',
        lookup_field = 'masterWalletId'
    )
    class Meta:
        model   = Transaction
        fields  = ['transactionId','blockchain','sender','hash','error','status','createdAt','updatedAt','signedMultiSigPayload',]


class SignedMultiSigPayloadSerializer(serializers.ModelSerializer):
    class Meta:
        model   = SignedMultiSigPayload
        fields  = '__all__'

class MultiSigPayloadSerializer(serializers.ModelSerializer):
    class Meta:
        model   = MultiSigPayload
        fields  = '__all__'

class RawTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model   = RawTransaction
        fields  = '__all__'