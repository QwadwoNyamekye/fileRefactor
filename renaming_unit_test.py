import os
import unittest
import renaming
import os
import xlrd
import shutil
from openpyxl import load_workbook
from openpyxl.styles import PatternFill
import re


class TestRenaming(unittest.TestCase):
    def test_files(self):
        self.assertEqual(renaming.renaming(), 1)
        self.assertIsInstance(
            renaming.check_path(os.listdir('.'), 0, xlrd.open_workbook('excel.xlsx')
                                , xlrd.open_workbook('excel.xlsx').sheet_by_name('Sheet1')), str)
        self.assertIsInstance(renaming.calc_rows(xlrd.open_workbook('excel.xlsx').sheet_by_name('Sheet1'),
                                                 os.listdir('.')[0], [],
                                                 xlrd.open_workbook('excel.xlsx').sheet_by_name('Sheet1').nrows), int)
        self.assertEqual(renaming.format_cells([]), int)
        self.assertEqual(renaming.rename_file('./final/COMMUNITY', [],
                              xlrd.open_workbook('excel.xlsx').sheet_by_name('Sheet1').nrows,
                              xlrd.open_workbook('excel.xlsx').sheet_by_name('Sheet1'), 'final', 2), 1)
