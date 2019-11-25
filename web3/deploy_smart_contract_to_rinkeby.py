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

format = ['abi', 'bytecode']
compiled_code = compile_codes(smart_contract, format, 'dict')

bytecode = compiled_code['hello']['bytecode']
abi = compiled_code['hello']['abi']

w3 = Web3(IPCProvider('/home/slavnic/.ethereum/rinkeby/geth.ipc'))

HelloSmartContract = w3.eth.contract(abi=abi, bytecode=bytecode)

from_account = "0x4b9c55f40d1dccc01d2a8fc778855ccc4d185137"
password = 'password123'
with open('/home/slavnic/.ethereum/rinkeby/keystore/UTC--2019-10-12T17-07-17.673753784Z--4b9c55f40d1dccc01d2a8fc778855ccc4d185137') as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(encrypted_key, password)

nonce = w3.eth.getTransactionCount(Web3.toChecksumAddress(from_account))

transaction = HelloSmartContract.constructor().buildTransaction({'from': Web3.toChecksumAddress(from_account),
                                                                 'gas': 500000,
                                                                 'gasPrice': w3.toWei('30', 'gwei'),
                                                                 'nonce': nonce})

signed = w3.eth.account.signTransaction(transaction, private_key)
tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)

tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print(tx_receipt)

