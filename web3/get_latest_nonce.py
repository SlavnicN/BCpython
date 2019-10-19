from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider('http://localhost:7545'))
transaction_count = w3.eth.getTransactionCount("0xDE5EC7Ee54F935A34a15445e64c8Fc796ADb18fb")
print(transaction_count)