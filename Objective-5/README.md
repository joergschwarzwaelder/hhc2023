# Objective 5: Azure 101
**Difficultree: 🎄🎄**  
**Location: Christmas Island: Rudolph's Rest**

In this objective the player gets hand on experience with the Azure CLI.

```
elf@16e0a0834f6e:~$ az help | less
[...]
elf@16e0a0834f6e:~$ az account show | less
{
  "environmentName": "AzureCloud",
  "id": "2b0942f3-9bca-484b-a508-abdae2db5e64",
  "isDefault": true,
  "name": "northpole-sub",
  "state": "Enabled", "tenantId": "90a38eda-  4006-4dd5-924c-6ca55cacc14d",
  "user": {
    "name": "northpole@northpole.invalid",
    "type": "user"
  }
}
elf@16e0a0834f6e:~$ az group list
[
  {
    "id": "/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/northpole-rg1",
    "location": "eastus",
    "managedBy": null, "name": "northpole-rg1",
    "properties": {
      "provisioningState": "Succeeded"
    },
    "tags": {}
  },
  {
    "id": "/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/northpole-rg2",
    "location": "westus",
    "managedBy": null,
    "name": "northpole-rg2",
    "properties": {
      "provisioningState": "Succeeded"
    },
    "tags": {}
  }
]
elf@16e0a0834f6e:~$ az functionapp list --resource-group northpole-rg1
[...]
elf@16e0a0834f6e:~$ az vm list --resource-group northpole-rg2
[...]
elf@16e0a0834f6e:~$ az vm run-command invoke --resource-group northpole-rg2 -n NP-VM1 --command-id RunShellScript --scripts "ls"
{
  "value": [
    {
      "code": "ComponentStatus/StdOut/succeeded",
      "displayStatus": "Provisioning succeeded",
      "level": "Info",
      "message": "bin\netc\nhome\njinglebells\nlib\nlib64\nusr\n",
      "time": 1702808672
    },
    {
      "code": "ComponentStatus/StdErr/succeeded",
      "displayStatus": "Provisioning succeeded",
      "level": "Info",
      "message": "",
      "time": 1702808672
    }
  ]
}
```

**Achievement: Azure 101**
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk1MDg2MjYxLDE2Mzg0OTYwMDcsLTIwMT
AxOTI2M119
-->