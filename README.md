# Network Port Scanner

A lightweight Python-based port scanning tool designed to scan target IP addresses or domain names for open TCP ports and identify active services.

## Features

* **TCP Port Scanning:** Scans single ports or range of ports.
* **Service Detection:** Identifies standard service names running on open ports (e.g., HTTP, SSH, FTP).
* **Customizable Range:** Allows user to specify custom port ranges (e.g., 1-1024).
* **Error Handling:** Gracefully handles invalid IP addresses, hostname resolution failures, and connection timeouts.

## Requirements & Prerequisites

* Operating System: Linux / macOS / Windows
* Language: Python 3.x
* Required Libraries: Standard Library (`socket`, `sys`, `threading` if applicable)

## Installation & Setup

Clone the repository to your local machine:

```bash
git clone https://github.com/Mesbamahib007/Port-Scanner.git
cd Port-Scanner
