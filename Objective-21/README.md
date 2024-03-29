# Objective 21: Camera Access
**Difficultree: 🎄🎄🎄**  
**Location: Space Island: Zenith SGS**

The entrance to Zenith SGS is invisible and is located on "Space Island: Cape Cosmic Inside Fence" at 54/24.
The objective is to gain access to Jack's camera and find the third item on Jack's TODO list.

To clear this objective, the [Docker image](https://www.holidayhackchallenge.com/2023/client_container.zip) provided by the vending machine "NanoSat-o-Matic" has to be used.

In the next step, GateXOR has to be used to establish a WireGuard VPN connection - the client side configuration is provided and has to be added to `/etc/wireguard/wg0.conf` in the Docker container. Afterwards the Wireguard connection can be brought up with `wg-quick up wg0`.
Sample configuration:
```
[Interface]
Address = 10.1.1.1/24
PrivateKey = DQmUt0eU3kyXPrakUS74gUpG59ZZp0m8IBGrea2xF/k=
ListenPort = 51820

[Peer]
PublicKey = 2bEA/MsiBlvdMYAgNNZT0zPqxnTEtDX8tYi22rbCUyQ=
AllowedIPs = 10.1.1.2/32
```

In the container is a "Consumer Test Tool" to interact with the server side.
The directory service URI "maltcp://10.1.1.1:1024/nanosat-mo-supervisor-Directory" is used throughout the objective.
With the button "Fetch Information" we can retrieve details about all registered providers. Initially only "nanosat-mo-supervisor" is available.

We can connect to it by selecting this provider followed by pressing the button "Connect to Selected Provider".
This opens a new tab "nanosat-mo-supervisor" on the subtab "Apps Launcher Service".
As our objective is to take a picture using the camera, the "camera" app is selected followed by "runApp".

Next we navigate back to "Communications Settings" and refresh the data with "Fetch Information". Now the "App: camera" should be visible and we can connect to it (select provider, click "Connect to Selected Provider").

A new tab "App: camera" appears. In this tab we can navigate to subtab "Action service", where an action service definition for "Base64SnapImage" can be found.

When this is selected and "submitAction" is pressed, the camera takes a picture and this image is transferred base64 encoded to the client SW.

This transfer can be captured using the installed "Wireshark" on the wg0 interface. As the traffic is unencrypted, it is easy to spot and extract the base64 image data from the TCP stream.
Finally, this base64 data just has to be decoded.
![Camera image](image.jpg)
As we need the third item on the TODO list, **CONQUER HOLIDAY SEASON!** is the solution.

**Achievement: Camera Access**
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQyNjg0MTYzNywtMjA5MzY4NTA2MiwzNT
Y4NTk1OTQsMTMyMzU2NjYzMiwtNzQ4MjgzNTk5LC03NDgyODM1
OTksNzM2MDg0MDg1LDIwNDgxMDg5MTIsLTIwMTAxOTI2M119
-->