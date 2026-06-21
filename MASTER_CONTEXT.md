# Network Engineering Mastery — Master Context
## Session Info
Last updated: 2026-06-21
Current phase: Automation Foundations — IN PROGRESS
Module 6 (Nornir) COMPLETE
Next session: Module 7 — REST API (requests)

## Student Profile
- Protocol knowledge: beginner
- Python/automation knowledge: Modules 1-6 complete
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
5. NAPALM                 ✓ COMPLETE
6. Nornir                 ✓ COMPLETE
7. REST API (requests)    ← NEXT
8. Ansible
9. pyATS/Genie + Pytest

#### Module 6 — Nornir ✓
- WHY Nornir: sequential loop problem, per-script plumbing
  repetition, no standard result shape — all three solved
- Plugin-based architecture: nornir core is minimal;
  nornir-utils, nornir-netmiko, nornir-napalm, nornir-jinja2
  are separate installs
- SimpleInventory: three-file structure (hosts/groups/defaults)
- Inheritance / resolution order: host → group → defaults;
  write credentials once, override where needed
- hosts.yaml: unique-per-device (hostname, data, groups)
- groups.yaml: shared-by-category (e.g. vyos_routers username)
- defaults.yaml: fallback for everyone
- data: free-form dict on hosts/groups for role, ASN, etc.
- InitNornir: config via inline dict or config.yaml
- Task: a function that handles ONE host; Nornir fans it out
- Runner: threaded, num_workers controls concurrency
- num_workers: 1 vs 5 — wall-clock demo with sleep(2)
  confirmed ~10s serial vs ~2s parallel
- Result hierarchy: AggregatedResult → MultiResult → Result
- AggregatedResult.failed, .failed_hosts — whole-run health
- MultiResult[0] — single Result for a simple task
- Result.result, .failed, .exception — per-host outcome
- Per-host failure handling: exception on one host does NOT
  crash the run; Nornir catches and records it
- Filtering: nr.filter() returns a new Nornir object (original
  untouched), scopes blast radius
- Simple filter: nr.filter(role="leaf") — kwargs match on
  host attributes and data fields
- F object: F(groups__contains="vyos_routers") for group
  membership and other non-equality checks
- Boolean logic: F(...) & F(...), F(...) | F(...), ~F(...)
- lab14_nornir_inventory.py ✓ (built incrementally:
  single device → defaults inheritance → groups)
- lab15_nornir_first_task.py ✓ (task + threaded runner,
  num_workers concurrency demo)
- lab16_nornir_results.py ✓ (AggregatedResult/MultiResult/
  Result hierarchy, per-host failure handling)
- lab17_nornir_filter.py ✓ (simple kwargs, F object,
  group/data/logic, scoped run)
- Execution deferred — multi-router EC2 not yet provisioned

## Teaching Notes
- Do NOT ask for output confirmation — student reports errors
- Student actively questions design decisions — answer directly
- Student pushes back on over-engineering — keep it lean
- Student writes scripts independently — confidence growing
- Build one concept at a time before full scripts
- Make the problem visible before introducing the solution
- .items() introduced Module 5 — part of vocabulary
- List of strings vs list of dicts — understood
- Incremental inventory build (1 file → 2 files → 3 files)
  worked well — use same pattern for new concepts
- Module order changed: REST API moved before Ansible

## Where We Stopped
Module 6 Nornir complete and pushed to GitHub.
Multi-router EC2 deferred — provisioned before Phase 1 IGP.
Next: Module 7 REST API — works on existing Ubuntu EC2.
EC2: STOP after this session.
Region: ap-south-1. venv: ~/netauto/venv.

## Curriculum Decisions Locked
- Order: Phase 0 → 0.5 → Auto Foundations → 1 IGP → 2 BGP
  → 3 TE → 4 MPLS → 5 DC → 6 Combinations → 7 Design
- Automation woven into every phase
- IPv4 + IPv6 dual stack throughout
- Mixed routers: FRRouting, Cumulus Linux, VyOS, Bird2 on EC2
- No GNS3, no EVE-NG — AWS only, teardown scripts always
- Multi-router EC2 provisioned before Phase 1 begins

## Automation Tools by Phase
- Foundations: Python, Netmiko, NAPALM, Nornir, Ansible,
  REST API, Jinja2, Git
- Phase 1: above tools applied to IGPs
- Phase 2+: RESTCONF added
- Phase 3+: NETCONF, gNMI added
- Phase 5+: Terraform, Containerlab added
- Phase 6+: CI/CD, Nautobot added

## Additional Topics Woven In
- BFD: IGP and BGP phases
- MLAG/MC-LAG: Phase 5
- ECMP hashing: Phase 2 and 5
- pyATS/Genie + Pytest: every phase

## Post-Curriculum Topics (saved)
Multicast, QoS, RoCEv2/DCB, VRRP/HSRP, OSPFv3, TI-LFA,
OpenConfig, YANG/NETCONF, BGP GR/LLGR, MLAG deep dive,
PBR, UDLD, Ethernet OAM, LACP

## Model Switching Protocol
- Sonnet: Automation Foundations (current)
- Opus: dense RFC internals, IGP/BGP protocol material
- Claude explicitly says "switch to Opus" / "switch back to Sonnet"
- Student switches manually via model selector
- Never assume model — always wait for the instruction

## Lab Environment
- AWS EC2 (ap-south-1, Mumbai)
- Elastic IP configured
- Python venv: ~/netauto/venv
- VS Code Remote SSH: host ec2-netauto
- Routers: FRRouting (active), VyOS (pending multi-router EC2)
- Repo: ~/network-engineering-mastery

## Git Repo Status
- MASTER_CONTEXT.md: up to date
- automation-foundations/python/ ✓
- automation-foundations/jinja2/ ✓
- automation-foundations/netmiko/ ✓
- automation-foundations/napalm/ ✓
- automation-foundations/nornir/ ✓
- lab-journal/ ✓
