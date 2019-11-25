from web3 import Web3, IPCProvider
from vyper import compile_codes

contract_source_code = '''
name: public(bytes[24])

@public
def __init__():
    self.name = "Satoshi Nakamoto"

@public
def change_name(new_name: bytes[24]):
    self.name = new_name

@public
def say_hello() -> bytes[32]:
    hello: bytes[7] = "Hello, "
    return concat(hello, self.name)

'''

smart_contract = {}
smart_contract['hello'] = contract_source_code

format = ['abi','bytecode']
compiled_code = compile_codes(smart_contract, format,'dict')

abi = compiled_code['hello']['abi']
bytecode = compiled_code['hello']['bytecode']

w3 = Web3(IPCProvider('/home/slavnic/.ethereum/rinkeby/geth.ipc'))

from web3.middleware import geth_poa_middleware
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

w3.eth.defaultAccount = w3.toChecksumAddress("0x4b9c55f40d1dccc01d2a8fc778855ccc4d185137")
password = 'password123'
contract_address = "0x5142D109ded7dd68fa462f6679798075F7c9A0ac"
address = w3.toChecksumAddress(contract_address)

with open('/home/slavnic/.ethereum/rinkeby/keystore/UTC--2019-10-12T17-07-17.673753784Z--4b9c55f40d1dccc01d2a8fc778855ccc4d185137') as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(encrypted_key, password)


Hello = w3.eth.contract(address = address, abi=abi)

print(Hello.functions.name().call())
print(Hello.functions.say_hello().call())

nonce = w3.eth.getTransactionCount(w3.eth.defaultAccount)

txn = Hello.functions.change_name(b"Lionel Messi").buildTransaction({
    'gas': 500000,
    'gasPrice': w3.toWei('30','gwei'),
    'nonce': nonce
})

signed_txn = w3.eth.account.signTransaction(txn, private_key = private_key)
signed_txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
w3.eth.waitForTransactionReceipt(signed_txn_hash)

print(Hello.functions.say_hello().call())
