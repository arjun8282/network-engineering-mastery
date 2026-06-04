# Network Engineering Mastery — Master Context

## Session Info
Last updated: 2026-06-04
Current phase: Automation Foundations — IN PROGRESS
Module 1 (Python for Networking) COMPLETE
Next session: Module 2 — Git workflow + VS Code Remote SSH setup

## Student Profile
- Protocol knowledge: beginner
- Python/automation knowledge: Module 1 complete
- Goal: FAANG/NVIDIA network engineer role
- Timeline: 7 months
- GitHub: https://github.com/arjun8282/network-engineering-mastery.git

## Completed Phases

### Phase 0 — Prerequisites ✓
- Host vs router (ip_forward)
- RIB vs FIB
- Longest Prefix Match — verified with live lab
- ARP — L2/L3 resolution, STALE/REACHABLE/FAILED
- Link-local IPv6 addresses (fe80::)
- TCP vs UDP — why each protocol chose what it did
- BGP=TCP 179, OSPF=IP 89, IS-IS=L2,
  BFD=UDP 3784, VXLAN=UDP 4789
- Namespace lab: h1—r1—h2 dual stack
  built, verified, broken and fixed

### Phase 0.5 — DC Architecture ✓
- Gen 1: 3-tier, STP problems, east-west, failure domains
- Gen 2: Spine-leaf/Clos, ECMP, BGP underlay (RFC 7938),
  dual-ToR, MLAG concept
- Gen 3: Multi-pod/super-spine, pod scaling
- Gen 4: Multi-DC/DCI, border leaf, EVPN Type-5,
  transit vs peering vs IXP
- Gen 5: AI/GPU clusters, rail-optimized, RoCEv2,
  PFC/ECN/DCQCN, 3 fabrics, DGX SuperPOD

## In-Progress Phase

### Automation Foundations — IN PROGRESS
Module order:
1. Python for Networking  ✓ COMPLETE
2. Git workflow           ← NEXT (+ VS Code Remote SSH setup)
3. Jinja2
4. Netmiko
5. NAPALM
6. Nornir
7. Ansible
8. REST API (requests)
9. pyATS/Genie + Pytest (permanent every phase after)

#### Module 1 — Python for Networking ✓ COMPLETE

Part 1 ✓
- venv created (~/netauto/venv)
- Variables, f-strings, lists, loops, dictionaries
- Core mental model: "a network is data"
- ipaddress module: ip_interface, ip_network,
  num_addresses, is_private (RFC 1918),
  is_link_local (RFC 4291), .version for dual-stack
- Dual-stack enforced from day one
- Broken lab: 3 bugs found and fixed

Part 2 ✓
- Functions: def, parameters, return, default
  arguments (family=4), reusability
- Type hints: PEP 484, labels only, not enforced
- .get() on dicts: safe access with fallback
- __name__ == "__main__": protects demo code
  from running on import
- YAML: spaces not tabs, dash = list item,
  key: value = dict, yaml.safe_load always
- File I/O: open(), with block (auto-closes)
- Error handling: try/except FileNotFoundError,
  sys.exit() with exit codes (0=pass, 1=fail, 2=error)
- Built loopback validator from scratch:
  checks missing v4/v6, wrong prefix length,
  duplicate loopbacks, exits with correct code
  for CI gating
- Key insight: YAML → safe_load → same Python
  list of dicts → loop + function = Ansible/Nornir
  skeleton
- Filed committed: lab6_loopback_validator.py,
  inventory.yml

## Teaching Notes
- Student learns best with small examples first,
  one concept at a time, before any full script
- Always explain every line before student types it
- Never give a full script without building up to it
- Confirm output at every step before moving on
- Student gets frustrated with long scripts dumped
  at once — always build incrementally

## Where We Stopped
Module 1 complete and pushed to GitHub.
Next: Module 2 — Git workflow + VS Code Remote SSH.
EC2 instance: STOPPED (not terminated), ap-south-1.
Repo cloned on EC2 at ~/network-engineering-mastery.
venv at ~/netauto/venv. PyYAML installed.
GitHub PAT created and working for push from EC2.

## Open Questions
None.

## Lab Environment
- AWS EC2 (free tier + minimal cost)
- Region: ap-south-1 (Mumbai)
- Python venv: ~/netauto/venv
- Routers: FRRouting, Cumulus, VyOS, Bird2
- No GNS3, no EVE-NG
- Namespace labs for local concept verification
- Repo cloned on EC2: ~/network-engineering-mastery

## Git Repo Status
- Repo: https://github.com/arjun8282/network-engineering-mastery.git
- MASTER_CONTEXT.md: up to date
- phase0-prerequisites/README.md ✓
- phase0.5-dc-architecture/README.md ✓
- automation-foundations/python/
  lab6_loopback_validator.py ✓
  inventory.yml ✓
- automation-foundations/tests/ (created, empty)
- lab-journal/ (created)

## Decisions Locked
- Woven automation in every phase
- IPv4 + IPv6 dual stack throughout
- Mixed routers: FRRouting, Cumulus, VyOS, Bird2
- 7 month target
- Model switching: Automation Foundations stays
  on current (non-Opus) model
- Git: Claude provides all commands, student
  copy-pastes
- AWS: every command explained before running
- Teaching pace: small examples first, one concept
  at a time, explain every line, confirm before
  moving on

## Curriculum Order
Phase 0   → Prerequisites ✓
Phase 0.5 → DC Architecture ✓
Auto      → Automation Foundations ← IN PROGRESS
Phase 1   → OSPF + IS-IS
Phase 2   → BGP
Phase 3   → Traffic Engineering
Phase 4   → MPLS
Phase 5   → VXLAN + EVPN
Phase 6   → Combinations + Real Designs
Phase 7   → Design Mastery + Interviews

## Additional Topics (post-curriculum)
Saved in Claude memory — multicast, QoS, RoCEv2/DCB,
VRRP/HSRP, OSPFv3, TI-LFA, OpenConfig, YANG/NETCONF,
BGP GR/LLGR, ECMP hashing deep dive, MLAG deep dive,
PBR, UDLD, Ethernet OAM/CFM, LACP deep dive

## Notes
- Never hallucinate theory — RFC references accurate
- Every AWS command explained before running
- Automation woven into every phase immediately
  after manual CLI lab
- Lab stages: guided → complexity → production → broken
- Student pace: needs examples before scripts,
  confirmation at every step, never dump full scripts
