from web3 import Web3, IPCProvider
from web3.middleware import geth_poa_middleware

w3 = Web3(IPCProvider('/home/slavnic/.ethereum/rinkeby/geth.ipc'))

w3.middleware_onion.inject(geth_poa_middleware, layer=0)

password = 'password123'
from_account = '0x4b9c55f40d1dccc01d2a8fc778855ccc4d185137'
to_account = '0x1af095e784338245d90eeaba689b7c1e5eed56ea'
with open('/home/slavnic/.ethereum/rinkeby/keystore/UTC--2019-10-12T17-07-17.673753784Z--4b9c55f40d1dccc01d2a8fc778855ccc4d185137') as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(encrypted_key, password)

nonce = w3.eth.getTransactionCount(Web3.toChecksumAddress(from_account))

transaction = {
    'to' : Web3.toChecksumAddress(to_account),
    'value' : w3.toWei('1', 'ether'), 
    'gas' : 21000,
    'gasPrice': w3.toWei('2', 'gwei'),
    'nonce' : nonce
}

signed = w3.eth.account.signTransaction(transaction, private_key)
w3.eth.sendRawTransaction(signed.rawTransaction)

