from django.contrib import admin

from .models import *

@admin.register(MasterWallet)
class MasterWalletAdmin(admin.ModelAdmin):
    pass

@admin.register(UserWallet)
class UserWalletAdmin(admin.ModelAdmin):
    pass

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass

@admin.register(SignedMultiSigPayload)
class SignedMultiSigPayloadAdmin(admin.ModelAdmin):
    pass

@admin.register(MultiSigPayload)
class MultiSigPayloadAdmin(admin.ModelAdmin):
    pass

@admin.register(RawTransaction)
class RawTransactionAdmin(admin.ModelAdmin):
    pass

@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    pass

@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    pass

@admin.register(Nonce)
class NonceAdmin(admin.ModelAdmin):
    pass

@admin.register(HenesisKey)
class HenesisKeyAdmin(admin.ModelAdmin):
    pass

@admin.register(AccountKey)
class AccountKeyAdmin(admin.ModelAdmin):
    pass

@admin.register(ValueTransferEvents)
class ValueTransferEventsAdmin(admin.ModelAdmin):
    pass

@admin.register(CallEvents)
class CallEventsAdmin(admin.ModelAdmin):
    pass


