# Objective 18: The Captain's Comms
**Location: Steampunk Island: Brass Bouy Port**

**Hints provided by Chimney Scissorsticks**

This objective is a deep dive into JWT tokens.

For the whole task the tool https://token.dev/ was used.

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

In addition, a "CaptainsCookie" is set without a signature:
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

From the same To-Do list, we know that the public key of the signatures is in [https://captainscomms.com/jwtDefault/capsPubKey.key](https://captainscomms.com/jwtDefault/capsPubKey.key), accessible with the role "radioMonitor".
In addition, using the same token, we can access [https://captainscomms.com/jwtDefault/rDecoder.tok](https://captainscomms.com/jwtDefault/rDecoder.tok). This token unlocks the role "radioDecoder" which is required to use the decoder function in the SDR receiver, providing these three pieces of information:

**CW:**

![CW Decoder](https://github.com/joergschwarzwaelder/hhc2023/blob/main/Objective-18/CWDecoder.png)

`... CQ CQ CQ DE KH644 - -- SILLY CAPTAIN! WE FOUND HIS FANCY RADIO PRIVATE KEY IN A FOLDER CALLED TH3CAPSPR1V4T3F0LD3R ...`
With this information we are able to access the private signature key in [https://captainscomms.com/jwtDefault/keys/TH3CAPSPR1V4T3F0LD3R/capsPrivKey.key](https://captainscomms.com/jwtDefault/keys/TH3CAPSPR1V4T3F0LD3R/capsPrivKey.key) using the role "radioDecoder".

**NUM:**

![NUM Decoder](https://github.com/joergschwarzwaelder/hhc2023/blob/main/Objective-18/NUMDecoder.png)

`{music} {music} {music} 88323 88323 88323 {gong} {gong} {gong} {gong} {gong} {gong} 12249 12249 16009 16009 12249 12249 16009 16009 {gong} {gong} {gong} {gong} {gong} {gong} {music} {music} {music}`
This gives a hint to the go-date `1224` and the go-time 1600.
As we have to target four hours earlier, we have to choose `1200`.

**RadioFax:**

![RadioFaxDecoder](https://github.com/joergschwarzwaelder/hhc2023/blob/main/Objective-18/RadioFaxDecoder.png)

Freq: `10426` Hz

With the above private key we can create a signature for the above JWT token for the "GeeseIslandsSuperChiefCommunicationsOfficer" role and have with this role access to the transmitter station.

Setting these three values in the transmitter station finalizes the objective:

![Completion](https://github.com/joergschwarzwaelder/hhc2023/blob/main/Objective-18/completion.png)

**Achievement: The Captain's Comms**
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjQyNTY5MzY5LC0yMDEwMTkyNjNdfQ==
-->