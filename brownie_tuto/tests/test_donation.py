#!/usr/bin/python3
from brownie import accounts
from web3.auto import w3
import pytest
#import eth_tester

def test_donatee(Donation):
    donation = accounts[0].deploy(Donation)
    
    assert(accounts[0] == w3.eth.coinbase)

def test_donate_less_than_1_eth(Donation):
    donation = accounts[0].deploy(Donation)
    with pytest.reverts('dev: not enougth you dumb'):
        donation.donate('Taylor Swift',{'value': 500000000000000})