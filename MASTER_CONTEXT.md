# Network Engineering Mastery — Master Context
## Session Info
Last updated: 2026-06-16
Current phase: Automation Foundations — IN PROGRESS
Module 5 (NAPALM) COMPLETE
Next session: Module 6 — Nornir

## Student Profile
- Protocol knowledge: beginner
- Python/automation knowledge: Modules 1-5 complete
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
6. Nornir                 ← NEXT
7. Ansible
8. REST API (requests)
9. pyATS/Genie + Pytest

#### Module 5 — NAPALM ✓
- NAPALM vs Netmiko: structured getters vs raw strings,
  config lifecycle vs blind push
- NOS concept: management plane + control plane + data plane
- VyOS vs FRR: VyOS is a full NOS (FRR under the hood,
  commit/rollback session model). FRR is a routing daemon
  suite — no management plane of its own.
- Core drivers: EOS, IOS, IOS-XR, NX-OS, JunOS
- napalm-vyos: community driver, VyOS is lab proxy
- Driver pattern: get_network_driver → instantiate → open()
- Context manager: preferred production pattern
- Getters: get_facts(), get_interfaces() — normalized
  dict return across all vendors
- Config lifecycle: load_merge_candidate → compare_config
  → commit_config or discard_config → rollback
- Full pipeline: YAML inventory → Jinja2 → NAPALM
  load/diff/commit
- Dict inventory with .items() — why two variables needed
- List of strings vs list of dicts in YAML — key distinction
  for Jinja2 template access patterns
- lab11_napalm_getters.py ✓
- lab12_napalm_pipeline.py ✓ (interface descriptions)
- lab13_ntp_pipeline.py ✓ (NTP + DNS + interfaces)
- Execution deferred — VyOS EC2 not yet provisioned

## Teaching Notes
- Do NOT ask for output confirmation — student reports errors
- Student actively questions design decisions — answer directly
- Student pushes back on over-engineering — keep it lean
- Student writes scripts independently — confidence growing
- Build one concept at a time before full scripts
- .items() introduced this module — now part of vocabulary
- List of strings vs list of dicts now understood

## Where We Stopped
Module 5 NAPALM complete and pushed to GitHub.
VyOS
