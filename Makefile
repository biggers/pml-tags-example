## PREREQs for this project:
## On Debian or Ubuntu Linux:
#
#  sudo apt-get -u install python-dev python-virtualenv
#  

# Note: Must use real Tabs, NOT spaces in a Makefile!

.ONESHELL:

PROJ = pml-tags-example
#VIRTENV_PATH = /usr/local/encap/Python-2.7.6/bin
VIRTENV_PATH = /usr/bin

.PHONY: all git_clone creat_virtenv pip_install

all: creat_virtenv pip_install

# NOTE: Who's on first: the chicken or the egg?
# ... need this Makefile, but it's in the git-clone!
git_clone: ${PROJ}/cis_pml.py

${PROJ}/cis_pml.py:
	git clone https://github.com/biggers/pml-tags-example.git

creat_virtenv: ${PROJ}/bin/pip

${PROJ}/bin/pip:
	${VIRTENV_PATH}/virtualenv ${PROJ}

pip_install: ${PROJ}/lib/python2.7/site-packages/say/__init__.py

${PROJ}/lib/python2.7/site-packages/say/__init__.py:
	cd ${PROJ}; bin/pip install beautifulsoup4 say
