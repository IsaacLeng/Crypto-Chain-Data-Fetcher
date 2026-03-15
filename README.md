# ⛓️ ETH vs SOL: Live Block Data Analyzer

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IsaacLeng/Crypto-Chain-Data-Fetcher/blob/main/ETH_SOL_TPS_Analysis.ipynb)
*(Click the badge above to run the script directly in your browser / 点击上方徽章即可在浏览器中一键运行)*

## 📖 Overview / 项目简介
This project provides a lightweight, real-time data pipeline to fetch and compare live block metrics between **Ethereum (ETH)** and **Solana (SOL)**. 

By querying public RPC nodes, this script highlights the fundamental architectural differences between a modular, high-security network (Ethereum) and a monolithic, high-throughput network (Solana). It serves as a foundational tool for broader blockchain data extraction and quantitative time-series analysis.

本项目是一个轻量级的实时数据管道，通过直接调用公共 RPC 节点，实时抓取并对比以太坊和 Solana 的区块底层数据。这直观地展示了“模块化”与“单体式”区块链在吞吐量（TPS）和出块逻辑上的本质差异。

## ✨ Core Features / 核心功能
- **Ethereum Data Fetching:** Utilizes `Web3.py` to extract block height, timestamp, transaction count, and block size via Cloudflare/PublicNode RPCs.
- **Solana Data Fetching:** Uses native `requests` to query the Solana Mainnet-Beta JSON-RPC, extracting real-time slot data and high-frequency transaction signatures.
- **Robust Error Handling:** Built-in safeguards against common RPC rate limits and empty slot queries.
- **Bilingual Documentation:** Code is thoroughly commented in both English and Chinese.

## 💻 Tech Stack / 技术栈
- **Python 3.x**
- **Web3.py** (Ethereum RPC interaction)
- **Requests** (REST API calls for Solana)

## 🚀 Quick Start / 快速运行

### Option 1: Cloud Execution (Recommended)
The easiest way to run this code without setting up a local environment is via Google Colab. Simply click the **"Open In Colab"** badge at the top of this page.

### Option 2: Local Setup
If you prefer to run this locally in your Jupyter environment:

1. Clone the repository:
   ```bash
   git clone [https://github.com/IsaacLeng/Crypto-Chain-Data-Fetcher.git](https://github.com/IsaacLeng/Crypto-Chain-Data-Fetcher.git)
2. Install the required dependencies:
   ```bash
   pip install web3 requests
3. Run the Python script or open the Jupyter Notebook.
   Sample Output / 预期输出样本
  ```Plaintext
=== 以太坊 (Ethereum) 最新区块 ===
区块高度: 19432851
出块时间: 2024-03-15 10:12:45
包含交易数: 142 笔
区块大小: 125.40 KB

=== Solana 最新区块 ===
最新 Slot 高度: 254198273
包含交易数: 2105 笔

Developed for educational and data analysis purposes. / 仅供学习与数据分析参考。
