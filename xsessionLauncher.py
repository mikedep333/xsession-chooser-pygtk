#!/usr/bin/python3
#
# -*- coding: utf-8 -*-
import configparser
import os
import sys
from subprocess import call

def launch(filepath):
    config = configparser.ConfigParser()
    config.sections()
    config.read(filepath)
    xsession = config['Desktop Entry']
    os.environ['XDG_CURRENT_DESKTOP'] = xsession['DesktopNames']
    call(xsession['Exec'])
