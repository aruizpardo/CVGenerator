from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, white, pink, lightblue

import functions
import os
import sys

# Get cv data
import data

# Global variables
APP_ROOT = os.path.abspath(os.path.dirname(sys.argv[0]))


def main():
    functions.create_rounded_image(os.path.join(APP_ROOT, "img", "cara.webp"))

    w, h = A4
    c = canvas.Canvas("cv.pdf", pagesize=A4)

    # c.setFillColor(lightblue)
    # c.rect(0, 0, w-50, h-50, stroke=False, fill=True)

    # Header
    c.drawImage(os.path.join(APP_ROOT, "img", "banner.webp"), 0, h-120, w, 100)
    c.drawImage(os.path.join(APP_ROOT, "img", "cara.png"), 100, h-95, 75, 75, mask="auto")



    c.setFillColor(black)
    c.drawString(80, h - 80, "¡Hola, mundo!")
    c.showPage()
    c.save()


if __name__ == '__main__':
    main()
    os.startfile(os.path.join(APP_ROOT, "cv.pdf"))
