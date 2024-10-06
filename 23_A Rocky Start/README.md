# DESCRIPTION

The game has finally loaded! Yet, as you start to play, a sinking realization dawns: you’ve been led into a trap. The virus has ensnared you in a loop, wasting precious time. The game is rigged to stall your progress. To save OASIS, you must break free of this digital decoy and bypass the virus's stalling tactics.

# WRITEUP
Description must include " the game is broken, you can't shoot. However only if you get a score of 100 or more can you get flag "

or something along those lines.

Overflow the input field when it asks name.

Score is stored at buf + 25, this can be checked via a decompiler.


working payload : eeeeeeeeeeeeeeeeeeeeeeeeee

>OASIS{D0DG3_4LL_TH3_R0CK5_0R_N07}
