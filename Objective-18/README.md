# Objective 18: The Captain's Comms
**Location: Steampunk Island: Brass Bouy Port**  
**Hints provided by Chimney Scissorsticks**

This objective is a deep dive into JWT tokens.

When the activity is started, a cookie "justWatchThisRole" is set containing this signed JWT:
```
{
  "iss": "HHC 2023 Captain's Comms",
  "iat": 1699485795.3403327,
  "exp": 1809937395.3403327,
  "aud": "Holiday Hack 2023",
  "role": "radioUser"
}
```

In addition, a "CaptainsCokie" is set without a signature:
```
{
  "iss": "HHC 2023 Captain's Comms",
  "iat": 1699485795.3403327,
  "exp": 1809937395.3403327,
  "aud": "Holiday Hack 2023",
  "role": "GeeseIslandsSuperChiefCommunicationsOfficer"
}
```

From the Captain's ChatNPT Initial To-Do list (on the desk) we know, that one token resides in [https://captainscomms.com/jwtDefault/rMonitor.tok](https://captainscomms.com/jwtDefault/rMonitor.tok), accessible using a JWT for role "radioUser" - which we already have.

This rMonitor.tok JWT is a JWT for the role "radioMonitor":
```
{
  "iss": "HHC 2023 Captain's Comms",
  "iat": 1699485795.3403327,
  "exp": 1809937395.3403327,
  "aud": "Holiday Hack 2023",
  "role": "radioMonitor"
}
```

From the same To-Do list, we know that the public key of the signatures is in [https://captainscomms.com/jwtDefault/capsPubKey.key](https://captainscomms.com/jwtDefault/capsPubKey.key) accessible


**Achievement: The Captain's Comms**
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ3Mzc3MDM3MywtMjAxMDE5MjYzXX0=
-->