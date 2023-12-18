# Objective 21: Camera Access
**Location: Space Island: Zenith SGS**  

To clear this objective, the provided [Docker image](https://www.holidayhackchallenge.com/2023/client_container.zip) has to be used.
In the next step, GateXOR has to be used to establish a WireGuard VPN connection - the client side configuration is provided and has to be added to `/etc/wireguard/wg0.conf` in the Docker container. Afterwards the Wireguard connection can be brought up with `wp-quick up wg0`.

In the container is a "Consumer Test Tool" to interact with the server side.
The directory service URI "maltcp://10.1.1.1:1024/nanosat-mo-supervisor-Directory" is used throughout the objective.
With the button "Fetch Information" we can retrieve details about al


**Achievement: Ipsum**
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY3MjM2NDgxOCwyMDQ4MTA4OTEyLC0yMD
EwMTkyNjNdfQ==
-->