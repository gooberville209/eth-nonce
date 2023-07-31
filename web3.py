from web3 import Web3

def get_transaction_count(wallet_address, infura_url):
    # Connect to Ethereum node
    w3 = Web3(Web3.HTTPProvider(infura_url))
    
    # Ensure wallet address is valid
    if not w3.isAddress(wallet_address):
        raise ValueError("Invalid Ethereum wallet address")
    
    # Fetch transaction count
    transaction_count = w3.eth.getTransactionCount(wallet_address)
    
    return transaction_count

if __name__ == "__main__":
    # Replace with your own values
    WALLET_ADDRESS = 'YOUR_ETHEREUM_WALLET_ADDRESS'
    INFURA_URL = 'YOUR_INFURA_URL'
    
    count = get_transaction_count(WALLET_ADDRESS, INFURA_URL)
    print(f"Number of transactions for wallet {WALLET_ADDRESS}: {count}")

