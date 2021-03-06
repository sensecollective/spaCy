# coding: utf8
from __future__ import unicode_literals

# import the symbols for the attrs you want to overwrite
from ...attrs import LIKE_NUM

# check if token resembles a number

_num_words = ['nolla', 'yksi', 'kaksi', 'kolme', 'neljä', 'viisi', 'kuusi', 'seitsemän', 'kahdeksan', 'yhdeksän', 'kymmenen', 'yksitoista', 'kaksitoista', 'kolmetoista' 'neljätoista', 'viisitoista', 'kuusitoista', 'seitsemäntoista', 'kahdeksantoista', 'yhdeksäntoista', 'kaksikymmentä', 'kolmekymmentä', 'neljäkymmentä', 'viisikymmentä', 'kuusikymmentä'v, 'seitsemänkymmentä', 'kahdeksankymmentä', 'yhdeksänkymmentä', 'sata', 'tuhat', 'miljoona', 'miljardi', 'triljoona']


def like_num(text):
    text = text.replace('.', '').replace(',', '')
    if text.isdigit():
        return True
    if text.count('/') == 1:
        num, denom = text.split('/')
        if num.isdigit() and denom.isdigit():
            return True
    if text in _num_words:
        return True
    return False

LEX_ATTRS = {
    LIKE_NUM: like_num
}
