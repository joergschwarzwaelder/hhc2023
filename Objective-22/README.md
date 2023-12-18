# Objective 22: Missile Diversion
**Location: Space Island: Zenith SGS**

For this objective the same Docker image and Wireguard VPN connection as in [Objective 21](https://github.com/joergschwarzwaelder/hhc2023/tree/main/Objective-21)

In the first step, the app "missile-targeting-system" is started just like the "camera" app in objective 21.

The "Action Service" of this app has the predefined action "Debug", which is vulnerable to SQL injections by supplying additional data like `; show grants` as "AttributeValue".
The output of these injections can be found on the "nanosat-mo-supervisor" tab, subtab "Apps Launcher service":




**Achievement: Ipsum**
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NTg5ODMzMDksLTQ2NjI0MjMyMSwtMj
AxMDE5MjYzXX0=
-->