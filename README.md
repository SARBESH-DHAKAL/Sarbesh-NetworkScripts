# Sarbesh-NetworkScripts

**Sarbesh’s journey into networking and cybersecurity — real tools, real learning, real code.**

This repository contains Python-based scripts for learning and practicing computer networking concepts.  
Each tool is built with a "learn-by-doing" mindset as I explore CCNA, operating systems, and cybersecurity fundamentals.

---

## 📍 Current Tool

### 🔹 `networkScanner.py`

A multithreaded LAN scanner that:

- Accepts a subnet input like `192.168.0.0/24`
- Pings each IP in that range (using ICMP echo requests)
- Detects which hosts are alive
- Uses threading for fast parallel scanning

#### 💡 Concepts Practiced:
- IP addressing and subnetting
- ICMP protocol (`ping`)
- Threading in Python
- Subprocess module
- Basic network enumeration

---

## ▶️ How to Run

```bash
python networkScanner.py
