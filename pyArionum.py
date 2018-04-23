#key generation is borked

from ecdsa import SigningKey,SECP256k1,VerifyingKey, BadSignatureError
import json
import random
import requests
import os

def privkey_generate():
    print ("generating keys")
    privkey_raw = SigningKey.generate(curve=SECP256k1)
    privkey=privkey_raw.to_pem().decode('utf-8')
    pubkey=privkey_raw.get_verifying_key().to_pem().decode('utf-8')

    print(privkey_raw,privkey,pubkey)



peers_raw = requests.get('http://api.arionum.com/peers.txt')
peers = peers_raw.text.split("\n")

peer = (random.choice(peers))
address = "5rA1edefZmziJsX8C6KGSvKveSfCEFgAJFk7ktkePzBeFNNJZMEfwW8Lv8Zw37ie5xmMD5EChpkXXzBDaQC5eCBS"
txid = "n5Je9cZJ9RanmMdb8fjKRYneeLRYf9dGsi74msSSz3n7brwcMAX8tPvXmD3ExXt1uwft74menqG381iUag3oADc"

getPendingBalance_raw = requests.get('{}/api.php?q=getPendingBalance&account={}'.format(peer,address))
getPendingBalance = json.loads(getPendingBalance_raw.text)
print (getPendingBalance)
print (getPendingBalance['data'])

getTransactions_raw = requests.get('{}/api.php?q=getTransactions&account={}'.format(peer,address))
getTransactions = json.loads(getTransactions_raw.text)
print (getTransactions)

currentBlock_raw = requests.get('{}/api.php?q=currentBlock&account={}'.format(peer,address))
currentBlock = json.loads(currentBlock_raw.text)
print (currentBlock)

getTransaction_raw = requests.get('{}/api.php?q=getTransaction&transaction={}'.format(peer,txid))
getTransaction = json.loads(getTransaction_raw.text)
print (getTransaction)


privkey_generate()

