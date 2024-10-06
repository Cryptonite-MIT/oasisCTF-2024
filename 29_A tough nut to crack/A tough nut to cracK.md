# DESCRIPTION
IOI won’t be fooled so easily. In response to your clever coup, they dispatch their most advanced guards, outfitted with tactical gear and cutting-edge weaponry. But you’ve gained a powerful advantage—the mechanoids at your command. Now, it’s time to flip the battlefield dynamic and make the guards fight against their own machines. Use the mechanoids’ systems to reverse the hostility and dismantle the IOI’s last defense.


# WRITEUP 

- Given is a python bytecode file and `flag.enc`.
- We decompile the bytecode first using any online decompiler.
- The code encrypts it using a PRNG with seed(0) and an array of XORs.
- Reverse the code to get the flag.

>OASIS{py_X0R_08fu5c4710N5}
