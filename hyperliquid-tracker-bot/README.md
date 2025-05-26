# Hyperliquid Whale Tracker Bot

This bot scrapes large positions (over $1M) from Coinglass's Hyperliquid page and sends them to a Telegram chat.

## Features
- Detects positions over $1 million
- Parses coin name, amount, direction, and wallet address
- Tracks wallet net position trend
- Avoids duplicate messages

## Installation

1. Install Python 3.10+ and add to PATH
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Add your Telegram bot token and chat ID in the `bot.py` file.

```bash
python bot.py
```

## License

MIT
