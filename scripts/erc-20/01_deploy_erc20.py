from brownie import ERC20Basic, config, accounts
 
def deployContract():
    account = accounts.add(config["wallets"]["from_key"])
    ERC20Basic.deploy(100000000,{'from': account})
 
def main():
    deployContract()
