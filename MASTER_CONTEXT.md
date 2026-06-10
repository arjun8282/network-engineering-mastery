# Network Engineering Mastery — Master Context
## Session Info
Last updated: 2026-06-10
Current phase: Automation Foundations — IN PROGRESS
Module 5 (NAPALM) IN PROGRESS
Next session: Complete Module 5 execution against VyOS, then Module 6 Nornir

## Student Profile
- Protocol knowledge: beginner
- Python/automation knowledge: Modules 1-5 in progress
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
5. NAPALM                 ← IN PROGRESS
6. Nornir
7. Ansible
8. REST API (requests)
9. pyATS/Genie + Pytest

#### Module 5 — NAPALM (IN PROGRESS)
Concepts covered:
- NAPALM vs Netmiko: structured getters vs raw strings,
  config lifecycle vs blind push
- NOS concept: management plane + control plane + data plane
- VyOS vs FRR: VyOS is a full NOS (Debian-based, FRR under the hood,
  commit/rollback session model). FRR is a routing daemon suite
  installed on top of Linux — no management plane of its own.
- Core NAPALM drivers: EOS, IOS, IOS-XR, NX-OS, JunOS (the five
  platforms you'll meet at FAANG/NVIDIA)
- napalm-vyos: community driver, VyOS is the lab proxy for
  commercial NOS behavior
- Driver pattern: get_network_driver → instantiate → open()
  (two-step separation from Netmiko's single-step ConnectHandler)
- Context manager pattern: preferred production approach,
  auto open/close even on exception
- Getters: get_facts(), get_interfaces() — normalized dict
  return across all vendors, same keys regardless of platform
- Config lifecycle: load_merge_candidate / load_replace_candidate
  → compare_config() → commit_config() or discard_config()
  → rollback() if needed
- if diff: guard before committing — prevents unnecessary
  config churn in production

Lab files:
- automation-foundations/napalm/lab11_napalm_getters.py ✓ written,
  pending execution against real VyOS

Deferred: VyOS EC2 spin-up deferred to when multi-router
environment is needed. Script is ready — update IP and runs.

#### Module 4 — Netmiko ✓
- ConnectHandler, device_type, send_command
- vtysh -c chaining for FRR config push
- YAML inventory, Jinja2+Netmiko full pipeline
- lab8, lab9, lab10, lab_teardown committed

## Teaching Notes
- Student learns best with small examples first,
  one concept at a time, before any full script
- Always explain every line before student types it
- Never give a full script without building up to it
- Build scripts incrementally — one function at a time
- Do NOT ask for output confirmation at each step —
  student reports errors, session moves at pace
- Student actively questions why — answer directly
- Student pushes back on over-engineering — keep it lean
- Student flags typos and catches errors independently
  — confidence growing

## Where We Stopped
Module 5 NAPALM concepts complete. Script written.
Execution pending VyOS EC2.
Next: Module 6 Nornir (works on existing Ubuntu EC2 with FRR).
EC2: STOP after this session.
Region: ap-south-1. venv: ~/netauto/venv.

## Lab Environment
- AWS EC2 (ap-south-1, Mumbai)
- Elastic IP configured
- Python venv: ~/netauto/venv
- VS Code Remote SSH: host ec2-netauto
- Routers: FRRouting (active), VyOS (pending EC2)
- Repo: ~/network-engineering-mastery

## Git Repo Status
- MASTER_CONTEXT.md: up to date
- automation-foundations/python/ ✓
- automation-foundations/jinja2/ ✓
- automation-foundations/netmiko/ ✓
- automation-foundations/napalm/ ✓ (lab11 written)
- lab-journal/ ✓
