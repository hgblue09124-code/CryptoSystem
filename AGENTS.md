# AGENTS.md

# CryptoSystem AI Development Guide

Version: 1.0

---

# Mission

CryptoSystem is a long-term personal crypto automation platform.

It is NOT a simple trading bot.

Every architectural decision must support future automation.

The goal is to build a scalable software platform.

---

# Vision

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

Automation Layer

Every layer is independent.

Every module should be replaceable.

Never tightly couple modules.

---

# Core Principles

1. Production quality only.

2. Python 3.13

3. English only.

4. SOLID.

5. DRY.

6. KISS.

7. Composition over inheritance.

8. Type hints everywhere.

9. Logging everywhere.

10. Exception handling everywhere.

11. Unit-test friendly.

12. One responsibility per class.

13. No magic numbers.

14. No duplicated logic.

15. No placeholder implementation.

16. No TODO code.

17. Never break backward compatibility unless instructed.

---

# Folder Structure

src/

core/

shared/

database/

collector/

research/

decision/

risk/

execution/

dashboard/

ai/

automation/

config/

tests/

docs/

---

# Architecture Rules

Dependencies only flow downward.

AI

↓

Dashboard

↓

Execution

↓

Decision

↓

Research

↓

Collector

↓

Database

Lower layers never import upper layers.

Never violate this rule.

---

# Shared Module

Everything exchanged between modules must live in Shared.

Examples

Candle

MarketData

Ticker

Signal

Order

Position

Portfolio

Account

Enums

Exceptions

Validators

No duplicated models.

---

# Logging

Every important action must be logged.

Never use print().

---

# Configuration

Configuration must come from config/.

Never hardcode credentials.

---

# Database

Database layer knows nothing about trading logic.

Only data persistence.

---

# Collector

Responsible only for collecting data.

Never calculate indicators.

---

# Research

Responsible for analysis.

No trading execution.

---

# Decision Engine

Produces trading signals.

Never communicates with exchange.

---

# Execution

Only executes orders.

No market prediction.

---

# Dashboard

Visualization only.

No business logic.

---

# AI Layer

AI never directly places orders.

AI provides recommendations.

Automation decides whether execution is allowed.

---

# Automation

Coordinates modules.

Never bypass Risk Engine.

---

# Risk Engine

Highest priority.

Every order passes Risk Engine.

Risk Engine can reject any signal.

---

# Coding Style

Prefer dataclass(slots=True)

Prefer Enum

Prefer ABC

Prefer Protocol

Avoid global variables.

Prefer dependency injection.

Prefer immutable objects.

---

# Commit Convention

feat:

fix:

refactor:

docs:

test:

perf:

chore:

---

# Versioning

060.x Foundation

061.x Shared

062.x Database

063.x Collector

064.x Research

065.x Decision

066.x Risk

067.x Execution

068.x Dashboard

069.x AI

070.x Automation

---

# AI Instructions

Before writing code:

1.

Read the whole repository.

2.

Understand architecture.

3.

Reuse existing code.

4.

Avoid duplicate implementation.

5.

Keep modules independent.

6.

Think before coding.

7.

Explain important design decisions.

Never rewrite architecture unless required.

Always preserve project consistency.

---

# Ultimate Goal

CryptoSystem should evolve into a complete personal crypto automation platform capable of:

collecting data

analyzing markets

making decisions

managing risk

executing trades

learning from history

assisting the owner

while remaining modular and maintainable.
