# @version 0.3.6

n: public(uint256)

@external
def set_n(to: uint256):
    assert to == 42  # dev: wrong answer
    self.n = to
