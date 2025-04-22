from fpdf import FPDF

def shiritificate(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times",style='B',size=50)
    pdf.cell(text="CS50 Shirtificate", center=True, h=60)
    pdf.image("./shirtificate.png", x=10 ,y=75 ,w=pdf.epw)
    pdf.set_text_color(255,255,255)
    pdf.set_font(size=25)
    pdf.cell(text=f"{name} took CS50", center=True, h=260)
    pdf.output("shirtificate.pdf")

def main():
    shiritificate(input("Name: "))

main()
