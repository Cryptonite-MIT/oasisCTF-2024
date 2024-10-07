# DESCRIPTION

The game has finally loaded! Yet, as you start to play, a sinking realization dawns: you’ve been led into a trap. The virus has ensnared you in a loop, wasting precious time. The game is rigged to stall your progress. To save OASIS, you must break free of this digital decoy and bypass the virus's stalling tactics.

# WRITEUP


- Overflow the input field when it asks name.

- Score is stored at name-buffer + 25, this can be checked via a decompiler.


working payload : `eeeeeeeeeeeeeeeeeeeeeeeeee`

>OASIS{D0DG3_4LL_TH3_R0CK5_0R_N07}
