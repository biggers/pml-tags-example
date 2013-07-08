## PREREQs for this project:
## On Debian or Ubuntu Linux:
#
#  sudo apt-get -u install python-dev python-virtualenv
#  

# Note: Must use real Tabs, NOT spaces in a Makefile!

.ONESHELL:

PROJ = /var/tmp/foo_proj

#.PHONY: all
all: creat_virtenv pip_install


.PHONY: creat_virtenv
creat_virtenv: ${PROJ}

${PROJ}:
	virtualenv ${PROJ}

.PHONY: pip_install
pip_install: ${PROJ}/lib/python2.7/site-packages/say/__init__.py

${PROJ}/lib/python2.7/site-packages/say/__init__.py:
	${PROJ}/bin/pip install beautifulsoup4 say # bpython
