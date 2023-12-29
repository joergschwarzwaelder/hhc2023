# Objective 12: Na'an
**Difficultree: 🎄🎄**  
**Location: Film Noir Island: Chiaroscuro City**  
**Hints from Shifty McShuffles**

The aim of this objective is raise awareness of the special handling of "NaN" (non a number) in Python.

A card game is played against the cheating Shifty McShuffles.
Each player chooses five unique numbers between 0 and 9.
The players with the highest and lowest number get a point.

The issue with this game is, that it is also possible to submit "NaN" as chosen number. That way, choosing **0,1,8,9,NaN** does always win ("NaN" is explicitly allowed in the client side pre-checks).
When choosing 0,1,8,9, Shifty does always choose exactly the same numbers - effectively eliminating each other in the calculation.
For the final number, "NaN" is smaller than every remaining number Shifty chooses and at the same time also bigger than every number Shifty chooses. So NaN will win against any other number.

**Achievement: Na'an**

### Bonus

If the pre-checks in the browser are bypassed and a string is submitted instead of number, a Python error message reveals the [main part of the Python code](python-error.txt) running on the server side.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4OTg4NzY3NzAsLTQzODE5NDEzMywtMT
Y2ODc5MTcyMiwxMzcwODkzNzkwLDE5MzcwNjExNjgsLTIwMTAx
OTI2M119
-->