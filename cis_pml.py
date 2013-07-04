#!/home/gtd/cis_test_proj/bin/python
# -*- coding: utf-8 -*-

import sys
from pprint import pprint as pp
import cStringIO as CIO
import string
import random
import pdb

from say import say, fmt, stdout
from bs4 import BeautifulSoup, Tag

def creat_py_atom(size=6):
    """ create a valid Python-id (for variables, fn-names) with length 'size'
    """
    chars = string.ascii_lowercase
    digits = string.digits
    fn_atom = ''.join( random.choice(chars) )
    return  fn_atom + ''.join( random.choice(chars + digits + '_') for x in range(size-1) )

def main(args):
    main_atom = 'ghost_func'    # creat_py_atom(8)

    fn = args[1] if len(args) > 1 else 'cis.pml'

    with open(fn, 'rb') as f:
        soup = BeautifulSoup(f)

    buf_main = CIO.StringIO()
    say.setfiles([stdout, buf_main])

    say( u'from pprint import pprint' )
    say( u'import cStringIO as CIO')
    say( u'def {main_atom}():' )
    say( u'    plist = list()' )

    for pml_tag in soup.find_all('pml'):
        # pdb.set_trace()

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
        say(u'    plist.append(pml)')

    say(u'    return plist')
    # say( u'{main_atom}()' )

    code = buf_main.getvalue()
    print( code )
    exec( code )

    l = ghost_func()
    # for pml_tag in soup.find_all('pml'):
    #     pass

    pp( [ item for item in l] )


if __name__ == '__main__':
    main(sys.argv)
