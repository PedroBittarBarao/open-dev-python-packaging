#!/usr/bin/env python3
import dev_aberto
import gettext
from datetime import date
import babel.dates as bd
gettext.bindtextdomain('cli', 'locale')
gettext.textdomain('cli')
_ = gettext.gettext


if __name__ == '__main__':
    try:
        data, name = dev_aberto.hello()
        print(_('Last commit made in:'), bd.format_date(data), _(' by'), name)
    except:
        name = "fish"
        print(_('Last commit made in:'), bd.format_date(), _(' by'), name)


    
