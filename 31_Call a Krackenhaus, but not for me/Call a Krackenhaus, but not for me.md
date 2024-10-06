# DESCRIPTION
You move forward to a fortified area deep inside the OASIS—a place known only as the "Black Wall", you realize as you reach there. It is said that the Black Wall protects IOI's most sensitive data, including a mysterious entity that could end their control of OASIS. However, getting into the fortress won't be simple.  However, now that you have your mechanoid alongside you, you decide to cause a distraction using the robots while you sneak into the Black Wall.
Try and find a way to do so without getting caught.

# WRITEUP

- On decompiling the binary, we see 6 functions that help us in constructing the flag.
- The `main` function gives us the length of the flag which is 26
- The `krak` function checks if the flag starts with `OASIS{` and ends with `}`
- The `jack` function checks the for `_`'s in specified indexes of the flag
- The `wack` and `rack` functions check for certain characters at specified indexes of the flag
- All the functions help us in constructing the flag but we still don't know the character at index 13. The function `check_md5` acts as an integrity check. It compares the md5 hash of the user input with the md5 hash of the flag. We need to bruteforce the character at that index and generate hashes until we find a match.

>OASIS{cr4ck_me_1f_y0u_c4n}
