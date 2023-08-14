TEMPLATE = '''\
# @version {}

n: public(uint256)

@external
def set_n(to: uint256):
    assert to == 42  # dev: wrong answer
    self.n = to
'''

for version in ['0.3.7', '0.3.8', '0.3.9', '0.3.10']:
    with open(f'contracts/Template{version.replace(".", "")}.vy', 'wt') as f:
        f.write(TEMPLATE.format(version))
