from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from datetime import datetime
today = datetime.now()

my_canvas = canvas.Canvas("Raport "+str(today.strftime("%dd_%mm_%Yr__%HH_%MM_%SS"))+".pdf", pagesize=letter)
my_canvas.setLineWidth(.3)
my_canvas.setFont("Times-Roman", 16)
my_canvas.drawString(30, 750, 'Dział OGH')
my_canvas.drawString(400, 750, 'Gdańsk, dnia ' + str(today.date().strftime("%d/%m/%Y")))
my_canvas.drawString(275, 725, 'AMOUNT OWED:')
my_canvas.drawString(500, 725, "$1,000.00")
my_canvas.line(378, 723, 580, 723)
my_canvas.drawString(30, 703, 'RECEIVED BY:')
my_canvas.line(120, 700, 580, 700)
my_canvas.drawString(120, 703, "JOHN DOE")
my_canvas.save()
