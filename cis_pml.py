#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import StringIO as SIO
from pprint import pprint

from say import say, fmt, stdout
from bs4 import BeautifulSoup, Tag, Comment

_main_atom = 'pml_code_func'

_comment_re = r"""(<!--pml-\d+-->)"""
_comment_re = re.compile(_comment_re)

class LeadingIndent(object):
    """ keep state on PML.#0 leading indent, use to adjust
        other PML "code blocks" to that indentation-level
    """
    def __init__(self, first_pml):
        self.first_indent = self.get_pml_indent(first_pml)
        self.first_pml = first_pml

    def get_pml_indent(self, pml_block):
        m = re.search('(\n)(\s+)(\S+)', pml_block)
        return  len( m.group(2) )

    def sub_whitespace(self, m):
        ws = ' ' * self.first_indent
        adj_pml = m.group(1) + ws + m.group(3)
        return adj_pml

    def __call__(self, next_pml):
        if next_pml == self.first_pml:
            return self.first_pml
        self.leading = self.get_pml_indent(next_pml)
        re_range = '{{{0},{0}}}'.format(self.leading)
        pml_adj = re.sub('(\n*)([ \t]{})([^\n]+)'.format(re_range),
                         self.sub_whitespace, next_pml) #flags=re.DEBUG
        return pml_adj

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

def main(args, debug=False):
    fn = args[1] if len(args) > 1 else 'cis.pml'

    with open(fn, 'rb') as f:
        soup = BeautifulSoup(f)

    buf_main = SIO.StringIO()
    say.setfiles([buf_main])

    say( u'def {_main_atom}():' )
    say( u'    plist = list()' )

    adjuster = None
    for index, pml_tag in enumerate( soup.find_all('pml') ):
        bufc = SIO.StringIO()
        #         return "
        # <h3>Now, Good Bye...!</h3>
        # "
        for cld in pml_tag.children:
            if isinstance(cld, Tag):     # BS4 parses HTML tags in <pml/>!
                bufc.write( repr(cld) )
            else:
                if index == 0:            # we get "leading indent" from PML-0
                    if adjuster == None:
                        adjuster = LeadingIndent(cld)
                else:
                    cld = adjuster( cld )

                bufc.write( cld )

        say( bufc.getvalue() )
        bufc.close()
        say(u'    plist.append(pml)')   # append that <pml/> Py code ...

        # replace <pml/> ==>> <div><!-- pml-N --></div> - for Re.sub
        div = soup.new_tag("div")
        div.string = Comment( "pml-{}".format(index) )
        pml_tag.replace_with( div )

    say(u'    return plist')

    the_code = buf_main.getvalue()
    with open("out.py", 'wb') as fp:
        fp.write(the_code)
    buf_main.close()

    if debug == True:
        print( the_code )
    exec( the_code )                     # "execute" (to scope-in) the Py prog

    results = pml_code_func()            # run the Py-program from <pml> blocks
    if debug == True:
        pprint( [ item for item in results] )

    shtml = soup.prettify(formatter="minimal")
    shtml = _comment_re.sub( SubHandler(results), shtml )
    print( shtml )

if __name__ == '__main__':
    main(sys.argv)
