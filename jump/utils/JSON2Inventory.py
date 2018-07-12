import json
import sys

with open(sys.argv[1]) as json_data:
    data = json.load(json_data)
    agents = ""
    managers = ""

    for element in data:
      hostname = element['hostname']
      ip = element['IP']
      identifier = str(element['ID'])

      if hostname == 'Agent':
        #print('[Agents]')
        agents = agents + hostname + identifier + ' ansible_host=' + ip
        agents += '\n'
      else:
        managers = managers + hostname + identifier + ' ansible_host=' + ip

    print("[Agents]")
    print(agents)
    print("[Managers]")
    print(managers)
    print("\n")

    print("[Agents:vars]")
    print("ansible_user=vagrant ansible_ssh_private_key_file=" + sys.argv[2] + " ansible_ssh_common_args='-o StrictHostKeyChecking=no'")
    print("\n")
    print("[Managers:vars]")
    print("ansible_user=vagrant ansible_ssh_private_key_file=" + sys.argv[2] + " ansible_ssh_common_args='-o StrictHostKeyChecking=no'")
