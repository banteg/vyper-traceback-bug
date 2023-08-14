# @version 0.3.10

@external
def clone(clone: address) -> address:
    return create_minimal_proxy_to(clone)
