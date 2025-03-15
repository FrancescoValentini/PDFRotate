# PDFRotate

**PDFRotate** is a simple Python tool to rotate PDF files. It can be used to rotate a single PDF file or all PDFs within a folder. Additionally, it offers an option to compress the PDFs after rotation.

## Requirements

- Python 3.x
- Required Python libraries: `pymupdf`

## Installation

#### 1) Clone and change directory
```bash
git clone https://github.com/FrancescoValentini/PDFRotate && cd PDFRotate
```

#### 2) Install Requirements
```bash
pip install -r requirements.txt
```

#### 3) Execute
```bash
python PDFRotate.py -h
```

## Examples
- **Rotate a single PDF file by 180 degrees:** `python PDFRotate.py input.pdf output.pdf -d 180`
- **Rotate and compress all PDFs in a folder by 180 degrees:** `python PDFRotate.py input_folder output_folder -d 180 -c`

## Usage

Run the script from the command line with the following arguments:

```bash
python PDFRotate.py [-h] [-d {90,180,270}] [-c] inputPath outputPath
```

```
positional arguments:
  inputPath             Path to the input PDF file or folder containing PDF files.
  outputPath            Path to save the rotated (and optionally compressed) PDF file or folder.

options:
  -h, --help            show this help message and exit
  -d {90,180,270}, --degrees {90,180,270}
                        Rotation angle in degrees (90, 180, or 270). Default is 90.
  -c, --compress        Compress the PDF after rotation.

Examples:
  1. Rotate a single PDF file by 180 degrees:
     python PDFRotate.py input.pdf output.pdf -d 180
  2. Rotate and compress all PDFs in a folder by 180 degrees:
     python PDFRotate.py input_folder output_folder -d 180 -c
```

