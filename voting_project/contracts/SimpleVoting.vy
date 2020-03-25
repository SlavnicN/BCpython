struct Proposal:
    name: bytes32
    vote_count: int128

Voting: event ({_from: indexed(address), _proposal: int128})

proposals: public(map(int128,Proposal))

proposals_count: public(int128)
voters_voted: public(map(address, int128))

@public
def __init__(_proposalNames: bytes32[2]):
    for i in range(2):
        self.proposals[i] = Proposal({
            name: _proposalNames[i],
            vote_count: 0
        })
        self.proposals_count += 1

@public
def vote(proposal: int128):
    assert self.voters_voted[msg.sender] == 0 #dev: already vote
    assert proposal < self.proposals_count #dev: not in the liste

    self.voters_voted[msg.sender] = 1
    self.proposals[proposal].vote_count += 1

    log.Voting(msg.sender, proposal)

@private
@constant
def winning_proposal() -> int128:
    winning_vote_count: int128 = 0
    winning_proposal: int128 = 0
    for i in range(2):
        if self.proposals[i].vote_count > winning_vote_count:
            winning_vote_count = self.proposals[i].vote_count
            winning_proposal = i
    return winning_proposal

@public
@constant
def winner_name() -> bytes32:
    return self.proposals[self.winning_proposal()].name
