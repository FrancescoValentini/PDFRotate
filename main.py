import argparse
import fitz  # PyMuPDF

def rotate(inputFile, outputFile, angle=90):
    """
    Rotates all pages of a PDF file by a specified angle and saves the rotated version to a new file.

    :param inputFile: Path to the input PDF file that needs to be rotated.
    :param outputFile: Path where the rotated PDF will be saved.
    :param angle: The angle by which to rotate the PDF pages. Must be 90, 180, or 270 degrees.
    :return: None
    """
    doc = fitz.open(inputFile)

    for page in doc:
        page.set_rotation(angle)

    doc.save(outputFile)
    doc.close()


def compress(inputFile, outputFile):
    """
    Compresses a PDF file

    :param inputFile: Path to the input PDF file that needs to be compressed.
    :param outputFile: Path where the compressed PDF will be saved.
    :return: None
    """
    doc = fitz.open(inputFile)

    # Save compressed file
    doc.save(outputFile, garbage=4, deflate=True, clean=True)
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