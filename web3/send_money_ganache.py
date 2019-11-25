from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider('HTTP://127.0.0.1:7545'))

private_key = 'c09fe042c4a69d50e36ac22bfa49c1c18eba7b2df98ed6000a91efce9dee3ae7'

transaction = {
    'to': Web3.toChecksumAddress('0x87A6544308BEaf8A14E57cAC0E3A8E93a98831A0'),
    'value': w3.toWei('1','ether'),
    'gas': 100000,
    'gasPrice': w3.toWei('1', 'gwei'),
    'nonce': 2
}

signed = w3.eth.account.signTransaction(transaction, private_key)
tx = w3.eth.sendRawTransaction(signed.rawTransaction)