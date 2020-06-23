# bookletmaker
Attempts to convert first 8 pages of a .pdf into a booklet. Simple script based on pdfrw: https://github.com/pmaupin/pdfrw

To Use: Syntax I use in Linux CLI: python3 bookletmaker.py filename.pdf will output to booklet.filename.pdf in the same directory. Currently, you must manually adjust the scale variable in the script to make it work properly. You may also need to adjust the x and y scales depending on your input document (and also introduce these variables yourself). For 8.5 x 11 size paper I write 2.75" by 4.25" documents in LaTeX and use scale = 1. I suggest printing "actual size" as "fit" will squish the document so that it will not fit correctly once you fold it. See photographs for an idea of how to fold and cut the paper. 

Description: A rather rudimentary and brief script most could write themselves, yes, but I use it frequently. Intended to imitate a similar .pdf converter program (hard to find the original online nowadays, there is an updated website with a paid version) which does not work well in Windows 10. Script is much less general and capable at the moment. An example is included (rules for two-handed Pinochle). Photographs of booklet and assembly included. Scissors recommended to cut out the central line. 


