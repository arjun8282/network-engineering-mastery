import  yaml
import sys

def load_inventory(path):
     try:
        with open(path) as f:
             return  yaml.safe_load(f)["fabric"]

     except FileNotFoundError:
         print(f"the {path} is wrong . File not found ")
         sys.exit(2)


def validate(fabric):
   problems=[]
   seen ={}
   for dev in fabric:
         host = dev.get("hostname" , "<no_hostname>" )
         asn = dev.get("asn")
         if asn is None:
            problems.append(f"{host} has no asn ") 
         elif not  (1 <= asn <= 65535):
           problems.append(f"{host} has invalid ASN")
        
         if asn in seen:
           problems.append(f"{host}:{asn}  duplicates {seen[asn]}")
         else:
           seen[asn] =  host
   return problems 
def main():
    fabric = load_inventory("inventory.yml")
    print(f"loaded {len(fabric)} devices")
    problems = validate(fabric)
    if problems:
       print(f"Failed-{len(problems)} problems:")
       for p in problems:
           print(f"{p}")
       return 1
    print("passsed-all ASN clean")
    return 0      
if __name__ == "__main__":
     sys.exit(main())
