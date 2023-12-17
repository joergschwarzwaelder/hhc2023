# Objective 10: Game Cartridges: Vol 2
**Location: Pixel Island: Driftbit Grotto**  

The Game Cartrige 2 can be found at the above location at 3/20.
It can be started anytime from the "Items" section in the game.
There are two different versions of this game. If the game is started, it is randomly chosen which one is started.
The only difference between both is, that a specific screen in one game is open on the top and you the player is pushed down a few steps when trying to pass. The other version is just the opposite: The screen is open on the bottom and the player is pushed up when trying to pass.

To solve this challenge, both versions of the game were byte compared in order to find, where the "push down"/"push up" definition is done. It turned out, that on byte position `0x17c80` game0 has a `0x02` and game1 a `0x01`.
After changing this byte in the game0 binary to `0x01` , the character is not pushed back down anymore and instead push up effectively passing the "magical b




**Achievement: Game Cartridges: Vol 2**
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTkwNDc1MDU3MSw5NTMzMjUyNzQsLTIwMT
AxOTI2M119
-->