# DESCRIPTION

The game has finally loaded! Yet, as you start to play, a sinking realization dawns: you've been led into a trap. The virus has ensnared you in a loop, wasting precious time. The game is rigged to stall your progress. To save OASIS, you must break free of this digital decoy and bypass the virusâ€™s stalling tactics. Sometimes, you need to overflow the memory's expectations to find a way out.

The game is broken; you can't shoot. However, only if you get a score of 100 or more can you get the flag.

# WRITEUP


- Overflow the input field when it asks name.

- Score is stored at name-buffer + 25, this can be checked via IL2cpp dumping (not that it was expected of players, or required). 

- players were to perform EDA by trying different payloads and observe how score's affected, maybe even get an instant unexpected solve.

working payload : `eeeeeeeeeeeeeeeeeeeeeeeeee`

>OASIS{D0DG3_4LL_TH3_R0CK5_0R_N07}
