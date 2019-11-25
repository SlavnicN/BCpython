pragma solidity ^0.4.0;

contract Donation{
    struct DonaturDetail{
        uint256 sum;
        string name;
        uint time;
    }
    mapping(address => DonaturDetail) public donatur_details;
    address public donatee;
    address[10] public donaturs;
    uint256 index; 


    constructor() public {
        donatee = msg.sender;
    }

    function donate(string name) public payable{
        require (msg.value >= 0.5 ether); //dev: not enougth you dumb
        require (index < 10); //dev: too many people

        donatur_details[msg.sender] = DonaturDetail({
                                                    sum: msg.value, 
                                                    name:name, 
                                                    time: block.timestamp
                                                    });
        
        donaturs[index] = msg.sender; 
        index += 1;
    }

    function withdraw_donation() public{
        require(msg.sender == donatee);//dev: wrong guy, budy
        donatee.send(this.balance);
    }
}