from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider('http://localhost:7545'))

transaction = {
    'to': Web3.toChecksumAddress('0x87A6544308BEaf8A14E57cAC0E3A8E93a98831A0'),
    'value': w3.toWei('1','ether'),
    'gas': 100000,
    'gasPrice': w3.toWei('1','gwei'),
    'nonce': 0
}

print("Estimating gas usage: "+str(w3.eth.estimateGas(transaction)))
print("Gas price: "+ str(w3.eth.gasPrice))


