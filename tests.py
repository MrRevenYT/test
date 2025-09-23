# import yaml
# with open('config.yaml', 'r', encoding='utf-8') as file:
#     config = yaml.safe_load(file)
#
# print(config["bot"]["token"])

import yaml
with open('config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.safe_load(file)

print(config["messages"]["ru"])