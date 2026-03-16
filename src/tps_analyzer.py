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
    
    # 作用：回溯 N 个区块，计算真实的 TPS，V2 version
    def calculate_real_tps(self, eth_blocks=5, sol_blocks=15):
        """
        Calculates real TPS by sampling the last N blocks from each network.
        ETH 出块慢(~12秒)，取 5 个区块约 1 分钟数据。
        SOL 出块快(~400毫秒)，取 15 个区块约几秒数据。
        """
        print(f"📊 Analyzing real-time TPS (ETH: last {eth_blocks} blocks, SOL: last {sol_blocks} slots)...\n")

        # --- 1. 计算 Ethereum TPS ---
        latest_eth = self.eth_client.get_block_by_identifier('latest')
        eth_end_height = latest_eth['height']
        eth_end_time = latest_eth['timestamp']
        
        eth_total_txs = 0
        eth_start_time = eth_end_time
        
        for i in range(eth_end_height - eth_blocks + 1, eth_end_height + 1):
            block = self.eth_client.get_block_by_identifier(i)
            eth_total_txs += block['tx_count']
            if i == eth_end_height - eth_blocks + 1:
                eth_start_time = block['timestamp']

        eth_time_diff = eth_end_time - eth_start_time
        # 防止除以 0 的情况
        eth_tps = eth_total_txs / eth_time_diff if eth_time_diff > 0 else 0

        print(f"=== Ethereum 实时吞吐量 ===")
        print(f"采样区间: 区块 {eth_end_height - eth_blocks + 1} -> {eth_end_height}")
        print(f"总耗时: {eth_time_diff} 秒 | 总交易: {eth_total_txs} 笔")
        print(f"🚀 实际 TPS: {eth_tps:.2f} tx/s\n")

        # --- 2. 计算 Solana TPS ---
        latest_slot = self.sol_client.get_latest_slot()
        sol_total_txs = 0
        valid_sol_blocks = 0
        
        current_slot = latest_slot
        sol_end_time = None
        sol_start_time = None
        
        while valid_sol_blocks < sol_blocks:
            block = self.sol_client.get_block_stats(current_slot)
            if block and block['timestamp']:
                if valid_sol_blocks == 0:
                    sol_end_time = block['timestamp']
                
                sol_total_txs += block['tx_count']
                sol_start_time = block['timestamp']
                valid_sol_blocks += 1
                
            current_slot -= 1

        sol_time_diff = sol_end_time - sol_start_time
        sol_tps = sol_total_txs / sol_time_diff if sol_time_diff > 0 else 0

        print(f"=== Solana 实时吞吐量 ===")
        print(f"采样区间: 过去 {sol_blocks} 个有效 Slots (截止 {latest_slot})")
        print(f"总耗时: {sol_time_diff} 秒 | 总交易: {sol_total_txs} 笔")
        print(f"🚀 实际 TPS: {sol_tps:.2f} tx/s\n")
