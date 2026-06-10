from napalm import get_network_driver
import json

driver = get_network_driver('vyos')

with driver(
    hostname='172.31.x.x',
    username='vyos',
    password='',
    optional_args={'key_file': '/home/ubuntu/.ssh/netmiko_lab'}
) as device:

 

      facts = device.get_facts()
      print("===FACTS===")
      print(json.dumps(facts, indent=2))


      interfaces=device.get_interface()
      print("===INterfaces==")
      print(json.dumps(interfaces, indent=2))

      print("loading candidate config ")
      device.load.merge_candidate(
            config="set interfaces ethernet eth1 description 'NAPALM-MANAGED'"
      )
      print("\n=== Diff ===")
      diff = device.compare_config()
      print(diff)

      if diff:
         print("\n=== Committing ===")
         device.commit_config()
         print("Committed.")
      else:
         print("No changes — discarding.")
         device.discard_config()
      
