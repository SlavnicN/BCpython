from web3 import Web3
w3 = Web3()

with open('/home/slavnic/.ethereum/rinkeby/keystore/UTC--2019-10-12T17-07-17.673753784Z--4b9c55f40d1dccc01d2a8fc778855ccc4d185137') as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(encrypted_key, 'password123')
    print(private_key)
