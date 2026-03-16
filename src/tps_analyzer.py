from .chain_clients import EthClient, SolClient

class NetworkAnalyzer:
    """Analyzes and compares live data across different blockchain networks."""
    def __init__(self):
        # Automatic node connection during initialization / 初始化时自动连接节点
        self.eth_client = EthClient()
        self.sol_client = SolClient()

    def compare_live_transactions(self):
        """Fetches and prints a live comparison of the latest block transactions."""
        print("Fetching live data from networks...\n")
        
        # Get Ethereum data / 获取以太坊数据
        eth_stats = self.eth_client.get_latest_block_stats()
        print(f"=== {eth_stats['network']} ===")
        print(f"Block Height: {eth_stats['height']}")
        print(f"Timestamp: {eth_stats['timestamp']}")
        print(f"Transactions: {eth_stats['tx_count']} txs")
        print(f"Block Size: {eth_stats['size_kb']} KB\n")

        # Get Solana data / 获取 Solana 数据
        latest_slot = self.sol_client.get_latest_slot()
        sol_stats = self.sol_client.get_block_stats(latest_slot)
        print(f"=== {sol_stats['network']} ===")
        print(f"Slot Height: {sol_stats['height']}")
        print(f"Transactions: {sol_stats['tx_count']} txs\n")
        
        # Simple difference analysis / 简单的差异分析
        diff = sol_stats['tx_count'] - eth_stats['tx_count']
        print(f"👉 Analysis: Solana's current block processed {diff} more transactions than Ethereum's.")
