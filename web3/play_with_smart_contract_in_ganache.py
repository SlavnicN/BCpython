from web3 import Web3, HTTPProvider
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

abi = compiled_code['hello']['abi']

w3 = Web3(HTTPProvider('http://localhost:7545'))

address = "0x04EE02b64C4D05a495db958C1fe11df66E8c39f1"
private_key = "0x27064b8e320d83ae1755aa9145ea76e4d65bd4071cd21a16e174f9cbcafd4d5b"
w3.eth.defaultAccount = '0x87A6544308BEaf8A14E57cAC0E3A8E93a98831A0'

Hello = w3.eth.contract(address= address, abi=abi)

print(Hello.functions.name().call())

print(Hello.functions.say_hello().call())


nonce = w3.eth.getTransactionCount(w3.eth.defaultAccount)

txn = Hello.functions.change_name(b"Lionel Messi").buildTransaction({
    'gas': 70000,
    'gasPrice': w3.toWei('1', 'gwei'),
    'nonce': nonce
})

signed_txn = w3.eth.account.signTransaction(txn, private_key=private_key)
signed_txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
w3.eth.waitForTransactionReceipt(signed_txn_hash)

print(Hello.functions.say_hello().call())




