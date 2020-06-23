# Booklet Maker
# Converts 8 pages into a single page for a MyPocketMod-style booklet.
# Usage: bookletmaker.py filename.pdf

# 1. Rotate pages 1 - 8 properly (1, 6-8 upside down)
# 2. Move pages 2 - 4 to the end. 
# 3. Set up new page (width and height swap places)
# 4. Shrink and place pages (first four in top row, last four in bottom row) 


import sys
import os

from pdfrw import PdfReader, PdfWriter, PageMerge

def place8(srcpages):
    scale = 1
    srcpages = PageMerge() + srcpages
    x_increment, y_increment = (scale * i for i in srcpages.xobj_box[2:])
    for i, page in enumerate(srcpages):
        print(page.w)
        print(page.h)
        page.scale(scale, scale)
        page.x = (i % 4)*x_increment 
        page.y = 0 if i < 4 else y_increment
    return srcpages.render()

torotate = [0, 5, 6, 7]

inpfn, = sys.argv[1:]
outfn = 'booklet.' + os.path.basename(inpfn)

trailer = PdfReader(inpfn)
pages = trailer.pages

for pageno in torotate:
    pages[pageno].Rotate = (int(pages[pageno].inheritable.Rotate or 0) + 180) % 360

writer = PdfWriter(outfn)

orgedpages = [ pages[0], pages[7], pages[6], pages[5], pages[1], pages[2], pages[3], pages[4]]
writer.addpage(place8(orgedpages))



#pages = PdfReader(inpfn).pages

#for index in range(0, len(pages), 4):
#    writer.addpage(get4(pages[index:index + 4]))

writer.write()
