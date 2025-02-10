from fpdf import FPDF

def main():
    # Prompt user for their name
    name = input("Name: ")

    # Create a new PDF, Portrait orientation, A4 size (210 x 297 mm)
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Add a title at the top, centered horizontally
    pdf.set_font("helvetica", "B", 24)
    pdf.cell(0, 15, "CS50 Shirtificate", align="C", ln=1)

    # Coordinates and dimensions for the shirt image
    # We choose a width that fits nicely on an A4 page; adjust as needed.
    img_width = 150  # in mm
    # Calculate x coordinate to center the image horizontally
    img_x = (210 - img_width) / 2
    img_y = 50  # y coordinate; chosen to leave space for the title

    # Place the shirt image (make sure "shirtificate.png" is in the same directory)
    pdf.image("shirtificate.png", x=img_x, y=img_y, w=img_width)

    # Overlay the user's name on top of the shirt image.
    # Set white text for the name.
    pdf.set_font("helvetica", "B", 32)
    pdf.set_text_color(255, 255, 255)
    # Set the position for the text.
    # (Here, we choose a y coordinate that appears on the shirt; adjust as needed.)
    pdf.set_xy(0, img_y + 60)
    pdf.cell(0, 10, name, align="C", ln=1)

    # Output the PDF to a file named "shirtificate.pdf"
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
