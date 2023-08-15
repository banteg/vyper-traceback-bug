from ape import networks, accounts, project, reverts
import pytest
from ape.contracts import ContractContainer
import typer

app = typer.Typer()


@app.command()
def main(version: str):
    dev = accounts.test_accounts[0]
    networks.parse_network_choice(":local:foundry").__enter__()

    factory = project.Factory.deploy(sender=dev)
    name = "Template" + version.replace(".", "")

    # template
    template = getattr(project, name).deploy(sender=dev)

    assert template.n() == 0

    template.set_n(42, sender=dev)
    assert template.n() == 42

    with reverts(dev_message="dev: wrong answer"):
        template.set_n(69, sender=dev)

    assert template.n() == 42

    # clone
    receipt = factory.clone(template, sender=dev)
    clone = ContractContainer(template.contract_type).at(receipt.return_value)

    assert clone.n() == 0

    clone.set_n(42, sender=dev)
    assert clone.n() == 42

    with reverts(dev_message="dev: wrong answer"):
        clone.set_n(69, sender=dev)

    assert clone.n() == 42


if __name__ == "__main__":
    app()
