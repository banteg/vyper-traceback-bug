# @version 0.2.2

n: public(uint256)

@external
def set_n(to: uint256):
    assert to != 2  # dev: assert not 2
    if to == 3:
        raise "raise if 3"
    assert to != 5, "assert not 5"
    assert to == 4  # dev: assert 4
    self.n = to
