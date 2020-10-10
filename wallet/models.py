from django.db import models

# Create your models here.

class Blockchain(models.Model):
    
    class Meta:
        

class MasterWallet(models.Model):
    masterWallet            = models.CharField(max_length=255, verbose_name='마스터지갑 ID', primary_key=True)
    name                    = models.CharField(max_length=255, verbose_name='지갑 이름')
    address                 = models.CharField(max_length=255, verbose_name='지갑 주소')
    blockchain              = models.CharField(max_length=255, verbose_name='블록체인 타입')
    transcationId           = models.CharField(max_length=255, verbose_name='지갑 생성 트랜잭션의 ID')

    created_at              = models.DateTimeField(auto_now_add=True, verbose_name='지갑 생성 시간(ms)')
    modified_at             = models.DateTimeField(auto_now=True, verbose_name='지갑 정보 수정 시간(ms)')

    status                  = models.CharField(max_length=255, verbose_name='지갑 상태')
    error                   = models.CharField(max_length=255, verbose_name='지갑 생설 실패 시 발생 에러')
    encryptionKey           = models.CharField(max_length=255, verbose_name='암호 키')
    whitelistActivated      = models.BooleanField(verbose_name='출금 주소 화이트리스팅 활성화 유무')
    version                 = models.CharField(max_length= 255, verbose_name='컨트렉트 버전')

    class Meta:
        ordering = ['-created_at']
        verbose_name        = 'master wallet'
        verbose_name_plural = 'master wallets'

    def get_absolute_url(self):
        pass

class UserWallet(models.Model):
    userWallet              = models.CharField(max_length=255, verbose_name='사용자지갑 ID', primary_key=True)
    name                    = models.CharField(max_length=255, verbose_name='지갑 이름')
    address                 = models.CharField(max_length=255, verbose_name='지갑 주소')
    blockchain              = models.CharField(max_length=255, verbose_name='블록체인 타입')
    status                  = models.CharField(max_length=255, verbose_name='지갑 상태')
    error                   = models.CharField(max_length=255, verbose_name='지갑 생설 실패 시 발생 에러', null=True)


    created_at              = models.DateTimeField(auto_now_add=True, verbose_name='지갑 생성 시간(ms)')
    modified_at             = models.DateTimeField(auto_now=True, verbose_name='지갑 정보 수정 시간(ms)')
    masterWallet            = models.ForeignKey(max_length=255, on_delete=models.CASCADE, related_name='userWallet')
    
    class Meta:
        ordering            = ['-created_at']
        verbose_name        = 'user wallet'
        verbose_name_plural = 'user wallets'

    def get_absolute_url(self):
        pass

class Transaction(models.Model):
    transaction             = models.CharField(max_length=255, verbose_name='트렌잭션 ID', primary_key=True)
    transactionHash         = models.CharField(max_length=255, verbose_name='트랜잭션 HASH')
    status#REQUESTED, PENDING, MINED, CONFIRMED, FAILED
    nonce
    to
    value
    data
    gasPrice
    gasLimit
    created_at              = models.DateTimeField(auto_now_add=True, verbose_name='트랜잭션 생성 시간(ms)')
    modified_at             = models.DateTimeField(auto_now=True, verbose_name='트랜잭션 변경 시간(ms)')

    userWallet              = models.ForeignKey(max_length=255, on_delete=models.CASCADE, related_name='transaction')
class Coin(models.Model):
    name                    = models.CharField(max_length=255)
    symbol                  = models.CharField(max_length=255)
    address                 = models.CharField(max_length=255)
    desc                    = models.CharField(max_length=255)
    blockchain              = models.CharField(max_length=255)
    attributes              = models.CharField(max_length=255)

    