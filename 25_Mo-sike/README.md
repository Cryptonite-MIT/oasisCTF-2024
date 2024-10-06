# DESCRIPTION 
You’ve uncovered the truth: it was a Trojan all along. Disguised as an integral part of the OASIS, the virus has been feeding vital information to IOI, undermining the system from within. Now, with its cover blown, you must track the data trails left behind by the Trojan before it can do any more damage. These data trails are in the form of a file containing a sequence of color names, each representing a piece of a larger mosaic. This mosaic forms a square grid, and when the squares are correctly arranged, they reveal a hidden image of a video game character. Your task is to decipher the relationship between the color list and the grid, reconstructing the image by placing each colored square in its correct position. The challenge lies in ensuring that the final arrangement reveals the intended character, with no visual discrepancies.. Follow the breadcrumbs and uncover its next move.


Flag format: OASIS{nameofcharacter_nameofgame} in lowercase
# WRITEUP

You are given a text file containing a sequence of color names, each representing a piece of a larger mosaic. This mosaic forms a square grid, and when the squares are correctly arranged, they reveal a hidden image of a video game character. Your task is to decipher the relationship between the color list and the grid, reconstructing the image by placing each colored square in its correct position. The challenge lies in ensuring that the final arrangement reveals the intended character, with no visual discrepancies. Flag format: OASIS{nameofcharacter_nameofgame} in lowercase

- Arrange the pixels in a 56x56 square.
- The resulting image can be reverse image searched to be found as `missingno`.

>OASIS{missingno_pokemon}
