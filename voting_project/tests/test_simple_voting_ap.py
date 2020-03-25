import pytest
import brownie
from brownie import accounts
from web3.auto import w3

@pytest.fixture
def voting(SimpleVoting):
    voting = accounts[0].deploy(SimpleVoting,[b'Djokovic',b'Nadal'])
    return voting

def test_initial_state(voting):
    assert voting.proposals_count() == 2

    Djokovic = voting.proposals__name(0)
    Nadal = voting.proposals__name(1)
    DjokovicVote = voting.proposals__vote_count(0)
    NadalVote = voting.proposals__vote_count(1)
    startDjoko = 32 - len(b'Djokovic')
    startNadal = 32 - len(b'Nadal')
    assert len(Djokovic) == 32 #not applicable (i use string and note bytes32)
    assert Djokovic[startDjoko:] == b'Djokovic'
    assert Nadal[startNadal:] == b'Nadal'
    assert DjokovicVote == 0
    assert NadalVote == 0

def test_vote(voting):
    assert voting.proposals__vote_count(0) == 0

    voting.vote(0,{'from': accounts[1]})

    assert voting.proposals__vote_count(0) == 1

def test_fail_duplicate_vote(voting):
    voting.vote(0,{'from': accounts[1]})
    with brownie.reverts('dev: already vote'):
        voting.vote(1,{'from': accounts[1]})
    with brownie.reverts('dev: already vote'):
        voting.vote(0,{'from': accounts[1]})


def test_winning_proposal(voting):
    startDjoko = 32 - len(b'Djokovic')
    voting.vote(0,{'from': accounts[1]})
    voting.vote(0,{'from': accounts[2]})
    voting.vote(1,{'from': accounts[3]})

    assert voting.proposals__vote_count(0) == 2
    assert voting.proposals__vote_count(1) == 1
    assert voting.winner_name()[startDjoko:] == b'Djokovic'