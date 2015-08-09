#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
import sys
import configparser
import subprocess

class xsessionLauncher(object):
    def launch(filepath):
        config = configparser.ConfigParser()
        config.sections()
        config.read(filepath)
        xsession = config['Desktop Entry']
        os.environ['XDG_CURRENT_DESKTOP'] = xsession['DesktopNames']
        call(xsession['Exec'])
