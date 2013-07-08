## PREREQs for this project:
## On Debian or Ubuntu Linux:
#
#  sudo apt-get -u install python-dev python-virtualenv
#  

# Note: Must use real Tabs, NOT spaces in a Makefile!

.ONESHELL:

PROJ = pml-tags-example

#.PHONY: all
all: creat_virtenv pip_install

# NOTE: Who's on first: the chicken or the egg?
# ... need this Makefile, but it's in the git-clone!
.PHONY: git_clone
git_clone: ${PROJ}/cis_pml.py

${PROJ}/cis_pml.py:
	git clone https://github.com/biggers/pml-tags-example.git


.PHONY: creat_virtenv
creat_virtenv: ${PROJ}/bin/pip

${PROJ}/bin/pip:
	virtualenv ${PROJ}

.PHONY: pip_install
pip_install: ${PROJ}/lib/python2.7/site-packages/say/__init__.py

${PROJ}/lib/python2.7/site-packages/say/__init__.py:
	${PROJ}/bin/pip install beautifulsoup4 say # bpython

