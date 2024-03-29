# Objective 15: Hashcat
**Difficultree: 🎄🎄**  
**Location: Island of Misfit Toys: Scaredy Kite Heights**

The aim of this objective is to get familiar with the password cracking tool "hashcat".

Provided is the [hash](hash.txt)

`$krb5asrep$23$alabaster_snowball@XMAS.LOCAL:22865a2bceeaa73227ea4021879eda02$8f07417379e610e2dcb0621462fec3675bb5a850aba31837d541e50c622dc5faee60e48e019256e466d29b4d8c43cbf5bf7264b12c21737499cfcb73d95a903005a6ab6d9689ddd2772b908fc0d0aef43bb34db66af1dddb55b64937d3c7d7e93a91a7f303fef96e17d7f5479bae25c0183e74822ac652e92a56d0251bb5d975c2f2b63f4458526824f2c3dc1f1fcbacb2f6e52022ba6e6b401660b43b5070409cac0cc6223a2bf1b4b415574d7132f2607e12075f7cd2f8674c33e40d8ed55628f1c3eb08dbb8845b0f3bae708784c805b9a3f4b78ddf6830ad0e9eafb07980d7f2e270d8dd1966`

and along with that a [password list](password_list.txt) containing 144 password candidates.

A first analysis shows that this is a type 18200 hash ("Kerberos 5, etype 23, AS-REP").

Hashcat is able to crack this:
```
elf@de3aa9d4d0ac:~$ hashcat -w 1 -u 1 --kernel-accel 1 --kernel-loops 1 -m 18200 --force hash.txt password_list.txt 
[...]
$krb5asrep$23$alabaster_snowball@XMAS.LOCAL:22865a2bceeaa73227ea4021879eda02$8f07417379e610e2dcb0621462fec3675bb5a850aba31837d541e50c622dc5faee60e48e019256e466d29b4d8c43cbf5bf7264b12c21737499cfcb73d95a903005a6ab6d9689ddd2772b908fc0d0aef43bb34db66af1dddb55b64937d3c7d7e93a91a7f303fef96e17d7f5479bae25c0183e74822ac652e92a56d0251bb5d975c2f2b63f4458526824f2c3dc1f1fcbacb2f6e52022ba6e6b401660b43b5070409cac0cc6223a2bf1b4b415574d7132f2607e12075f7cd2f8674c33e40d8ed55628f1c3eb08dbb8845b0f3bae708784c805b9a3f4b78ddf6830ad0e9eafb07980d7f2e270d8dd1966:IluvC4ndyC4nes!
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Type........: Kerberos 5 AS-REP etype 23
Hash.Target......: $krb5asrep$23$alabaster_snowball@XMAS.LOCAL:22865a2...dd1966
Time.Started.....: Wed Dec  6 17:09:25 2023 (0 secs)
Time.Estimated...: Wed Dec  6 17:09:25 2023 (0 secs)
Guess.Base.......: File (password_list.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:      806 H/s (0.84ms) @ Accel:1 Loops:1 Thr:64 Vec:16
Recovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 144/144 (100.00%)
Rejected.........: 0/144 (0.00%)
Restore.Point....: 0/144 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-0
Candidates.#1....: 1LuvCandyC4n3s!2022 -> iLuvC4ndyC4n3s!23!

Started: Wed Dec  6 17:09:22 2023
Stopped: Wed Dec  6 17:09:27 2023
```

Answer: **IluvC4ndyC4nes!**

**Achievement: Hashcat**
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk0MTYxOTc5OSwtMTQxMzY5MjQxLC0yMD
k5NzQxMTQ2LC03ODA5OTA5MjUsMTU3OTEwNTk2MCwtMjAxMDE5
MjYzXX0=
-->