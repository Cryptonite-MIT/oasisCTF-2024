# DESCRIPTION

Amid the chaos, you spot something crucial: a control unit embedded in the mechanoids’ chassis. With a well-timed leap, you manage to access one of the units. A complex matrix of data awaits you inside, but if you can decipher it, you could seize control of the entire robotic army. Can you crack the code and turn the tables on IOI?

# WRITEUP

- challenge is cenetered around the idea that `-x % p = p - x`
- diagonal elements of the provided matrix are of the form `flag characters * -1 % p`
- p is a prime different for each row.
- extract the p's using the idea in point 1
- then just subtract each diagonal element from p to get flag

>OASIS{Bro_Really_Modded_It_Negative}
