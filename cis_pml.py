#!/home/gtd/cis_test_proj/bin/python
# -*- coding: utf-8 -*-

import sys
from pprint import pprint as pp
import cStringIO as cio
import string
import random

from say import say, fmt, stdout
from bs4 import BeautifulSoup

def create_fn_atom(size=6):
    chars = string.ascii_lowercase
    digits = string.digits
    fn_atom = ''.join( random.choice(chars) )
    return  fn_atom + ''.join( random.choice(chars + digits) for x in range(size-1) )

print create_fn_atom(8)

with open('cis.pml', 'rb') as f:
    soup = BeautifulSoup(f)

buf_main = cio.StringIO()
say.setfiles([stdout, buf_main])

buf_pml = cio.StringIO()

say( u'from pprint import pprint' )
say( u'def main():' )

for pml_raw in soup.find_all('pml'):
    # fn_atom = create_fn_atom(8)
    # say("def {fn_atom}():")
    buf_pml = cio.StringIO()

    for l in pml_raw.get_text().split('\n'):
        say(l)

    say( u'    pprint(pml)' )
    # say( "{fn_atom}()" )

print buf_main.getvalue()
