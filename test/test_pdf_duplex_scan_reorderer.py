from unittest import TestCase

from pdf_duplex_scan_reorderer import flat_zip, gen_page_order


class TestPdfDuplexScanReorderer(TestCase):
    def test_flat_zip(self):
        self.assertListEqual(list(flat_zip([1, 2], ['a', 'b'])),
                             [1, 'a', 2, 'b'])

    def test_gen_page_order(self):
        with self.subTest("Even page count"):
            self.assertListEqual(list(gen_page_order(4)), [0, 3, 1, 2])

        with self.subTest("Odd page count"):
            self.assertListEqual(list(gen_page_order(5)), [0, 4, 1, 3, 2])
