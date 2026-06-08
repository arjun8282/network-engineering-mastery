import sys
import yaml
from jinja2 import Environment, FileSystemLoader


def  load_inventory(path):
     try:
         with open(path) as f:
               return yaml.safe_load(f)['devices']
     except FileNotFoundError:
            print(f"({path} is  wrong , couldn t find {path}")
            sys.exit(2)

def main():
          data=load_inventory("practice_inventory.yml")
          env = Environment(loader=FileSystemLoader("templates"))
          template=env.get_template("loopback.j2")

          for  device in  data:
              print(f"({device['name']}")
              print(template.render(device))
              print()


if __name__ == "__main__":
     main()
               

