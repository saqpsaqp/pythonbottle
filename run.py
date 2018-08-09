#!/usr/bin/env python3
from bottle import run
from aplicacion import aplicacion

run (aplicacion, host="0.0.0.0", port=8888)
