__author__ = 'grantpowell'

try:
    import reportlab
except:
    import pip
    pip.main(['install', 'reportlab'])
    import reportlab

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

with open('roster.txt') as file:
    names = [name.strip().split(',') for name in file.readlines()]

width, height = letter
c = canvas.Canvas("namecards.pdf", pagesize=letter)

namecnt = 0
while namecnt < len(names):
    for y in [0, 1, 2, 3]:
        if namecnt == len(names): continue
        for x in [0, 1]:
            if namecnt == len(names): continue
            xoffset = inch * 3.8 * x
            yoffset = inch * 2.5 * y
            c.rect(.5 * inch + xoffset, .5 * inch + yoffset, inch * 3.5, inch * 2.25)
            c.drawImage('transparent.jpg', .95 * inch + xoffset, .65 * inch + yoffset)
            c.setFont("Times-Roman", 20)
            c.drawCentredString((.5 * 3.5 + .5) * inch + xoffset, .6 * inch + yoffset, 'ALPHA KAPPA PSI')
            if len(names[namecnt][0]) >= 12 or len(names[namecnt][-1]) >= 12:
                c.setFont("Helvetica-Bold", 30)
            elif len(names[namecnt][0]) >= 8 or len(names[namecnt][-1]) >= 8:
                c.setFont("Helvetica-Bold", 35)
            else:
                c.setFont("Helvetica-Bold", 40)
            c.drawCentredString((.5 * 3.5 + .5) * inch + xoffset, 2 * inch + yoffset, names[namecnt][0])
            c.drawCentredString((.5 * 3.5 + .5) * inch + xoffset, 1.4 * inch + yoffset, names[namecnt][1])
            if len(names[namecnt]) > 2:
                c.setFont("Times-Italic", 16)
                c.drawCentredString((.5 * 3.5 + .5) * inch + xoffset, 1 * inch + yoffset, ' '.join(names[namecnt][2:]))
            namecnt += 1
    c.showPage()

c.save()


