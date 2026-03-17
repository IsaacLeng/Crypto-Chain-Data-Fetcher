# ⛓️ ETH vs SOL: Live Block Data Analyzer & Pipeline

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IsaacLeng/Crypto-Chain-Data-Fetcher/blob/main/ETH_SOL_TPS_Analysis.ipynb)
*(Click the badge above to run the dashboard directly in your browser / 点击上方徽章即可在浏览器中一键运行数据面板)*

## 📖 Overview / 项目简介
This project provides a lightweight, object-oriented data pipeline to fetch and analyze live on-chain metrics between **Ethereum (ETH)** and **Solana (SOL)**. 

By querying public RPC nodes, this tool not only captures real-time block snapshots but also calculates true network throughput (TPS) using rolling time-series windows. It highlights the architectural differences between a modular network (Ethereum) and a high-throughput monolithic network (Solana), serving as a foundation for broader quantitative blockchain analysis.

本项目是一个轻量级的面向对象数据管道，通过直接调用公共 RPC 节点，实时抓取并分析以太坊和 Solana 的链上数据。除了获取最新区块快照，本项目还通过滑动时间窗口计算真实的实时吞吐量（TPS），为量化分析和区块链基础架构对比提供数据支撑。

## ✨ Core Features / 核心功能
- **Real-Time TPS Calculation:** Computes actual Transactions Per Second (TPS) using rolling windows (e.g., last 5 blocks for ETH, last 15 slots for SOL) based on exact Unix timestamps.
- **Modular OOP Architecture:** Built with a scalable Object-Oriented Programming design, separating RPC client connections (`chain_clients.py`) from analytical logic (`tps_analyzer.py`).
- **Robust Error Handling:** Built-in retry mechanisms and safeguards against Solana's skipped slots and strict RPC rate limits.
- **Bilingual Documentation:** Code is thoroughly commented in both English and Chinese.

## 📂 Project Structure / 项目结构
```text
Crypto-Chain-Data-Fetcher/
├── src/
│   ├── __init__.py
│   ├── chain_clients.py    # RPC wrappers for Ethereum & Solana
│   └── tps_analyzer.py     # Time-series analysis and TPS logic
├── ETH_SOL_TPS_Analysis.ipynb # Interactive Colab Dashboard
├── requirements.txt        # Package dependencies
└── README.md
```
## 💻 Tech Stack / 技术栈
Python 3.x

Web3.py (Ethereum RPC interaction)

Requests (REST API calls for Solana)

Git (Version control & Colab integration)

## 🚀 Quick Start / 快速运行
### Option 1: Cloud Execution (Recommended)
The easiest way to run the analytical dashboard without setting up a local environment is via Google Colab. Simply click the "Open In Colab" badge at the top of this page. The notebook will automatically pull the latest modular code from this repository.

### Option 2: Local Setup
If you prefer to run this locally in your Jupyter environment or IDE:

1. Clone the repository:
```Bash
git clone [https://github.com/IsaacLeng/Crypto-Chain-Data-Fetcher.git](https://github.com/IsaacLeng/Crypto-Chain-Data-Fetcher.git)
cd Crypto-Chain-Data-Fetcher
```
2. Install the required dependencies:
```Bash
pip install -r requirements.txt
```
3. Run the interactive notebook ETH_SOL_TPS_Analysis.ipynb or import the modules into your own script.

## 📊 Sample Output / 预期输出样本

```text
--- 实时吞吐量 (TPS) 深度分析 ---
📊 Analyzing real-time TPS (ETH: last 5 blocks, SOL: last 15 slots)...

=== Ethereum 实时吞吐量 ===
采样区间: 区块 19432847 -> 19432851
总耗时: 60 秒 | 总交易: 752 笔
🚀 实际 TPS: 12.53 tx/s

=== Solana 实时吞吐量 ===
采样区间: 过去 15 个有效 Slots (截止 254198273)
总耗时: 6.2 秒 | 总交易: 18450 笔
🚀 实际 TPS: 2975.81 tx/s
```
Developed for educational and quantitative data analysis purposes. / 仅供学习与数据分析参考。
