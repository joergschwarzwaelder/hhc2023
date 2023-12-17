# Objective 12: Na'an
**Location: Film Noir Island: Chiaroscuro City**  
**Hints from Shifty McShuffles**

The aim of this objective is raise awareness of the special handling of "NaN" (non a number) in Python.

A card game is played against the cheating Shifty McShuffles.
Each player chooses five unique numbers between 0 and 9.
The players with the highest and lowest number get a point.

The issue with this game is, that it is also possible to submit "NaN" as chosen number. That way, choosing **0,1,8,9,NaN** does always win.
If you choose 0,1,8,9, Shifty does always choose exactly the same number - effectively eliminating each other in the calculation.
For the final number, "NaN" is smaller than every remaining number Shifty chooses and in parallel also higher than every number Shifty chooses. NaN will win against any other number.

**Achievement: Na'an**

### Bonus

If the prechecks in the browser are bypassed and a string is submitted instead of number, a Python error message reveals the main part of the Python code.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgxNDA0MDI5NCwtMTY2ODc5MTcyMiwxMz
cwODkzNzkwLDE5MzcwNjExNjgsLTIwMTAxOTI2M119
-->