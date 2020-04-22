.. Reminder for header structure:
   Niveau 1: ====================
   Niveau 2: --------------------
   Niveau 3: ++++++++++++++++++++
   Niveau 4: """"""""""""""""""""
   Niveau 5: ^^^^^^^^^^^^^^^^^^^^

.. meta::
  :description: Recompiling WAPT from source
  :keywords: Python, WAPT, virtualenv, CodeTyphon, Lazarus, InnoSetup,
             documentation

Recompiling WAPT from source
============================

Building the WAPT Agent for Windows
-----------------------------------

WAPT requirements
+++++++++++++++++

Python environment
""""""""""""""""""

* Python 2.7.13;

* client python libraries in :file:`requirements.txt`;

* server python libraries in :file:`requirements-server.txt`;

Lazarus environment
"""""""""""""""""""

WAPT relies on the following third-party freepascal/ lazarus librairies:

* pl_indy: https://www.pilotlogic.com/sitejoom/index.php/115-wiki/ct-packages/networking/271-pl-indy;

* superobject: https://github.com/hgourvest/superobject;

* virtualtrees: https://www.pilotlogic.com/sitejoom/index.php/85-wiki/codetyphon-studio/ct-packages/301-pl-virtualtrees
  and https://github.com/blikblum/VirtualTreeView-Lazarus;

* python4delphi: https://github.com/pyscripter/python4delphi;

* delphizmq: https://github.com/bvarga/delphizmq;

* JCL: https://wiki.delphi-jedi.org/wiki/JCL_Installation;

* thmtlport: https://svn.code.sf.net/p/lazarus-ccr/svn/components/thtmlport/;

Tranquil IT packages
""""""""""""""""""""

* pltis_python4delphi: https://github.com/tranquilit/pltis_python4delphi;

* pltis_utils: https://github.com/tranquilit/pltis_utils: subset of libraries
  from JEDI JCL project adapted to lazarus;

* pltis_sogrid: https://github.com/tranquilit/pltis_sogrid;

* pltis_superobject: https://github.com/tranquilit/pltis_superobject;

Creating a development environment with virtualenv
++++++++++++++++++++++++++++++++++++++++++++++++++

With a clean Windows installed:

* install python2.7.12 from https://www.python.org/ftp/python/2.7.12/python-2.7.12.msi;

* upgrade :program:`python-setuptools`:

.. code-block:: bash

    c:\python27\python -m pip install -U pip setuptools

* create a development environment with ``virtualenv``;

  .. code-block:: bash

      mkdir c:\tranquilit
      git clone git@github.com:tranquilit/WAPT.git (ou git clean -fxd ...)
      cd c:\tranquilit\wapt init_workdir.bat

Installing the WAPT development environment
+++++++++++++++++++++++++++++++++++++++++++

On a clean Windows 7 install as a :term:`Local Administrator`:

* install the WAPT agent from https://srvwapt.mydomain.lan/wapt/waptagent.exe;

* deactivate UAC;

* show hidden files and file extensions;

* increase the width of the CMD windows and flip to quick edit mode;

* copy the code signing certificate into :file:`C:\\users\\buildbot\\Documents`;

Installing Lazarus
++++++++++++++++++

