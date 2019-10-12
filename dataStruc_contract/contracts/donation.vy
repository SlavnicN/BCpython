struct DonaturDetail:
    sum: uint256(wei)
    name: bytes[100]
    time: timestamp

contract Hello():
    def say_hello() -> bytes[32]: constant

donatur_details: public(map(address, DonaturDetail))

donaturs: public(address[10])

donatee: public(address)

index: int128

@public
def __init__():
    self.donatee = msg.sender

@payable #this means it accepte payment in ether in this methode
@public
def donate(name: bytes[100]):
    assert msg.value >= as_wei_value(1, "ether") #it's the same as saying >=1000000000000000000
    assert self.index < 10

    self.donatur_details[msg.sender] = DonaturDetail({
                                            sum: msg.value,
                                            name: name,
                                            time: block.timestamp 
                                        })
    
    self.donaturs[self.index] = msg.sender
    self.index += 1
@public
def withdraw_donation():
    assert msg.sender == self.donatee   

    send(self.donatee, self.balance)

@public
@constant
def donation_smart_contract_call_hello_smart_contract_methode(smart_contract_address: address) -> bytes[32]:
    return Hello(smart_contract_address).say_hello()

