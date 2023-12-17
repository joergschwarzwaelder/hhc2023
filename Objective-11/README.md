# Objective 11: Game Cartridges: Vol 3
**Location: Steampunk Island: Rosty Quay**  

The Game Cartrige 3 can be found at the above location at 23/31. As Rosty Quay is a maze in this area, it is advised to zoom out in the browser to find the right way.
The game can be started anytime from the "Items" section in the game.

The game was solved using the VisualBoyAdvance simulator.

In the game there are effectively two challenges:

###Obtain 999 coins
There are three different kind of coins in the game with values 1, 10, and 100. The game has overflow issues so that is it impossible to make 999 with regular gaming.
In order to analyze, how/were the amount of coins is stored, the game status was backed up using the simulator prior and after obtaining coins.
Using that it was found that the single digits of the coins amount are stored in these locations:

- 100s: `0x44d8`
- 10s: `0x44a4`
- 1s: `0x4470`

Setting these three bytes to 

###Pass the gap 

**Achievement: Game Cartridges: Vol 3**
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQzNzk5NDU4OSwtMjAxMDE5MjYzXX0=
-->