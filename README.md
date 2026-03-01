<div align="center">

# ☁️ TeraBox Downloader — Telegram Bot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/python--telegram--bot-21.6-blue?style=for-the-badge" alt="PTB"/>
  <img src="https://img.shields.io/badge/curl__cffi-Chrome%20impersonation-orange?style=for-the-badge" alt="curl_cffi"/>
  <img src="https://img.shields.io/badge/Docker-ready-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
</p>

A clean, modular **Telegram bot** that resolves TeraBox share links into direct download URLs — powered by `curl_cffi` Chrome impersonation to reliably bypass Cloudflare.

---
</div>

## ✨ Features

- 🔗 **Direct link extraction** — resolves any TeraBox share URL to a `dlink` in seconds
- 🛡️ **Cloudflare bypass** — uses `curl_cffi` with Chrome 110 browser impersonation
- 💾 **In-memory TTL cache** — avoids hammering the API for repeated links (configurable TTL)
- 🖼️ **Thumbnail preview** — sends the file thumbnail when available
- 🌐 **Multi-domain support** — works across all major TeraBox domains
- 🐳 **Docker ready** — single-command deployment

---

## 📁 Project Structure

```
terabox_bot/
├── main.py               ← Entry point; starts the bot
├── config.py             ← Loads all env vars (BOT_TOKEN, NDUS_COOKIE, etc.)
├── requirements.txt      ← Python dependencies
├── Dockerfile            ← Container definition
├── .env.example          ← Copy → .env and fill in your values
│
├── bot/
│   ├── __init__.py
│   ├── app.py            ← Builds and wires the PTB Application
│   └── handlers.py       ← /start, /help, and link message handlers
│
├── core/
│   ├── __init__.py
│   ├── terabox.py        ← TeraBox API client (jsToken scrape + share/list call)
│   └── cache.py          ← Simple in-memory TTL cache
│
└── utils/
    ├── __init__.py
    ├── url.py            ← URL validation, surl extraction, text URL finder
    └── formatting.py     ← format_bytes() and other display helpers
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- A Telegram Bot token from [@BotFather](https://t.me/BotFather)
- The `ndus` cookie from [terabox.com](https://www.terabox.com) (see below)

### Getting the `ndus` Cookie

1. Log in to [https://www.terabox.com](https://www.terabox.com) in your browser
2. Open **DevTools** (`F12`) → **Application** tab → **Cookies** → `terabox.com`
3. Copy the value of the `ndus` cookie

---

### 1️⃣ Local Setup

```bash
# Clone the repo
git clone https://github.com/yourname/terabox-tg-bot.git
cd terabox-tg-bot

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and fill in BOT_TOKEN and NDUS_COOKIE

# Run the bot
python main.py
```

---

### 2️⃣ Docker Deployment

```bash
# Build the image
docker build -t terabox-tg-bot .

# Run with env vars
docker run -d \
  -e BOT_TOKEN=your_token \
  -e NDUS_COOKIE=your_ndus_value \
  --name terabox-bot \
  terabox-tg-bot
```

Or using a `.env` file:

```bash
docker run -d --env-file .env --name terabox-bot terabox-tg-bot
```

---

## ⚙️ Environment Variables

| Variable     | Required | Default | Description |
|--------------|----------|---------|-------------|
| `BOT_TOKEN`  | ✅ Yes   | —       | Telegram bot token from @BotFather |
| `NDUS_COOKIE`| ✅ Yes   | —       | `ndus` cookie value from terabox.com |
| `CACHE_TTL`  | No       | `7200`  | Seconds to cache resolved links (2 hrs) |
| `LOG_LEVEL`  | No       | `INFO`  | Logging verbosity: `DEBUG`, `INFO`, `WARNING` |

---

## 🌐 Supported Domains

| Domain |
|--------|
| `terabox.com` / `www.terabox.com` |
| `terabox.app` / `www.terabox.app` |
| `1024terabox.com` / `www.1024terabox.com` |
| `teraboxshare.com` / `www.teraboxshare.com` |
| `teraboxlink.com` / `www.teraboxlink.com` |
| `dm.terabox.app` |

---

## 🤖 Bot Commands

| Command  | Description |
|----------|-------------|
| `/start` | Welcome message |
| `/help`  | Supported link formats and usage |
| _(any TeraBox link)_ | Resolves and returns the direct download URL |

---

## 🔍 How It Works

1. User sends a TeraBox share link
2. Bot extracts the `surl` token from the URL
3. Checks the in-memory cache — returns instantly if already resolved
4. Otherwise: GETs the share page and scrapes the `jsToken` from the HTML
5. Calls `https://dm.terabox.app/share/list` with the token → gets file metadata + `dlink`
6. Replies with filename, size, thumbnail (if available), and a download button

---

## 🤝 Credits

Based on the original TeraBox API logic by:

🌟 **[@cantarella_wuwa](https://t.me/cantarella_wuwa)**
🌟 **[@cantarellabots](https://t.me/cantarellabots)**

---

<p align="center"><i>Developed with ❤️ for the open-source community.</i></p>

