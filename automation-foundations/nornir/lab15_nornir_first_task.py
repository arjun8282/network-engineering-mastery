from nornir import InitNornir
from nornir.core.task import Task, Result

def check_in(task):
    if task.host.name == "vyos2":
       raise ValueError("Simulated device unreachable")
    return Result(host=task.host, result=f"ok fronm the {task.host.name}")

def main():
    nr = InitNornir(
        runner={"plugin": "threaded", "options": {"num_workers": 5}},
        inventory={
            "plugin": "SimpleInventory",
            "options": {
                "host_file": "hosts.yaml",
                "group_file": "groups.yaml",
                "defaults_file": "defaults.yaml",
            },
        },
    )

    result = nr.run(task=check_in)
   

    print("any failures:", result.failed)
    print("host which failed:", result.failed_hosts.keys())
    print("-" * 40)

    for host_name, multi_result in result.items():
       single =multi_result[0]
       if single.failed:
          print(f"{host_name}: FAILED -> {single.exception}")
       else:
          print(f"{host_name}:{single.result}")

if __name__ == "__main__":
     main() 
