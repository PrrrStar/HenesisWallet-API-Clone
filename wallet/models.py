from django.db import models


class AccountKey(models.Model):
    address                 = models.CharField(max_length=255, verbose_name='Account Key 주소')
    pub                     = models.CharField(max_length=255, verbose_name='Key의 Public Key')
    keyFile                 = models.CharField(max_length=255, verbose_name='마스터지갑 비밀번호로 암호화된 Private Key')

class HenesisKey(models.Model):
    address                 = models.CharField(max_length=255, verbose_name='Henesis Key 주소')


class MasterWallet(models.Model):
    masterWalletId          = models.CharField(max_length=255, verbose_name='마스터지갑 ID')
    name                    = models.CharField(max_length=255, verbose_name='지갑 이름')
    address                 = models.CharField(max_length=255, verbose_name='지갑 주소')
    blockchain              = models.CharField(max_length=255, verbose_name='블록체인 타입')
    createdAt               = models.CharField(max_length=255, verbose_name='지갑 생성 시간(ms)')
    updatedAt               = models.CharField(max_length=255, verbose_name='지갑 정보 수정 시간(ms)')
    status                  = models.CharField(max_length=255, verbose_name='지갑 상태')
    error                   = models.CharField(max_length=255, verbose_name='지갑 생설 실패 시 발생 에러')
    encryptionKey           = models.CharField(max_length=255, verbose_name='암호 키')
    whitelistActivated      = models.BooleanField(verbose_name='출금 주소 화이트리스팅 활성화 유무')
    version                 = models.CharField(max_length= 255, verbose_name='컨트렉트 버전')

    accountKeyId            = models.ForeignKey(AccountKey, on_delete=models.CASCADE, verbose_name='Henesis Wallet의 Account Key', db_column='accountKeyId')
    transcationId           = models.ForeignKey('Transaction', on_delete=models.CASCADE, verbose_name='지갑 생성 트랜잭션의 ID', db_column='transactionId')

    class Meta:
        ordering            = ['-createdAt']
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
    createdAt               = models.DateTimeField(auto_now_add=True, verbose_name='지갑 생성 시간(ms)')
    updatedAt               = models.DateTimeField(auto_now=True, verbose_name='지갑 정보 수정 시간(ms)')

    masterWalletId          = models.ForeignKey(MasterWallet, on_delete=models.CASCADE, verbose_name='마스터 지갑의 ID', db_column='masterWalletId')
    transcationId           = models.ForeignKey('Transaction', on_delete=models.CASCADE, verbose_name='지갑 생성 트랜잭션의 ID', db_column='transactionId')

    class Meta:
        ordering            = ['-createdAt']
        verbose_name        = 'user wallet'
        verbose_name_plural = 'user wallets'

    def get_absolute_url(self):
        pass

class Transaction(models.Model):
    transactionId           = models.CharField(max_length=255, verbose_name='트렌잭션 ID')
    blockchain              = models.CharField(max_length=255, verbose_name='블록체인 플랫폼')
    sender                  = models.CharField(max_length=255, verbose_name='Henesis Key의 주소')
    hash                    = models.CharField(max_length=255, verbose_name='트랜잭션 해시')
    error                   = models.CharField(max_length=255, verbose_name='트랜잭션 전송 시 발생한 에러')
    status                  = models.CharField(max_length=255, verbose_name='트래잭션 상태')#REQUESTED, PENDING, MINED, CONFIRMED, FAILED
    createdAt               = models.CharField(max_length=255, verbose_name='트랜잭션 생성 시간(ms)')
    updatedAt               = models.CharField(max_length=255, verbose_name='트랜잭션 변경 시간(ms)')

    keyId                   = models.ForeignKey(HenesisKey, on_delete=models.CASCADE, verbose_name='Henesis Key의 ID', db_column='keyId')
    signedMultiSigPayloadId = models.ForeignKey('SignedMultiSigPayload', on_delete=models.CASCADE, verbose_name='Account Key로 서명한 트랜잭션 Payload', db_column='signedMultiSigPayloadId')
    rawTransactionId        = models.ForeignKey('RawTransaction', on_delete=models.CASCADE, verbose_name='블록체인에 전파된 트랜잭션', db_column='rawTransactionId')

class SignedMultiSigPayload(models.Model):
    signature               = models.CharField(max_length=255, verbose_name='서명한 트랜잭션 Payload')

    multiSigPayloadId       = models.ForeignKey('MultiSigPayload', on_delete=models.CASCADE, verbose_name='Account Key로 서명한 트랜잭션 Payload', db_column='multiSigPayloadId')
    
class MultiSigPayload(models.Model):
    value                   = models.CharField(max_length=255, verbose_name='암호화폐의 양')
    walletAddress           = models.CharField(max_length=255, verbose_name='트랜잭션을 발생시킬 지갑의 주소')
    toAddress               = models.CharField(max_length=255, verbose_name='트랜잭션의 수신자')
    walletNonce             = models.CharField(max_length=255, verbose_name='트랜잭션을 발생시킬 지갑의 nonce') 
    hexData                 = models.CharField(max_length=255, verbose_name='트랜잭션에 담긴 데이터')

