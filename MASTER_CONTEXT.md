# Network Engineering Mastery — Master Context

## Session Info
Last updated: 2026-05-30
Current phase: Phase 0 COMPLETE
Next session starts: Phase 0.5 — DC Architecture
                     (begin with AWS setup first)

## Student Profile
- Protocol knowledge: beginner
- Python/automation knowledge: zero
- Goal: FAANG/NVIDIA network engineer role
- Timeline: 7 months
- GitHub: https://github.com/arjun8282/network-engineering-mastery

## Completed Phases
- Phase 0: Prerequisites ✓
  - Host vs router (ip_forward)
  - RIB vs FIB
  - Longest prefix match — verified with live lab
  - ARP — L2/L3 resolution, STALE/REACHABLE/FAILED
  - Link-local IPv6 addresses (fe80::)
  - TCP vs UDP — why each protocol chose what it did
  - BGP=TCP 179, OSPF=IP 89, IS-IS=L2,
    BFD=UDP 3784, VXLAN=UDP 4789
  - Namespace lab: h1—r1—h2 dual stack built,
    verified, broken and fixed

## Current Phase
Current phase: Phase 0.5 COMPLETE
Next session: Automation Foundations
              Python basics for networking
Status: All concepts confirmed solid including
        L2/L3 boundary, routed ports, why
        broadcasts stop at spine uplinks,
        VXLAN purpose now clear
EC2 Instance: stopped (not terminated,
              needed for future labs)
## Where We Stopped
Phase 0 complete. Clean slate for Phase 0.5.
AWS setup instructions already given in previous
chat — student has AWS account ready.

## Open Questions
None — Phase 0 concepts confirmed solid.

## Lab Environment
- AWS EC2 (free tier + minimal cost)
- Routers: FRRouting, Cumulus Linux, VyOS, Bird2
- No GNS3, no EVE-NG
- Namespace labs for local concept verification

## Git Repo Status
- Repo: https://github.com/arjun8282/network-engineering-mastery
- MASTER_CONTEXT.md: pushing now
- Phase 0 lab folder: needs to be created

## Notes
- All curriculum decisions finalized
- Project Instructions set in Claude Project
- Model switching: Claude instructs when to
  switch to Opus and back
- Woven automation approach confirmed
- IPv4 + IPv6 dual stack throughout
