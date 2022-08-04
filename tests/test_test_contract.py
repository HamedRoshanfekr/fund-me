from brownie import TestContract, accounts

def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    test_contract = TestContract.deploy({"from": account})
    hello = test_contract.hello()
    expected = "Hello!"
    # Assert
    assert expected == hello