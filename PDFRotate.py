import argparse
import fitz  # PyMuPDF
import os
import time
from datetime import timedelta

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


def processFolder(inputFolder, outputFolder, angle=90, compress=False):
    """
    Processes all PDF files in a folder, rotating them by a specified angle and optionally compressing them.

    :param inputFolder: Path to the folder containing the PDF files to be rotated.
    :type inputFolder: str
    :param outputFolder: Path to the folder where the rotated (and optionally compressed) PDFs will be saved.
    :type outputFolder: str
    :param angle: The angle by which to rotate the PDF pages. Must be 90, 180, or 270 degrees.
    :type angle: int
    :param compress: If True, the rotated PDFs will be compressed before saving. Default is False.
    :type compress: bool
    :return: None
    """
    # Ensure the output folder exists
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

    # Iterate over all files in the input folder
    for filename in os.listdir(inputFolder):
        if filename.endswith(".pdf"):
            inputFilePath = os.path.join(inputFolder, filename)
            print(f"[INFO] Processing: {inputFilePath}")
            outputFilePath = os.path.join(outputFolder, filename)
            rotate(inputFilePath, outputFilePath, angle, compress)

def isFolder(path):
    return os.path.isdir(path)


def main():
    start_time = time.time()

    parser = argparse.ArgumentParser(
        description="Rotate and optionally compress a PDF file or all PDFs in a folder.\n\nAuthor: Francesco Valentini",
        epilog="Examples:\n"
               "  1. Rotate a single PDF file by 180 degrees:\n"
               "     python PDFRotate.py input.pdf output.pdf -d 180\n"
               "  2. Rotate and compress all PDFs in a folder by 180 degrees:\n"
               "     python PDFRotate.py input_folder output_folder -d 180 -c",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "inputPath",
        help="Path to the input PDF file or folder containing PDF files."
    )
    parser.add_argument(
        "outputPath",
        help="Path to save the rotated (and optionally compressed) PDF file or folder."
    )
    parser.add_argument(
        "-d", "--degrees",
        type=int,
        default=90,
        choices=[90, 180, 270],
        help="Rotation angle in degrees (90, 180, or 270). Default is 90."
    )
    parser.add_argument(
        "-c", "--compress",
        action="store_true",
        help="Compress the PDF after rotation."
    )
    args = parser.parse_args()

    if not (isFolder(args.inputPath) or isFolder(args.outputPath)):
        print(f"\n[INFO] Processing: {args.inputPath}...")
        rotate(args.inputPath, args.outputPath, args.degrees, args.compress)
    else:
        processFolder(args.inputPath, args.outputPath, args.degrees, args.compress)

    elapsed_time = time.time() - start_time
    elapsed_time_formatted = str(timedelta(seconds=int(elapsed_time)))
    print(f"\n[INFO] Operation completed in: {elapsed_time_formatted}.")


if __name__ == "__main__":
    main()