class RawTransaction(models.Model):
    nonce                   = models.CharField(max_length=255, verbose_name='트랜잭션 발신의 nonce')
    to                      = models.CharField(max_length=255, verbose_name='트랜잭션 수신자')
    value                   = models.CharField(max_length=255, verbose_name='트랜잭션에 담긴 암호화폐의 양')
    data                    = models.CharField(max_length=255, verbose_name='트래잭션에 담긴 데이터')
    gasPrice                = models.CharField(max_length=255, verbose_name='트랜잭션의 gas price(단위:wei')
    gasLimit                = models.CharField(max_length=255, verbose_name='트랜잭션의 gas limit(단위:wei)')


class Coin(models.Model):
    name                    = models.CharField(max_length=255, verbose_name='암호화폐 이름')
    symbol                  = models.CharField(max_length=255, verbose_name='암호화폐 기호')
    address                 = models.CharField(max_length=255, verbose_name='암호화폐 주소')
    desc                    = models.CharField(max_length=255, verbose_name='암호화폐 설명')
    blockchain              = models.CharField(max_length=255, verbose_name='암호화폐가 발행된 블록체인 플랫폼')
    attributes              = models.CharField(max_length=255, verbose_name='암호화폐의 메타 데이터')

class Balance(models.Model):
    coinType                = models.CharField(max_length=255, verbose_name='암호화폐 타입')
    amount                  = models.CharField(max_length=255, verbose_name='확정된 잔액 ')
    spendableAmount         = models.CharField(max_length=255, verbose_name='출금 가능한 잔액')
    name                    = models.CharField(max_length=255, verbose_name='암호화폐 이름')
    coinType                = models.CharField(max_length=255, verbose_name='암호화폐 타입')
    symbol                  = models.CharField(max_length=255, verbose_name='암호화폐 심볼, ticker')
    
    coinId                  = models.ForeignKey(Coin, on_delete=models.CASCADE, verbose_name='Coin의 ID', db_column='coinId')
    masterWalletId          = models.ForeignKey(MasterWallet, on_delete=models.CASCADE, verbose_name='마스터 지갑의 ID', db_column='masterWalletId')
    userWalletId            = models.ForeignKey(UserWallet, on_delete=models.CASCADE, verbose_name='사용자 지갑의 ID', db_column='userWalletId')

class Nonce(models.Model):
    nonce                   = models.CharField(max_length=255)

    masterWalletId          = models.ForeignKey(MasterWallet, on_delete=models.CASCADE, verbose_name='마스터 지갑의 ID', db_column='masterWalletId')
    userWalletId            = models.ForeignKey(UserWallet, on_delete=models.CASCADE, verbose_name='사용자 지갑의 ID', db_column='userWalletId')

class ValueTransferEvents(models.Model):
    fromAddr                = models.CharField(max_length=255, verbose_name='출금 주소')
    toAddr                  = models.CharField(max_length=255, verbose_name='입금 주소')
    amount                  = models.CharField(max_length=255, verbose_name='암호화폐 양')
    status                  = models.CharField(max_length=255, verbose_name='트랜잭션 상태')
    orgId                   = models.CharField(max_length=255, verbose_name='지갑이 속한 팀 ID')
    coinSymbol              = models.CharField(max_length=255, verbose_name='암호화폐 기호')
    transferType            = models.CharField(max_length=255, verbose_name='입출금 타입')
    confirmation            = models.CharField(max_length=255, verbose_name='블록 컨펌 수')
    transactionHash         = models.CharField(max_length=255, verbose_name='트랜잭션 해시')
    createdAt               = models.CharField(max_length=255, verbose_name='트랜잭션 생성 시간(ms)')
    updatedAt               = models.CharField(max_length=255, verbose_name='트랜잭션 변경 시간(ms)')
    walletName              = models.CharField(max_length=255, verbose_name='해당 내역의 지갑 이름')
    walletType              = models.CharField(max_length=255, verbose_name='해당 내역의 지갑 종류')

    masterWalletId          = models.ForeignKey(MasterWallet, on_delete=models.CASCADE, verbose_name='마스터 지갑의 ID', db_column='masterWalletId')
    walletId                = models.ForeignKey(UserWallet, on_delete=models.CASCADE, verbose_name='사용자 지갑의 ID', db_column='userWalletId')
    transcationId           = models.ForeignKey(Transaction, on_delete=models.CASCADE, verbose_name='지갑 생성 트랜잭션의 ID', db_column='transactionId')

class CallEvents(models.Model):
    status                  = models.CharField(max_length=255, verbose_name='트랜잭션 상태')
    orgId                   = models.CharField(max_length=255, verbose_name='지갑이 속한 팀 ID')
    toAddress               = models.CharField(max_length=255, verbose_name='호출한 스마트 컨트랙트 주소')
    confirmation            = models.CharField(max_length=255, verbose_name='블록 컨펌 수')
    transactionHash         = models.CharField(max_length=255, verbose_name='트랜잭션 해시')
    createdAt               = models.CharField(max_length=255, verbose_name='트랜잭션 생성 시간(ms)')
    updatedAt               = models.CharField(max_length=255, verbose_name='트랜잭션 변경 시간(ms)')

    masterWalletId          = models.ForeignKey(MasterWallet, on_delete=models.CASCADE, verbose_name='마스터 지갑의 ID', db_column='masterWalletId')
    walletId                = models.ForeignKey(UserWallet, on_delete=models.CASCADE, verbose_name='사용자 지갑의 ID', db_column='userWalletId')
    transcationId           = models.ForeignKey(Transaction, on_delete=models.CASCADE, verbose_name='지갑 생성 트랜잭션의 ID', db_column='transactionId')
