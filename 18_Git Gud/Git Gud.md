# DESCRIPTION

You decrypt the code and follow all the commands. However, as you think you have breached the firewall, the screen goes black and random numbers start glitching on the screen. You realize that the OASIS realizes that they have left admin privileges and are messing with the computer in order for you not to be able to perform the final push.

# WRITEUP

- Given is a 7zip archive.
- Extracting it gives us a git repo with a research paper on RPO.
- The flag is spelled out in the git commit messages shown through `git log`.

Solve shell command: `git log | grep '    ' | tac | tr -d ' ' | tr -d '\n'`

>OASIS{g3t_gu663r_4t_g!t!!}
