#!/usr/bin/python3
from brownie import accounts
import pytest

def test_greeter(Greeter):
    greeter = accounts[0].deploy(Greeter)

    greeting = greeter.greet()
    assert greeting == 'Hello'


def test_custom_greeting(Greeter):
    greeter = accounts[0].deploy(Greeter)

    greeter.setGreeting('Guten Tag')

    greeting = greeter.greet()
    assert greeting == 'Guten Tag'
