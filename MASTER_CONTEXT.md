# Network Engineering Mastery — Master Context
## Session Info
Last updated: 2026-06-09
Current phase: Automation Foundations — IN PROGRESS
Module 4 (Netmiko) COMPLETE
Next session: Module 5 — NAPALM

## Student Profile
- Protocol knowledge: beginner
- Python/automation knowledge: Modules 1-4 complete
- Goal: FAANG/NVIDIA network engineer role
- Timeline: 7 months
- GitHub: https://github.com/arjun8282/network-engineering-mastery.git

## Completed Phases
### Phase 0 — Prerequisites ✓
### Phase 0.5 — DC Architecture ✓

## In-Progress Phase
### Automation Foundations — IN PROGRESS
Module order:
1. Python for Networking  ✓ COMPLETE
2. Git workflow           ✓ COMPLETE
3. Jinja2                 ✓ COMPLETE
4. Netmiko                ✓ COMPLETE
5. NAPALM                 ← NEXT
6. Nornir
7. Ansible
8. REST API (requests)
9. pyATS/Genie + Pytest

#### Module 4 — Netmiko ✓
- ConnectHandler as the SSH entry point
- device_type as the central concept — linux, vyos etc.
- send_command for pulling show output
- vtysh -c chaining for pushing FRR config
- send_config_set limitation with device_type linux explained
- YAML inventory driving device connections
- Jinja2 + Netmiko full pipeline: YAML → template → command string → SSH → FRR
- subprocess.run for OS-level commands in teardown
- lab8_first_connection.py, lab9_send_config.py, lab10_jinja_netmiko.py, lab_teardown.py
- Key insight: send_config_set works for proper Netmiko device types like VyOS — FRR requires explicit vtysh driving via device_type linux

## Teaching Notes
- Student learns best with small examples first,
  one concept at a time, before any full script
- Always explain every line before student types it
- Never give a full script without building up to it
- Build scripts incrementally — one function at a time
- Confirm output at every step before moving on
- Student flags when output pasting is unnecessary —
  trust them to report errors, don't demand every output
- Student actively questions why things are done a
  certain way — answer directly before moving on
- Student writes independently and catches missing
  patterns (try/except, functions) — confidence growing
- Student pushes back on over-engineering —
  single-line wrapper functions rejected, keep it lean

## Where We Stopped
Module 4 Netmiko complete and pushed to GitHub.
Next: Module 5 — NAPALM.
EC2 instance: STOP after this session.
Region: ap-south-1. venv: ~/netauto/venv.

## Lab Environment
- AWS EC2 (ap-south-1, Mumbai)
- Elastic IP configured — static, no config update needed
- Python venv: ~/netauto/venv
- VS Code Remote SSH: host ec2-netauto in ~/.ssh/config
- Routers: FRRouting, Cumulus, VyOS, Bird2
- Repo: ~/network-engineering-mastery
- Netmiko lab key: ~/.ssh/netmiko_lab (EC2 self-SSH)

## Git Repo Status
- MASTER_CONTEXT.md: up to date
- automation-foundations/python/ ✓
- automation-foundations/jinja2/ ✓
- automation-foundations/netmiko/ ✓
- lab-journal/ ✓
