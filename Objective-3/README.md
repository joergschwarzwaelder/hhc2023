# Objective 3: Linux 101
**Location: Christmas Island: Santa's Surf Shack**  

Is this terminal the player gets to know some Linux basics.

```
elf@dd0741506806:~$ ls
HELP  troll_19315479765589239  workshop
elf@dd0741506806:~$ cat troll_19315479765589239
troll_24187022596776786
elf@dd0741506806:~$ rm troll_19315479765589239  
elf@dd0741506806:~$ pwd
/home/elf
elf@dd0741506806:~$ ls -a
.  ..  .bash_history  .bash_logout  .bashrc  .profile  HELP  troll_19315479765589239  workshop
elf@dd0741506806:~$ history | grep troll
    1  echo troll_9394554126440791
    [...]
elf@dd0741506806:~$ env | grep -i troll
SESSNAME=Troll Wrangler
z_TROLL=troll_20249649541603754
OLDPWD=/opt/troll_den
elf@dd0741506806:~$ cd workshop/
elf@dd0741506806:~/workshop$ grep -i troll toolbox_*
toolbox_191.txt:tRoLl.4056180441832623
elf@dd0741506806:~/workshop$ chmod a+x present_engine
elf@dd0741506806:~/workshop$ ./present_engine
troll.898906189498077
elf@dd0741506806:~/workshop$ cd electrical/
elf@dd0741506806:~/workshop/electrical$ mv blown_fuse0 fuse0
elf@dd0741506806:~/workshop/electrical$ ln -s fuse0 fuse1
elf@dd0741506806:~/workshop/electrical$ cp fuse1 fuse2
elf@dd0741506806:~/workshop/electrical$ echo "TROLL_REPELLENT" >> fuse2
elf@dd0741506806:~/workshop/electrical$ find /opt/troll_den/ -iname '*troll*'  
[...]/opt/troll_den/
/opt/troll_den/plugins/embeddedjsp/src/main/java/org/apache/struts2/jasper/compiler/ParserController.java
/opt/troll_den/apps/showcase/src/main/resources/tRoLl.6253159819943018
/opt/troll_den/apps/rest-showcase/src/main/java/org/demo/rest/example/IndexController.java
/opt/troll_den/apps/rest-showcase/src/main/java/org/demo/rest/example/OrdersController.java
/opt/troll_den$ find . -iname '*troll*'  
./apps/showcase/src/main/resources/template/ajaxErrorContainers/tr0LL_9528909612014411
elf@dd0741506806:/opt/troll_den$ find . -size +108k -size -110k
./plugins/portlet-mocks/src/test/java/org/apache/t_r_o_l_l_2579728047101724
elf@dd0741506806:/opt/troll_den$ ps -aef
elf@dd0741506806:/opt/troll_den$ netstat -an | grep LISTEN
elf@dd0741506806:/opt/troll_den$ curl http://localhost:54321
elf@dd0741506806:/opt/troll_den$ pkill 14516_troll
```

**Achievement: Linux 101**

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM0NDI3NTc0NSwtMjEzNzUxMjQyMywxND
k2NjczMzM0LC0yMDEwMTkyNjNdfQ==
-->