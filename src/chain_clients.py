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

    # ==========================================
    # V1 方法 (保留)：用于获取最新区块的“快照”
    # 特点：返回格式化好的 datetime 时间，方便直接 print 打印给人看
    # ==========================================
    def get_latest_block_stats(self):
        block = self.w3.eth.get_block('latest')
        return {
            "network": "Ethereum",
            "height": block.number,
            "timestamp": datetime.datetime.fromtimestamp(block.timestamp),
            "tx_count": len(block.transactions),
            "size_kb": round(block.size / 1024, 2)
        }

    # ==========================================
    # V2 方法 (新增)：用于获取历史区块并进行 TPS 数学计算
    # 特点：支持传入具体的区块高度，并且返回原始的 Unix 时间戳（整数）供代码计算
    # ==========================================
    def get_block_by_identifier(self, block_identifier='latest'):
        block = self.w3.eth.get_block(block_identifier)
        return {
            "network": "Ethereum",
            "height": block.number,
            "timestamp": block.timestamp, # 原始数字格式时间戳
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

    # ==========================================
    # V1 & V2 兼容版升级：在字典里直接追加 timestamp 字段
    # ==========================================
    def get_block_stats(self, slot, max_retries=3):
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getBlock",
            "params": [
                slot,
                {"encoding": "json", "maxSupportedTransactionVersion": 0, "transactionDetails": "signatures"}
            ]
        }
        
        for attempt in range(max_retries):
            response = requests.post(self.url, json=payload, headers=self.headers).json()
            if 'result' in response and response['result'] is not None:
                block_data = response['result']
                signatures = block_data.get('signatures', [])
                
                # 新增抓取 blockTime
                block_time = block_data.get('blockTime') 
                
                return {
                    "network": "Solana",
                    "height": slot,
                    "timestamp": block_time, 
                    "tx_count": len(signatures)
                }
            time.sleep(1)
            slot -= 1 
            
        return None
