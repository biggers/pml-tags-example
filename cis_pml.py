#!/home/gtd/cis_test_proj/bin/python
# -*- coding: utf-8 -*-

import re
import sys
import string
import random
import cStringIO as CIO
from pprint import pprint

from say import say, fmt, stdout
from bs4 import BeautifulSoup, Tag, Comment

""" HOW.TO
PROJ=/usr/local/src/cis_test_proj
virtualenv $PROJ

cd $PROJ
. bin/activate
pip install beautifulsoup4 say

bin/python cis_pml.py
"""
_main_atom = 'pml_code_func'

_comment_re = r"""(<!--pml-\d+-->)"""
_comment_re = re.compile(_comment_re)

class SubHandler(object):
    def __init__(self, results):
        self.count = 0
        self.results = results

    def __call__(self, match):
        pml_block = self.results[ self.count ]
        content = """{}\n{}""".format( match.groups()[0], pml_block )
        self.count += 1
        return content

def main(args, debug=True):
    global results
    fn = args[1] if len(args) > 1 else 'cis.pml'

    with open(fn, 'rb') as f:
        soup = BeautifulSoup(f)

    buf_main = CIO.StringIO()
    say.setfiles([stdout, buf_main])

    say( u'from pprint import pprint' )
    say( u'import cStringIO as CIO')
    say( u'def {_main_atom}():' )
    say( u'    plist = list()' )

    for index, pml_tag in enumerate( soup.find_all('pml') ):
        bufc = CIO.StringIO()
        #         return "
        # <h3>Now, Good Bye...!</h3>
        # "
        for cld in pml_tag.children:
            if isinstance(cld, Tag):     # Python code could have HTML tags!
                bufc.write( repr(cld) )
            else:
                bufc.write( cld )

        say( bufc.getvalue() )
        bufc.close()
        say(u'    plist.append(pml)')    # append that <pml/> Py code ...

        # replace <pml/> ==>> <div><!-- pml-N --></div> - for Re.sub
        div = soup.new_tag("div")
        div.string = Comment( "pml-{}".format(index) )
        pml_tag.replace_with( div )

    say(u'    return plist')

    code = buf_main.getvalue()
    if debug:
        print( code )

    exec( code )                         # "execute" (to scope-in) the Py prog
    results = pml_code_func()            # run the Py-program from <pml> blocks
    if debug:
        pprint( [ item for item in results] )

    shtml = soup.prettify(formatter="minimal")
    if debug:
        print( shtml )

    shtml = _comment_re.sub( SubHandler(results), shtml )
    print( shtml )

if __name__ == '__main__':
    main(sys.argv)
