import ape
import pytest
from ape.contracts import ContractContainer


versions = [
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


@pytest.fixture
def factory(project, accounts):
    return project.Factory.deploy(sender=accounts[0])


@pytest.fixture(params=versions)
def template(project, accounts, request):
    name = "Template" + request.param.replace(".", "")
    return getattr(project, name).deploy(sender=accounts[0])


@pytest.fixture
def clone(template, factory, accounts):
    receipt = factory.clone(template, sender=accounts[0])
    return ContractContainer(template.contract_type).at(receipt.return_value)


def verify_logic(contract, caller):
    assert contract.n() == 0

    contract.set_n(5, sender=caller)
    assert contract.n() == 5

    with ape.reverts(dev_message="dev: assert not 2"):
        contract.set_n(2, sender=caller)

    with ape.reverts("raise if 3"):
        contract.set_n(3, sender=caller)

    with ape.reverts("assert not 4"):
        contract.set_n(4, sender=caller)

    with ape.reverts(dev_message="dev: assert 5"):
        contract.set_n(6, sender=caller)

    assert contract.n() == 5


def test_template(template, accounts):
    verify_logic(template, accounts[0])


def test_clone(clone, accounts):
    verify_logic(clone, accounts[0])
