from unittest import mock
from brownie import accounts, config, TestContract, network, FundMe, MockV3Aggregator
from scripts.helper import LOCAL_BLOCKCHAIN_ENVIRONMENT, deploy_mocks, get_account


def deploy_test():
    account = get_account()
    # account = accounts.add(config["wallets"]["from_key"])
    testContract = TestContract.deploy({"from": account})
    print(account)
    print(testContract.hello())
    print(testContract.howdy("yall"))
    
def deploy_fund_me():
    print(f"active network is {network.show_active()}")
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    
    fund_me = FundMe.deploy(price_feed_address, {"from": account}, publish_source= config["networks"][network.show_active()].get("verify"))
    print(f"{fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
