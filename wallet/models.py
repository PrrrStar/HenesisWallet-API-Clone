from django.db import models


class AccountKey(models.Model):
    address                 = models.CharField(max_length=255, verbose_name='Key 주소')
    pub                     = models.CharField(max_length=255, verbose_name='Key의 Public Key')
    keyFile                 = models.CharField(max_length=255, verbose_name='마스터 직바 비밀번호로 암호화된 Private Key')

class MasterWallet(models.Model):
    masterWalletId          = models.CharField(max_length=255, verbose_name='마스터지갑 ID')
    name                    = models.CharField(max_length=255, verbose_name='지갑 이름')
    address                 = models.CharField(max_length=255, verbose_name='지갑 주소')
    blockchain              = models.CharField(max_length=255, verbose_name='블록체인 타입')
    transcationId           = models.CharField(max_length=255, verbose_name='지갑 생성 트랜잭션의 ID')

    created_at              = models.CharField(max_length=255, verbose_name='지갑 생성 시간(ms)')
    modified_at             = models.CharField(max_length=255, verbose_name='지갑 정보 수정 시간(ms)')

    status                  = models.CharField(max_length=255, verbose_name='지갑 상태')
    error                   = models.CharField(max_length=255, verbose_name='지갑 생설 실패 시 발생 에러')
    encryptionKey           = models.CharField(max_length=255, verbose_name='암호 키')
    whitelistActivated      = models.BooleanField(verbose_name='출금 주소 화이트리스팅 활성화 유무')
    version                 = models.CharField(max_length= 255, verbose_name='컨트렉트 버전')

    class Meta:
        ordering            = ['-created_at']
        verbose_name        = 'master wallet'
        verbose_name_plural = 'master wallets'

    def get_absolute_url(self):
        pass

class UserWallet(models.Model):
    userWalletId            = models.CharField(max_length=255, verbose_name='사용자지갑 ID')
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
    id                      = models.CharField(max_length=255, verbose_name='트렌잭션 ID')
    blockchain              = models.CharField(max_length=255, verbose_name='블록체인 플랫폼')
    sender                  = models.CharField(max_length=255, verbose_name='Henesis Key의 주소')
    hash                    = models.CharField(max_length=255, verbose_name='트랜잭션 해시')
    error                   = models.CharField(max_length=255, verbose_name='트랜잭션 전송 시 발생한 에러')
    status                  = models.CharField(max_length=255, verbose_name='트래잭션 상태')#REQUESTED, PENDING, MINED, CONFIRMED, FAILED
    keyId                   = models.ForeignKey
    created_at              = models.CharField(max_length=255, verbose_name='트랜잭션 생성 시간(ms)')
    modified_at             = models.CharField(max_length=255, verbose_name='트랜잭션 변경 시간(ms)')

    userWallet              = models.ForeignKey(max_length=255, on_delete=models.CASCADE, related_name='transaction')

class RawTransaction(models.Model):
    nonce                   = models.CharField(max_length=255, verbose_name='트랜잭션 발신의 nonce')
    to                      = models.CharField(max_length=255, verbose_name='트랜잭션 수신자')
    value                   = models.CharField(max_length=255, verbose_name='트랜잭션에 담긴 암호화폐의 양')
    data                    = models.CharField(max_length=255, verbose_name='트래잭션에 담긴 데이터')
    gasPrice                = models.CharField(max_length=255, verbose_name='트랜잭션의 gas price(단위:wei')
    gasLimit                = models.CharField(max_length=255, verbose_name='트랜잭션의 gas limit(단위:wei)')

class SignedMultiPayload(models.Model):
    signature               = models.CharField(max_length=255, verbose_name='서명한 트랜잭션 Payload')
    multiSigPayload         = models.CharField(max_length=255, verbose_name='서명하기 이전의 트랜잭션 Payload')

class MultiSigPayload(models.Model):
    value                   = models.CharField(max_length=255, verbose_name='암호화폐의 양')
    walletAddress           = models.CharField(max_length=255, verbose_name='트랜잭션을 발생시킬 지갑의 주소')
    toAddress               = models.CharField(max_length=255, verbose_name='트랜잭션의 수신자')
    walletNonce             = models.CharField(max_length=255, verbose_name='트랜잭션을 발생시킬 지갑의 nonce') 
    hexData                 = models.CharField(max_length=255, verbose_name='트랜잭션에 담긴 데이터')

class Coin(models.Model):
    name                    = models.CharField(max_length=255)
    symbol                  = models.CharField(max_length=255)
    address                 = models.CharField(max_length=255)
    desc                    = models.CharField(max_length=255)
    blockchain              = models.CharField(max_length=255)
    attributes              = models.CharField(max_length=255)

    