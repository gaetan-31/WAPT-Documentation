# -*- coding: utf-8 -*-
from setuphelpers import *

uninstallkey = ['Mozilla Firefox 45.4.0 ESR (x64 fr)']

def install():
    print('installing tis-firefox-esr')
    run(r'"Firefox Setup 45.5.0esr.exe" -ms')
 
def uninstall():
    print('uninstalling tis-firefox-esr')
    run(r'"C:\Program Files\Mozilla Firefox\uninstall\helper.exe"                                                                                                                                                                                                                                                                                                                                                                                                     -ms')
