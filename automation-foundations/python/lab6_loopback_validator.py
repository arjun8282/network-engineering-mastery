import sys
import yaml
from ipaddress import ip_interface
def load_inventory(path: str) -> list:
    try:
        with open(path) as f:
            return yaml.safe_load(f)["fabric"]
    except FileNotFoundError:
        print(f"ERROR: file not found: {path}")
        sys.exit(2)

def validate(fabric: list) -> list:
    problems = []
    seen = {}
    for dev in fabric:
        host = dev.get("hostname", "<no-hostname>")

        if dev.get("loopback_v4") is None:
            problems.append(f"{host}: missing loopback_v4")
        
        if dev.get("loopback_v6") is None:
           problems.append(f"{host}: missing loopback_v6")

        v4=dev.get("loopback_v4")
        iface=ip_interface(v4)
        if iface.network.prefixlen !=32:
           problems.append(f"{host}: llopbacck_v4 is /{iface.network.prefixlen} , expected prefixlength /32")
              
       

        v6=dev.get("loopback_v6")
        iface6=ip_interface(v6)
        if iface6.network.prefixlen !=128:
          problems.append(f"{host}: loopback_v6 is /{iface6.network.prefixlen}, expected /128")
       
        if  v4 in seen:
           problems.append(f"{host}: loopback_v4 duplicates {seen[v4]}")
        else:
           seen[v4] = host 
    return problems

def main() -> int:
    fabric = load_inventory("inventory.yml")
    print(f"Loaded {len(fabric)} devices")

    problems = validate(fabric)

    if problems:
        print(f"FAILED - {len(problems)} problem(s) found:")
        for p in problems:
            print(f"  {p}")
        return 1

    print("PASSED - all loopbacks clean")
    return 0

if __name__ == "__main__":
    sys.exit(main())
