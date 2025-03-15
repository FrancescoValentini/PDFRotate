from PyPDF2 import PdfReader, PdfWriter

def rotate(inputFile, outputFile, angle=90):
    """
    Rotates a PDF file by a specified angle and saves the rotated version to a new file.

    :param inputFile: Path to the input PDF file that needs to be rotated.
    :param outputFile: Path where the rotated PDF will be saved.
    :param angle: The angle by which to rotate the PDF pages. Default is 90 degrees.
    :return: None
    """
    reader = PdfReader(inputFile)
    writer = PdfWriter()

    for page_index in range(len(reader.pages)):
        page = reader.pages[page_index]
        writer.add_page(page.rotate(angle))

    with open(outputFile, "wb") as fp:
        writer.write(fp)
