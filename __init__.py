# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .import_csv import *


def register():
    Pool.register(
        ProfileCSV,
        ProfileCSVColumn,
        ImportCSVLog,
        ImportCSVStart,
        module='import_csv', type_='model')
    Pool.register(
        ImportCSV,
        module='import_csv', type_='wizard')
