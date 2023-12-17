# Objective 16: Elf Hunt
**Location: Pixel Island: Raincaster Cliffs**  
**Hints provided by Piney Sappington**

The objective is a browser game where the player has to target elves which move very fast over the screen.

If the browser developer console it was easy to spot, that the game uses a cookie `ElfHunt_JWT` which contains a JWT token.

With the help of https://token.dev is was possible to decode this JWT and it was found as an unsigned JWT with the content:
```
{
  alg: "none",
  typ: "JWT"
}.
{
  speed: -500
}.
```
As this is not signed, it can easily be modified to `speed: -40` using this tool.
Assigning the new JWT to the cookie, the game is much easier to play.


**Achievement: Elf Hunt**
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk2ODAxMzE2MSwtMjAxMDE5MjYzXX0=
-->