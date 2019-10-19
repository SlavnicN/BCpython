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

bytecode = compiled_code['hello']['bytecode']
abi = compiled_code['hello']['abi']

w3 = Web3(HTTPProvider('http://localhost:7545'))

HelloSmartContract = w3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = HelloSmartContract.constructor().transact({'from': '0x87A6544308BEaf8A14E57cAC0E3A8E93a98831A0'})

#need to wait to get the smart contract address after the tx has been confirmed
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print(tx_receipt)

