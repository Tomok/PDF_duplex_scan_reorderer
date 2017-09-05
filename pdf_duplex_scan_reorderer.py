from typing import Iterator

from PyPDF2 import PdfFileReader, PdfFileWriter

INPUT_FILE = "./Input.pdf"
OUTPUT_FILE = "./Output.pdf"


def flat_zip(*iterators: Iterator, zip_function=zip):
    for tup in zip_function(*iterators):
        for v in tup:
            yield v


def main():
    with open(INPUT_FILE, "rb") as readfile:
        input_pdf = PdfFileReader(readfile)
        page_cnt = input_pdf.getNumPages()
        front_pages = range(0, page_cnt // 2)
        back_pages = range(page_cnt - 1, page_cnt // 2 - 1, -1)
        pages_ordered = flat_zip(front_pages, back_pages)
        with open(OUTPUT_FILE, "wb") as writefile:
            output_pdf = PdfFileWriter()
            for page_no in pages_ordered:
                output_pdf.addPage(input_pdf.getPage(page_no))
            output_pdf.write(writefile)


if __name__ == '__main__':
    main()
