# CryptoSystem

> A modular, AI-assisted personal crypto automation platform built for long-term development.

---

# Overview

CryptoSystem is a long-term software project focused on building a complete personal crypto automation platform.

This project is **not** a simple trading bot.

The objective is to create a modular system capable of collecting market data, analyzing trends, making trading decisions, managing risk, executing trades, and continuously improving through historical analysis and AI assistance.

---

# Vision

Build a production-quality platform that can:

- Collect real-time market data
- Research and analyze market behavior
- Generate trading signals
- Manage trading risk
- Execute orders automatically
- Record trading history
- Evaluate trading performance
- Learn from historical data
- Assist decision making with AI
- Automate repetitive workflows

---

# Architecture

```
Database
    ↓
Collector
    ↓
Research
    ↓
Decision Engine
    ↓
Risk Engine
    ↓
Execution Engine
    ↓
Dashboard
    ↓
AI Layer
    ↓
Automation
```

Every layer has a single responsibility.

Dependencies always flow downward.

---

# Project Structure

```
CryptoSystem/

├── src/
│   ├── core/
│   ├── shared/
│   ├── database/
│   ├── collector/
│   ├── research/
│   ├── decision/
│   ├── risk/
│   ├── execution/
│   ├── dashboard/
│   ├── ai/
│   └── automation/
│
├── config/
├── tests/
├── logs/
│
├── README.md
├── AGENTS.md
├── CHANGELOG.md
├── VERSION
├── requirements.txt
└── main.py
```

---

# Technology Stack

- Python 3.13
- SQLite (initial database)
- Type Hints
- Dataclasses
- Dependency Injection
- Logging
- Unit Testing
- Modular Architecture

Future integrations may include:

- Binance API
- Bybit API
- CCXT
- Pandas
- NumPy
- Plotly
- FastAPI

---

# Development Principles

- Production-quality code only
- English source code
- SOLID principles
- DRY
- KISS
- Strong typing
- Logging everywhere
- One responsibility per module
- Modular architecture
- Test-first mindset
- No placeholder implementations
- No duplicated logic

---

# Current Progress

| Module | Status |
|---------|--------|
| Project Planning | ✅ Completed |
| System Architecture | ✅ Completed |
| Development Standards | ✅ Completed |
| Core Foundation | 🚧 In Progress |
| Shared Models | ⏳ Planned |
| Database | ⏳ Planned |
| Collector | ⏳ Planned |
| Research | ⏳ Planned |
| Decision Engine | ⏳ Planned |
| Risk Engine | ⏳ Planned |
| Execution Engine | ⏳ Planned |
| Dashboard | ⏳ Planned |
| AI Layer | ⏳ Planned |
| Automation | ⏳ Planned |

Overall Progress:

**≈ 30%**

---

# Roadmap

| Version | Milestone |
|----------|-----------|
| 060.x | Core Foundation |
| 061.x | Shared Models |
| 062.x | Database Layer |
| 063.x | Market Collector |
| 064.x | Research Engine |
| 065.x | Decision Engine |
| 066.x | Risk Engine |
| 067.x | Execution Engine |
| 068.x | Dashboard |
| 069.x | AI Layer |
| 070.x | Automation Layer |

---

# Running

Clone the repository:

```bash
git clone https://github.com/hgblue09124-code/CryptoSystem.git
```

Enter the project:

```bash
cd CryptoSystem
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

Run tests:

```bash
python -m unittest
```

---

# AI Development

This repository is designed to be developed with AI assistance.

Before generating code, AI assistants should read:

- AGENTS.md

This file defines:

- Architecture
- Coding standards
- Development workflow
- Project rules
- Module responsibilities

---

# License

This is a personal long-term software project.

Copyright © 2026.
