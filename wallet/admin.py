from django.contrib import admin

from .models import MasterWallet

@admin.register(MasterWallet)
class MasterWalletAdmin(admin.ModelAdmin):
    list_display=()
