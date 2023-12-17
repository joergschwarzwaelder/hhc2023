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

With this SSH certificate (and the private key) we are able to login to the server as "monitor":




Lorem

**Achievement: Ipsum**
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk3Njk0MjA3MiwtMjAxMDE5MjYzXX0=
-->