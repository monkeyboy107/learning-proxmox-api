import yaml
from proxmox import ProxmoxAPI

file = 'secrets.yaml'

with open(file) as stream:
  secrets = yaml.safe_load(stream)

print(secrets)
