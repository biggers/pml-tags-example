#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import string
import random
import StringIO as SIO
from pprint import pprint

from say import say, fmt, stdout
from bs4 import BeautifulSoup, Tag, Comment

_main_atom = 'pml_code_func'

_comment_re = r"""(<!--pml-\d+-->)"""
_comment_re = re.compile(_comment_re)

class SubHandler(object):
    """ re.sub handler Class, to insert Py-run results from <pml/> into HTML-doc
    """
    def __init__(self, results):
        self.count = 0
        self.results = results

    def __call__(self, match):
        pml_block = self.results[ self.count ]
        content = """{}\n{}""".format( match.groups()[0], pml_block )
        self.count += 1
        return content

def main(args, debug=True):
    fn = args[1] if len(args) > 1 else 'cis.pml'

    with open(fn, 'rb') as f:
        soup = BeautifulSoup(f)

    buf_main = SIO.StringIO()
    say.setfiles([stdout, buf_main])

    say( u'def {_main_atom}():' )
    say( u'    plist = list()' )

    for index, pml_tag in enumerate( soup.find_all('pml') ):
        bufc = SIO.StringIO()
        #         return "
        # <h3>Now, Good Bye...!</h3>
        # "
        for cld in pml_tag.children:
            if isinstance(cld, Tag):     # BS4 parses HTML tags in <pml/>!
                bufc.write( repr(cld) )
            else:
                bufc.write( cld )

        say( bufc.getvalue() )
        bufc.close()
        say(u'    plist.append(pml)')   # append that <pml/> Py code ...

        # replace <pml/> ==>> <div><!-- pml-N --></div> - for Re.sub
        div = soup.new_tag("div")
        div.string = Comment( "pml-{}".format(index) )
        pml_tag.replace_with( div )

    say(u'    return plist')

    raw_code = buf_main.getvalue()
    clean_code = raw_code
    buf_main.close()

    if debug:
        print( clean_code )
    exec( clean_code )                   # "execute" (to scope-in) the Py prog

    results = pml_code_func()            # run the Py-program from <pml> blocks
    if debug:
        pprint( [ item for item in results] )

    shtml = soup.prettify(formatter="minimal")
    shtml = _comment_re.sub( SubHandler(results), shtml )
    print( shtml )

if __name__ == '__main__':
    main(sys.argv)
