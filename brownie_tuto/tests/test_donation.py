#!/usr/bin/python3
from brownie import accounts
from web3.auto import w3
import pytest

def test_donatee(Donation):
    donation = accounts[0].deploy(Donation)
    
    assert(accounts[0] == w3.eth.coinbase)

def test_donate_less_than_1_eth(Donation):
    donation = accounts[0].deploy(Donation)
    with pytest.reverts('dev: not enougth you dumb'):
        donation.donate('Taylor Swift',{'value': 500000000000000})

def test_donate_1_eth(Donation):
    import time
    donation = accounts[0].deploy(Donation)

    donatur_name = 'Novak Djokovic'
    donation.donate(donatur_name, {'from': accounts[1], 'value': 5000000000000000000})
    donatur = donation.donaturs(0)
    donation_sum = donation.donatur_details(donatur)['sum']
    donation_name = donation.donatur_details(donatur)['name']
    donation_time = donation.donatur_details(donatur)['time']

    assert(donatur == accounts[1])
    assert(donation_sum == 5000000000000000000)
    assert(donation_name == donatur_name)
    assert(int(time.time()) - donation_time < 600)


