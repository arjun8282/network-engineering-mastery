cat > ~/network-engineering-mastery/MASTER_CONTEXT.md << 'EOF'
# Network Engineering Mastery — Master Context
## Session Info
Last updated: 2026-06-24
Current phase: Automation Foundations — IN PROGRESS
Module 8 (Ansible) COMPLETE
Next session: Module 9 — pyATS/Genie + Pytest

## Student Profile
- Protocol knowledge: beginner
- Python/automation knowledge: Modules 1-8 complete
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
7. REST API (requests)    ✓ COMPLETE
8. Ansible                ✓ COMPLETE
9. pyATS/Genie + Pytest   ← NEXT

#### Module 8 — Ansible ✓
- WHY Ansible: declarative vs imperative — describe end state,
  not steps; Ansible figures out what needs to change
- Agentless, push-based over SSH
- Control node pushes to targets; nothing installed on devices
- Inventory: INI format, groups, host variables
- group_vars/: files named after group loaded automatically
- host_vars/: files named after host loaded automatically
- Naming rule: filename must match group or host name exactly
- ansible_connection=local: no SSH, runs on control node itself
- Playbook: YAML file, one or more plays
- Play: maps hosts group to list of tasks
- Task: calls one module
- Module: unit of idempotent work
- gather_facts: true — Ansible collects system variables before
  tasks run (ansible_distribution, ansible_date_time,
  inventory_hostname, etc.)
- ansible.builtin.debug: prints messages, diagnostic only
- ansible.builtin.apt: package management, state=present
- ansible.builtin.file: ensures path exists with correct perms
- ansible.builtin.template: renders Jinja2 template to target
- ansible.builtin.service: manages services
- become: true — privilege escalation (sudo)
- state: present — idempotency declaration, not a command
- Idempotency: changed vs ok — safe to run repeatedly
- Handlers: only fire when notified task returns changed
- notify: pointer to handler by name; surgical restarts only
- Ansible Vault: encrypts secrets at rest, decrypts in memory
- ansible-vault create: creates encrypted file
- ansible-vault view: inspect encrypted file
- --ask-vault-pass: prompt for password at runtime
- Vault file must be named after group/host to auto-load
- Jinja2 templating: Module 3 syntax works natively in Ansible
- PLAY RECAP: ok/changed/failed — failed=0 is the key check
- playbook.yaml, ansible.cfg, inventory.ini committed to GitHub
- group_vars/control.yaml: NTP servers (plaintext)
- host_vars/localhost.yaml: secrets (vault encrypted)
- templates/ntp.conf.j2: Jinja2 template with facts + vars

#### Module 7 — REST API (requests) ✓
- WHY REST: machine interface vs human interface
- REST is not an RFC — Roy Fielding's 2000 PhD dissertation
- HTTP semantics: RFC 9110
- JSON: RFC 8259
- Forward pointer: RESTCONF is RFC 8040 (Phase 2)
- Resources + Methods + Status codes
- Idempotency: GET, PUT, DELETE idempotent; POST is not
- Response object: .status_code, .headers, .text, .json()
- Session: persistent TCP + headers set once
- Error handling: timeout=, raise_for_status(), RequestException
- Pagination via Link header rel="next"
- lab18_rest_api.py ✓
- lab19_rest_api_pagination.py ✓

#### Module 6 — Nornir ✓
- WHY Nornir: sequential loop, per-script plumbing, no standard
  result shape — all three solved
- Plugin-based: nornir-utils, nornir-netmiko, nornir-napalm
- SimpleInventory: hosts/groups/defaults
- Inheritance: host → group → defaults
- Task: function handling ONE host; Nornir fans out
- Runner: threaded, num_workers controls concurrency
- Result: AggregatedResult → MultiResult → Result
- Filtering: nr.filter() with F object
- lab14–17 complete, execution deferred to multi-router phase

## Teaching Notes
- Do NOT ask for output confirmation — student reports errors
- Student actively questions design decisions — answer directly
- Student pushes back on over-engineering — keep it lean
- Student writes scripts independently before requesting help
- Build one concept at a time before full scripts
- Make the problem visible before introducing the solution
- Always include full imports in every REPL snippet
- Recurring errors to anticipate:
  - Capitalization errors on class/method names
  - .json vs .json() attribute vs method
  - Missing f-string prefix
  - Indentation breaks in multi-block scripts

## Where We Stopped
Module 8 Ansible complete. All files committed to GitHub under
automation-foundations/ansible/.
Next: Module 9 pyATS/Genie + Pytest.
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
- automation-foundations/rest-api/ ✓
- automation-foundations/ansible/ ✓
- lab-journal/ ✓
EOF
