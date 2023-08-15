TEMPLATE = """\
# @version {}

n: public(uint256)

@external
def set_n(to: uint256):
    assert to != 2  # dev: assert not 2
    if to == 3:
        raise "raise if 3"
    assert to != 4, "assert not 4"
    assert to == 5  # dev: assert 5
    self.n = to
"""
VERSIONS = [
    "0.2.1",
    "0.2.2",
    "0.2.3",
    "0.2.4",
    "0.2.5",
    "0.2.7",
    "0.2.8",
    "0.2.11",
    "0.2.12",
    "0.2.15",
    "0.2.16",
    "0.3.0",
    "0.3.1",
    "0.3.2",
    "0.3.3",
    "0.3.4",
    "0.3.6",
    "0.3.7",
    "0.3.8",
    "0.3.9",
    "0.3.10",
]

for version in VERSIONS:
    with open(f'contracts/Template{version.replace(".", "")}.vy', "wt") as f:
        f.write(TEMPLATE.format(version))
