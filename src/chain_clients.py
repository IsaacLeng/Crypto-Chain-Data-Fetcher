from web3 import Web3
import requests
import datetime
import time

class EthClient:
    """Ethereum RPC Client for fetching on-chain data."""
    def __init__(self, rpc_url="https://ethereum-rpc.publicnode.com"):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        if not self.w3.is_connected():
            raise ConnectionError(f"Failed to connect to Ethereum RPC: {rpc_url}")

    def get_latest_block_stats(self):
        """Fetches the latest block and extracts key metrics."""
        block = self.w3.eth.get_block('latest')
        return {
            "network": "Ethereum",
            "height": block.number,
            "timestamp": datetime.datetime.fromtimestamp(block.timestamp),
            "tx_count": len(block.transactions),
            "size_kb": round(block.size / 1024, 2)
        }

class SolClient:
    """Solana REST API Client for fetching on-chain data."""
    def __init__(self, rpc_url="https://api.mainnet-beta.solana.com"):
        self.url = rpc_url
        self.headers = {"Content-Type": "application/json"}

    def get_latest_slot(self):
        payload = {"jsonrpc": "2.0", "id": 1, "method": "getSlot"}
        response = requests.post(self.url, json=payload, headers=self.headers).json()
        return response.get('result')

    def get_block_stats(self, slot, max_retries=3):
        """Fetches block details for a specific slot with retry logic."""
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getBlock",
            "params": [
                slot,
                {
                    "encoding": "json",
                    "maxSupportedTransactionVersion": 0,
                    "transactionDetails": "signatures"
                }
            ]
        }
        
        for attempt in range(max_retries):
            response = requests.post(self.url, json=payload, headers=self.headers).json()
            if 'result' in response and response['result'] is not None:
                signatures = response['result'].get('signatures', [])
                return {
                    "network": "Solana",
                    "height": slot,
                    "tx_count": len(signatures)
                }
            time.sleep(1)
            slot -= 1 
            
        raise ValueError("Failed to fetch Solana block after multiple retries.")
