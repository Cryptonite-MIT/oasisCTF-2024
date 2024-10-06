# DESCRIPTION

As the terminal roars back to life, a single message blinks on the screen: "START GAME." You’re no longer just a player—you’re in the endgame now. The keyboard before you looks deceptively simple, but nothing you try gets past the loading screen. Something is clearly wrong. Can you uncover the hidden flaw and push beyond this stagnant start?

# WRITEUP

First need to set your UserAgent to OASISPlayer and send a POST request on /game endpoint.

The response is: errorMessage	"Can you give me the name of the Student Project organizing this event as a url parameter 'name'?"

So send a POST request with query parameter name=Cryptonite to /game like so: /game?name=Cryptonite. (Uppercase or lowercase dosen't matter). 

The response is : errorMessage	"Do you know you can chain query parameters? Add a 'rank' parameter and give the current CTFTime rank of the project on /givemetheFlag".

So send a POST request with query parameter name=Cryptonite&rank=4 to /givemetheFlag like so: /givemetheFlag?name=Cryptonite&rank=4.

>OASIS{G37_d035_n07_4lw4y5_G37_th1ng5}
