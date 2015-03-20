# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .import_csv import *


def register():
    Pool.register(
        CSVProfile,
        CSVColumnProfile,
        CSVImportLog,
        module='import_csv', type_='model')