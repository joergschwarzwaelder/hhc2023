# Objective 7: Linux PrivEsc
**Location: Island of Misfit Toys: Ostrich Saloon**  

The objective is to perform a privilege escalation in a Linux terminal session.
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

**Achievement: Linux PrivEsc**
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgyNjE3ODY4NCwtMjAxMDE5MjYzXX0=
-->