.. code-block:: batch

    wapt-get install tis-pyscripter tis-tortoisegit tis-7zip tis-python27 tis-notepadplusplus tis-firefox tis-putty tis-lazarus tis-openssh tis-signtool

    wget https://www.sqlite.org/2018/sqlite-dll-win32-x86-3250200.zip
    unzip sqlite3.dll dans C:\Windows\SysWOW64
    md c:\tranquilit

    git.exe clone  --recurse-submodules "ssh://htouvet@srvdev.ad.tranquil.it:29418/wapt/wapt.git" "C:\tranquilit\wapt"
    REM git pull --recurse-submodules=yes --ff-only)
    cd  \tranquilit\wapt
    init_workdir.bat

    git clone git://srvdev.ad.tranquil.it/wapt/pltis_indy.git c:\tranquilit\pltis_indy
    git clone git://srvdev.ad.tranquil.it/wapt/pltis_utils.git c:\tranquilit\pltis_utils
    git clone git://srvdev.ad.tranquil.it/wapt/pltis_sogrid.git  c:\tranquilit\pltis_sogrid
    git clone git://srvdev.ad.tranquil.it/wapt/pltis_superobject.git  c:\tranquilit\pltis_superobject
    git clone git://srvdev.ad.tranquil.it/wapt/Python-for-Lazarus.git  c:\tranquilit\Python-for-Lazarus
    git clone git://srvdev.ad.tranquil.it/wapt/pltis_virtualtrees.git c:\tranquilit\pltis_virtualtrees
    git clone git://srvdev.ad.tranquil.it/wapt/pltis_virtualtreesextra.git c:\tranquilit\pltis_virtualtreesextra
    git clone git://srvdev.ad.tranquil.it/wapt/pltis_dcpcrypt.git c:\tranquilit\pltis_dcpcrypt
    git clone git://srvdev.ad.tranquil.it/wapt/pltis_luipack.git c:\tranquilit\pltis_luipack
    git clone git://srvdev.ad.tranquil.it/wapt/pltis_synapse.git c:\tranquilit\pltis_synapse

    c:\lazarus\lazbuild.exe --add-package c:\tranquilit\pltis_dcpcrypt\dcpcrypt_laz.lpk
    c:\lazarus\lazbuild.exe --add-package c:\tranquilit\pltis_indy\indylaz.lpk
    c:\lazarus\lazbuild.exe c:\tranquilit\pltis_utils\pltis_utils.lpk
    c:\lazarus\lazbuild.exe c:\tranquilit\pltis_superobject\pltis_superobject.lpk
    c:\lazarus\lazbuild.exe --add-package c:\tranquilit\pltis_virtualtrees\pltis_virtualtrees.lpk
    c:\lazarus\lazbuild.exe --add-package c:\tranquilit\pltis_virtualtreesextra\pltis_virtualtreesextra.lpk
    c:\lazarus\lazbuild.exe --add-package c:\tranquilit\pltis_sogrid\pltis_sogrid.lpk
    c:\lazarus\lazbuild.exe --add-package c:\tranquilit\pltis_dcpcrypt\dcpcrypt_laz.lpk
    c:\lazarus\lazbuild.exe c:\tranquilit\pltis_synapse\laz_synapse.lpk
    c:\lazarus\lazbuild.exe --add-package c:\tranquilit\pltis_luipack\luicomponents\luicomponents.lpk
    c:\lazarus\lazbuild.exe --add-package c:\tranquilit\pltis_luipack\luicomponents\luicomponents.lpk
    c:\lazarus\lazbuild.exe --add-package C:\tranquilit\Python-for-Lazarus\python4lazarus\python4lazarus_package.lpk
    c:\lazarus\lazbuild.exe --add-package C:\lazarus\components\anchordocking\design\anchordockingdsgn.lpk
    c:\lazarus\lazbuild.exe --build-ide=
    c:\lazarus\lazbuild.exe c:\tranquilit\wapt\wapt-get\pltis_wapt.lpk

    REM depending on version, change community to enterprise
    waptpython build_exe.py community

Installing the server environment on Windows
++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

    cd \tranquilit\wapt
    waptpython waptserver\winsetup.py all

Creating the InnoSetup installers
+++++++++++++++++++++++++++++++++

* install Innosetup from
  https://jrsoftware.org/download.php/ispack-unicode.exe

The :file:`.iss` files are located in :file:`C:\\tranquilit\\wapt\\waptsetup`;

The :program:`waptsetup` installer includes the python libraries,
the command line tool :program:`wapt-get`, the local webservice
:program:`waptservice`, the packaging tool and the WAPT console
:program:`waptconsole`.

The file :file:`waptserver.iss` allows to build an installer that includes
a Nginx web server in front and the Flask webservice :program:`waptserver.py`.

The :file:`waptstarter` installer only includes the local webservice and
the command line tool :program:`wapt-get`. It does not include the WAPT console
:program:`waptconsole`, nor the packaging tools.

:menuselection:`Right-click on the .iss file --> Compile ` will compile
an installer with :program:`InnoSetup`.

or using the command line:

.. code-block:: bash

  "C:\Program Files (x86)\Inno Setup 5\ISCC.exe" C:\tranquilit\wapt\waptsetup\waptsetup.iss

The installer's global parameters are defined with *#define* in the file header.

If you do not sign the installers, you may comment
the lines :code:`#define signtool ..`.

Building the WAPT Agent for MacOS
---------------------------------

Generating the agent package
++++++++++++++++++++++++++++

* if you do not have access to the :command:`sudo` command,
  you'll need to `enable the root user <https://support.apple.com/en-us/HT204012>`_;

* from the root of the WAPT directory, navigate to waptservice/pkg;

* execute the *createpkg* script with administrator rights;

  .. code-block:: bash

     sudo ./createpkg.py

It may ask for additional software (the Command Line Developer Tools)
and install them after a prompt which you should answer :guilabel:`Yes` to;

* the agent package should have been generated, under a name
  along the lines of :file:`tis-waptagent-1.7.6.6550-tismacos-fdc24bca.pkg`;

Installing the agent package
++++++++++++++++++++++++++++

* execute the following command on your MacOS:

  .. code-block:: bash

     sudo installer -pkg tis-waptagent*.pkg -target /

If the installation is successful, you should have the wapt files in
:file:`/opt` and access to the :command:`wapt`, :command:`wapt-get`,
:command:`waptpython` and :command:`waptservice` commands.

* the agent should launch at the next reboot, but you probably want to start it
  right away with the following command:

  .. code-block:: bash

     sudo launchctl load -w /Library/LaunchDaemons/wapt.plist

Building the WAPT Agent for Linux
---------------------------------

Building the environment on Debian Linux
++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

    mkdir ~/tranquilit/
    cd ~/tranquilit/
    git clone git@github.com:tranquilit/WAPT.git
    cd ~/tranquilit/wapt/waptserver/deb
    python createdeb.py
    cd ~/tranquilit/wapt/waptrepo/deb
    python createdeb.py
