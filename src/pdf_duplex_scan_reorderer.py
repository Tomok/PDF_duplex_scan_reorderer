from typing import Iterator

from PyPDF2 import PdfFileReader, PdfFileWriter

INPUT_FILE = "./Input.pdf"
OUTPUT_FILE = "./Output.pdf"


def flat_zip(*iterators: Iterator, zip_function=zip):
    """
    Zips the items yielded by iterator, but instead of returning tuples,
    it returns the items in the tuples.

    e.g. list(flat_zip([1, 2],['a', 'b']) = [1, 'a', 2, 'b']
    :param iterators:  Iteratores
    :param zip_function: function used to zip the iterators (to allow zip_longest and similar)
    :return: items from within the iterators
    """
    for tup in zip_function(*iterators):
        for v in tup:
            yield v


def gen_page_order(page_cnt: int):
    """
    Creates an iterator that sorts the pages in the new order
    :param page_cnt: Overall page count of the document, if even assumes last page was empty and not included
    :return: iterator of page numbers belonging to the old document (starting with 0),
        yields in order they should be in the new document
    """
    front_pages = range(0, page_cnt // 2)
    back_pages = range(page_cnt - 1, page_cnt // 2 - 1, -1)
    pages_ordered = flat_zip(front_pages, back_pages)
    return pages_ordered


def main():
    """ main function """
    with open(INPUT_FILE, "rb") as readfile:
        input_pdf = PdfFileReader(readfile)
        page_cnt = input_pdf.getNumPages()
        pages_ordered = gen_page_order(page_cnt)
        with open(OUTPUT_FILE, "wb") as writefile:
            output_pdf = PdfFileWriter()
            for page_no in pages_ordered:
                output_pdf.addPage(input_pdf.getPage(page_no))
            output_pdf.write(writefile)


if __name__ == '__main__':
    main()
