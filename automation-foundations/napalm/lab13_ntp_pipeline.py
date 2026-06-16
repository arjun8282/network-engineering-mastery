import yaml 
from jinja2 import Environment,FileSystemLoader
from napalm import get_network_driver



def load_inventory(path):
    try:
      with open (path) as f:
            return  yaml.safe_load(f)['devices']

    except FileNotFoundError:
          print(f" the file {path} yu gave is wrong . please provide correct file")


def render_config(dev_data):
    env=Environment(loader=FileSystemLoader("templates"))
    template=env.get_template("ntp.j2")
    return template.render(interfaces=dev_data['interfaces'], ntp_servers=dev_data['ntp_servers'],dns_servers=dev_data['dns_servers'])



def push_config(inventory):
    
    for dev_name,dev_data in inventory.items():
        driver=get_network_driver(dev_data['driver'])
        config=render_config(dev_data)
        try: 
           with driver(
                hostname=dev_data['hostname'],
                username=dev_data['username'],
                password=dev_data['password'],
                optional_args={'key_file': dev_data['key_file']}
             ) as device:

                device.load_merge_candidate(config=config)
                diff = device.compare_config()

                if diff:
                   print(diff)
                   device.commit_config()
                else:
                    print(f"No changes for {dev_name} — discarding.")
                    device.discard_config()

        except Exception as e:
            print(f"Failed on {dev_name}: {e}")   


   


def main():
    inventory=load_inventory("lab13_inventory.yaml")
    push_config(inventory)


if __name__ == '__main__':
    main()
