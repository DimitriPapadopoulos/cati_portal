cati_manager
============
[![Build Status](https://travis-ci.org/sapetnioc/cati_manager.svg?branch=master)](https://travis-ci.org/sapetnioc/cati_manager)
[![Coverage Status](https://coveralls.io/repos/github/sapetnioc/cati_manager/badge.svg)](https://coveralls.io/github/sapetnioc/cati_manager?branch=master)
[![Python 27](https://img.shields.io/badge/python-2.7-blue.svg)](https://travis-ci.org/sapetnioc/cati_manager)
[![Python 35](https://img.shields.io/badge/python-3.5-blue.svg)](https://travis-ci.org/sapetnioc/cati_manager)


Getting Started
---------------
```
VENV=/tmp/venv<br>
SRC=/tmp/cati_manager

git clone https://github.com/sapetnioc/cati_manager.git $SRC
virtualenv $VENV
cd $SRC
$VENV/bin/python setup.py develop
$VENV/bin/initialize_cati_manager_db $SRC/development.ini
$VENV/bin/pserve development.ini --reload
```