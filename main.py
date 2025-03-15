import argparse
import fitz  # PyMuPDF


def rotate(inputFile, outputFile, angle=90, compress=False):
    """
    Rotates all pages of a PDF file by a specified angle and optionally compresses the resulting PDF.

    :param inputFile: Path to the input PDF file that needs to be rotated.
    :type inputFile: str
    :param outputFile: Path where the rotated (and optionally compressed) PDF will be saved.
    :type outputFile: str
    :param angle: The angle by which to rotate the PDF pages. Must be 90, 180, or 270 degrees.
    :type angle: int
    :param compress: If True, the rotated PDF will be compressed before saving. Default is False.
    :type compress: bool
    :return: None
    """
    doc = fitz.open(inputFile)

    for page in doc:
        page.set_rotation(angle)

    if compress:
        doc.save(outputFile, garbage=4, deflate=True, clean=True)
    else:
        doc.save(outputFile)
    doc.close()



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputFile")
    parser.add_argument("outputFile")
    parser.add_argument("-d", "--degrees", action="store_const")
    parser.add_argument("-c", "--compress", action="store_true")
    args = parser.parse_args()


if __name__ == "__main__":
    main()