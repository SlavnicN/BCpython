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
        donation.donate('Taylor Swift',{'value': w3.toWei('0.05','ether')})

def test_donate_1_eth(Donation):
    import time
    donation = accounts[0].deploy(Donation)

    donatur_name = 'Novak Djokovic'
    donation.donate(donatur_name, {'from': accounts[1], 'value': w3.toWei('0.5','ether')})
    donatur = donation.donaturs(0)
    donation_sum = donation.donatur_details(donatur)['sum']
    donation_name = donation.donatur_details(donatur)['name']
    donation_time = donation.donatur_details(donatur)['time']

    assert(donatur == accounts[1])
    assert(donation_sum == w3.toWei('0.5','ether'))
    assert(donation_name == donatur_name)
    assert(int(time.time()) - donation_time < 600)

def test_wrong_account_withdraw_donation(Donation):
    donation = accounts[0].deploy(Donation)
    donatur_name = 'Novak Djokovic'
    donation.donate(donatur_name,{'from': accounts[1], 'value': w3.toWei('1','ether')})

    with pytest.reverts('dev: wrong guy, budy'):
        donation.withdraw_donation({'from': accounts[1]})

def test_withdraw_donation(Donation):
    donation = accounts[0].deploy(Donation)
    donatur_name = 'Rafa'
    donation.donate(donatur_name,{'from': accounts[1], 'value': w3.toWei('1','ether')})

    initial_balance = w3.eth.getBalance(w3.eth.coinbase)
    donation.withdraw_donation()
    after_withdraw_balance = w3.eth.getBalance(w3.eth.coinbase)

    assert(abs(after_withdraw_balance - initial_balance) - w3.toWei('1','ether') < w3.toWei('1','gwei'))