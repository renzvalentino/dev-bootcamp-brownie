from brownie import ERC20Basic, config, accounts, network


def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20 = ERC20Basic[-1]
    print("Total Supply is", erc20.totalSupply())
