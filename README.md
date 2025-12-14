# EC2 SSH Health Check

This project demonstrates a basic health check for an AWS EC2 instance by verifying
network reachability on the SSH port (22) using a Python script.

The goal is to simulate a simple monitoring probe similar to what is used in
cloud engineering and SRE workflows.

## What This Project Does
- Connects to a remote host using TCP
- Verifies whether port 22 (SSH) is reachable
- Reports HEALTHY or UNHEALTHY with a failure reason

## Technologies Used
- AWS EC2 (Amazon Linux)
- Python 3
- TCP socket networking

## How to Run
```bash
python health_check.py <EC2_PUBLIC_IP>
