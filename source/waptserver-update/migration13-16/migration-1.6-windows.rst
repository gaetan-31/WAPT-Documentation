.. Reminder for header structure:
   Niveau 1: ====================
   Niveau 2: --------------------
   Niveau 3: ++++++++++++++++++++
   Niveau 4: """"""""""""""""""""
   Niveau 5: ^^^^^^^^^^^^^^^^^^^^

.. meta::
   :description: Upgrading the WAPT Server on Windows
   :keywords: upgrading, upgrade, WAPT, 1.3, 1.6, Windows, documentation

.. _upgrade_1.3_1.6_windows:

Upgrading WAPT from 1.3 to 1.6 on Windows
+++++++++++++++++++++++++++++++++++++++++

.. attention::

   WAPT Server no longer installs on x86 versions of Windows.

* download the latest version of :program:`waptserversetup`
  1.6 from https://wapt.tranquil.it/wapt/releases/latest/;

* launch the installation on top of the existing 1.3 version by following
  :ref:`this documentation <wapt-server_win_install>`;

.. note::

  At the end of the post-configuration step, :program:`waptserver`
  will detect that you are upgrading from WAPT 1.3.13 and will ask you to
  launch the migration of the database from MongoDB to PostgreSQL.

* click on :guilabel:`Yes`;

* launch the WAPT console

.. note::

   If you come from a WAPT 1.3.13 version running with IIS, the WAPT
   listening ports must be changed. In that case, follow the documentation for
   :ref:`changing the listening port <windows_changing_port_80_443>`.

You may now go to the next step to :ref:`generate the necessary
keys <key-regenerate>`!!

Migrating WAPT 1.3 from a Windows OS to a Linux OS
""""""""""""""""""""""""""""""""""""""""""""""""""

The simplest method is to move over to a Linux based version
of :program:`waptserver`.

* download :program:`mongodb` from https://www.mongodb.com/download-center/community;

* extract :file:`mongodump.exe` from the archive;

.. note::

  A dump folder should have been created in the same directory
  as the :file:`mongodump.exe` file.

* backup the entire directory :file:`C:\\wapt` of the WAPT Server;

* backup the folder :file:`C:\\private`;

* install a fresh version **1.3.13** of WAPT on Linux (debian 8 x64)
  or CentOS7/ RedHat7 (x64);

.. hint::

  To install a new Linux Debian 10 (Buster) on a physical or virtual machine
  without a graphical user interface, please visit the official
  documentation for `Debian9 <https://www.debian.org/releases/buster/amd64/>`_.

* if the WAPT agents point to an IP address, then the new Debian based WAPT
  Server must have the same IP address as the old Windows based WAPT Server.

* if the WAPT agents point to a DNS CNAME, then you may point the :term:`DNS`
  field *srvwapt* to the IP address of the new Linux server.

* update the download sources;

.. code-block:: bash

  apt-get update && apt-get upgrade

* install the WAPT Server;

.. note::

  The utilities :program:`tis-waptserver`, :program:`tis-waptsetup`
  et :program:`tis-waptrepo` are signed; it is therefore necessary to recover
  the GPG key below to avoid warning messages when installing them.

.. code-block:: bash

  apt-get install apt-transport-https lsb-release systemd-sysv systemd
  wget -O - https://wapt.tranquil.it/debian/tiswapt-pub.gpg  | apt-key add -
  echo  "deb  https://wapt.tranquil.it/debian/wapt-1.3/ $(lsb_release -c -s) main"  > /etc/apt/sources.list.d/wapt.list
  apt-get update
  apt-get install tis-waptserver tis-waptrepo tis-waptsetup

* launch the configuration script;

.. code-block:: bash

  /opt/wapt/waptserver/scripts/postconf.sh

.. note::

  The password requested in step 4 is used to access the WAPT console.

* configure the WAPT Server;

* start the WAPT Server;

.. code-block:: bash

  systemctl start waptserver

* restore the WAPT packages on the Linux server;

  * upload the content of :file:`C:\\wapt\waptserver\\repository\\wapt`
    in :file:`/var/www/wapt/`;

  * upload the content of :file:`C:\\wapt\waptserver\\repository\\wapt-host`
    in :file:`/var/www/wapt-host/`;

  .. hint::

    You may upload the files on the Linux Server using the
    :program:`WinSCP` utility.

  * then change the owner of the files to wapt:

    .. code-block:: bash

      chown wapt:www-data /var/www/wapt*

* restore the MongoDB database on the Linux server:

  * using :program:`WinSCP`, upload the MongoDB dump folder in :file:`/root/`;

  * restore the MongoDB dump on your Linux hosted MongoDB instance:

    .. code-block:: bash

      mongorestore /root/dump

Your WAPT Server now works in 1.3.13 on Linux.

You may now install your :program:`waptagent` on your :term:`Administrator`
management PC and restore the :file:`C:\\private` folder on your workstation.

.. attention::

  You must not regenerate a private key, you must only point to your private
  key in the console. You must also refill the package prefix.

You may now follow the classic procedure to upgrade from 1.3.13 to 1.6!!
