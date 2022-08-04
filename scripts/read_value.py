from brownie import accounts, config, TestContract

def say_hello():
    test_contract = TestContract[-1]
    print(test_contract)
    print(test_contract.hello())
    
def main():
    say_hello()