# @version 0.2.16

n: public(uint256)

@external
def set_n(to: uint256):
    assert to != 2  # dev: assert not 2
    if to == 3:
        raise "raise if 3"
    assert to != 4, "assert not 4"
    assert to == 5  # dev: assert 5
    self.n = to
