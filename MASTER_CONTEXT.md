# Network Engineering Mastery — Master Context

## Session Info
Last updated: 2026-06-01
Current phase: Automation Foundations — IN PROGRESS
Module 1 (Python for Networking) Part 1 COMPLETE
Next session: Module 1 Part 2 — functions, file I/O,
              YAML inventory, error handling
              (the bridge into Netmiko)

## Student Profile
- Protocol knowledge: beginner
- Python/automation knowledge: just started
  (completed Python basics Part 1)
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
(full concept list confirmed solid — see prior context)

## In-Progress Phase

### Automation Foundations — IN PROGRESS
Phase module order:
1. Python for Networking  ← Part 1 done, Part 2 next
2. Git workflow
3. Jinja2
4. Netmiko
5. NAPALM
6. Nornir
7. Ansible
8. REST API (requests)
9. pyATS/Genie + Pytest (permanent every phase after)

#### Module 1 Part 1 — Python for Networking ✓
- venv created (~/netauto/venv) — all phase tooling lives here
- Variables, f-strings, lists, loops, dictionaries
- Core mental model: "a network is data"
  (device = dict, fabric = list of dicts)
- ipaddress module:
  ip_interface, ip_network, num_addresses,
  is_private (RFC 1918), is_link_local (RFC 4291),
  .version for dual-stack
- Dual-stack enforced from day one of automation
- Broken lab (3 bugs: missing colon, dict key typo,
  = vs ==) found and fixed
- Files committed: lab1.py, lab2.py,
  lab3_broken_fixed.py, README.md

#### Module 1 Part 1 — interview Qs (to discuss at start of Part 2)
1. Validate 500 leaf loopbacks for overlap/dupes pre-push
2. Why structured inventory vs hardcoded config strings
3. Dual-stack: IPv6 silently skipped — use .version to catch

## Where We Stopped
Module 1 Part 1 complete and pushed.
Next: Module 1 Part 2 (functions, file I/O, YAML, errors).
EC2 instance STOPPED (not terminated) in ap-south-1.
venv at ~/netauto/venv on the instance.
FRRouting installed and verified.

## Open Questions
None. Part 1 interview questions queued for Part 2.

## Lab Environment
- AWS EC2 (free tier + minimal cost)
- Region: ap-south-1 (Mumbai)
- Python venv: ~/netauto/venv
- Routers: FRRouting, Cumulus, VyOS, Bird2
- No GNS3, no EVE-NG
- Namespace labs for local concept verification

## Git Repo Status
- Repo: https://github.com/arjun8282/network-engineering-mastery.git
- MASTER_CONTEXT.md: up to date
- phase0-prerequisites/README.md ✓
- phase0.5-dc-architecture/README.md ✓
- automation-foundations/python/ (lab1, lab2,
  lab3_broken_fixed, README.md) ✓
- automation-foundations/tests/ (created, empty)
- lab-journal/ (created)

## Decisions Locked
- Woven automation in every phase
- IPv4 + IPv6 dual stack throughout
- Mixed routers: FRRouting, Cumulus, VyOS, Bird2
- 7 month target
- Model switching: Claude instructs when to switch
  to Opus and back. Automation Foundations stays on
  current (non-Opus) model — no dense RFC internals.
- Git: Claude provides all commands, student copy-pastes
- AWS: console explained when needed, every CLI
  command explained before running

## Curriculum Order
Phase 0   → Prerequisites ✓
Phase 0.5 → DC Architecture ✓
Auto      → Automation Foundations ← IN PROGRESS (M1 P1 done)
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
- All curriculum decisions finalized
- Project Instructions set in Claude Project
- Never hallucinate theory — RFC references accurate
- Every AWS command explained before running
- Automation woven into every phase immediately
  after manual CLI lab
- Lab stages: guided → complexity → production → broken
