import ape
import pytest
from ape.contracts import ContractContainer


versions = ["0.3.7", "0.3.8", "0.3.9", "0.3.10"]


@pytest.fixture
def factory(project, accounts):
    return project.Factory.deploy(sender=accounts[0])


@pytest.fixture(params=versions)
def template(project, accounts, request):
    name = "Template" + request.param.replace(".", "")
    return getattr(project, name).deploy(sender=accounts[0])


@pytest.fixture
def clone(template, factory, accounts, project):
    receipt = factory.clone(template, sender=accounts[0])
    return ContractContainer(template.contract_type).at(receipt.return_value)


def test_template(template, accounts):
    assert template.n() == 0

    template.set_n(42, sender=accounts[0])
    assert template.n() == 42

    with ape.reverts(dev="wrong answer"):
        template.set_n(69, sender=accounts[0])

    assert template.n() == 42


def test_clone(clone, accounts):
    assert clone.n() == 0

    clone.set_n(42, sender=accounts[0])
    assert clone.n() == 42

    with ape.reverts(dev="wrong answer"):
        clone.set_n(69, sender=accounts[0])

    assert clone.n() == 42
