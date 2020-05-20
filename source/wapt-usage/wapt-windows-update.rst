.. Reminder for header structure:
   Niveau 1: ====================
   Niveau 2: --------------------
   Niveau 3: ++++++++++++++++++++
   Niveau 4: """"""""""""""""""""
   Niveau 5: ^^^^^^^^^^^^^^^^^^^^

.. meta::
  :description: Using WAPT Windows Update Agent (WAPTWUA)
  :keywords: WAPT, Windows, Updates, WUA, documentation

.. _wapt_wua:

.. versionadded:: 1.7 Enterprise

Using WAPT Windows Update Agent (WAPTWUA)
=========================================

.. hint::

  Feature only available with WAPT **Enterprise** version

.. note::

  Since version 1.7, WAPT is able to manage Windows Updates on your endpoints.

  * the internals of WAPTWUA is based on the :abbr:`WUA (Windows Update Agent)`
    API;

  * for more information: https://docs.microsoft.com/en-us/windows/win32/wua_sdk/using-the-windows-update-agent-api;

Working principle
-----------------

Regularly, the WAPT server downloads an updated :file:`wsusscn2.cab` file
from Microsoft servers. By default, downloads happen once a day
and no download is triggered if the file has not changed
since the last download.

.. figure:: wapt-wua-diagramme-windows-update.png
  :align: center
  :alt: WAPT Windows Update flow process

  WAPT Windows Update flow process

.. note::

   In some cases, you may wish to push new KBs before the next Patch Tuesday
   release.

   To do so, you may follow :ref:`this documentation <simple_msu_packaging>`
   on packaging :mimetype:`.msu` files for these *Out-of-band* updates.

The :file:`wsusscn2.cab` file is then downloaded by the WAPT agent
from its nearest repository and then passed on to
the standard :abbr:`WUA (Windows Update Agent)` Windows utility
to crunch the update tree for the host.

Regularly, the host will analyze the available updates using
the :file:`wsusscn2.cab` file. The host will send its list of needed updates
as determined by its WUA to the WAPT server.

If an update is pending on the host and if that update is not present
on the WAPT server, the server will download the needed update
from official Microsoft servers.

.. hint::

  This mode of operation allows to download only the necessary updates
  on the computers, thus saving bandwidth, download time and disk space.

.. note:: Downloaded updates are stored:

  * on Linux hosts in :file:`/var/www/waptwua`;

  * on Windows hosts in :file:`C:\\wapt\\waptserver\\repository\\waptwua`;

The WAPT Windows Update Agent repository download URL is based
on the ``repo_url`` parameter in :file:`wapt-get.ini`:

* in case of repository replication, it is fully operational
  with WAPT Windows Update to reduce bandwidth use;

* do not forget to synchronize the :file:`waptwua` folder
  if you are replicating your packages with distant repositories;

.. note::

   If in your company, a proxy is needed to go out on the Internet,
   then be sure to :ref:`set the proxy server
   in the waptserver.ini file <waptserver_configuration>`.

Difference between WAPT Windows Updates and WSUS
++++++++++++++++++++++++++++++++++++++++++++++++

WSUS downloads all the updates for selected categories. This can lead to very large update database

WAPT Windows Update only downloads updates that have been asked by at least one computer client. This
helps to keep the local database small (a few 10s of Gigabytes) and it can be easily cleaned up 
if you want to recover space.

Major OS upgrades
+++++++++++++++++

Major OS upgrade are upgrade from one OS version to another. That includes, for example, upgrades
from Windows 7 to Windows 10, or from Windows 10 1803 to Windows 10 1903.

Major upgrade version are not handled in the same way as minor OS upgrades. Major upgrade are handled 
throught the download of the new install ISO content (same content as for a fresh install) and 
running setup.exe with the correct parameters. This process is the same for WSUS, SCCM and WAPT Windows Updates.

In the case of WAPT Windows Updates, you need to create a OS update package using a template package
provided on https://store.wapt.fr .

Drivers upgrades
++++++++++++++++

Drivers upgrades throught WSUS are not recommanded since it is hard to properly handle side effects. In the
case of WAPT Windows Updates, drivers are not downloaded since they are not referenced in the wsusscn2.cab 
files provided by Microsoft.

It is recommanded to push drivers updated through a custom package. If the fix is packaged as a msu file you
just need to launch the package wizard, select your msu file and click create package.

If the driver update is package as a zip containing the exe file, you can create a WAPT package containing the
necessary files and setup.exe binary with the correct silent flag.

Out of band KB
++++++++++++++

Microsoft does sometime provides OOB (Out of Band) updates that are not contained in the wsusscn2.cab index.
Those updates are not included in the main update because they may fix a very specific problem or may have
drawbacks in some situation.

If you want to deploy a OOB KB updates, you can download it from microsoft catalog https://www.catalog.update.microsoft.com/Home.aspx
and then package the MSU with the package wizard. 

You have to be carefull that OOB updates may break your system, be sure to read the prerequisite on the 
Microsoft bulletin corresponding to the update.


.. _wapt_wua_agent:

Configuring WAPTWUA on the WAPT agent
-------------------------------------

*WAPTWUA* is configured in :file:`wapt-get.ini`.

Add ``[waptwua]`` section.

You then have several options:

.. tabularcolumns:: |\X{5}{12}|\X{7}{12}|

============================== ==================================== ======================================================================================================================================================================
Options                        Default Value                        Description
============================== ==================================== ======================================================================================================================================================================
``enabled``                    False                                Enable or disable WAPTWUA on this machine.
``allow_direct_download``      False                                Allow direct download of updates from Microsoft servers if the WAPT server is not available
``default_allow``              False                                Set if missing update is authorized or not by default
``filter``                     Type='Software' or Type='Driver'     Define the filter to apply for the Windows update scan
``download_scheduling``        None                                 Set the Windows Update scan recurrence (Will not do anything if *waptwua* package rule or :file:`wsusscn2.cab` file have not changed) (ex: 2h)
``install_scheduling``         None                                 Set the Windows Update install recurrence (Will do nothing if no update is pending) (ex: 2h)
``install_at_shutdown``        False                                Install update when the machine will shutdown
``install_delay``              None                                 Set a deferred installation delay before publication in the repository (ex: 7d)
``allowed_severities``         None									                Define a severity list that will be automatically accepted during a wapt windows update scan. ex: *Important*, *Critical*, *Moderate*
============================== ==================================== ======================================================================================================================================================================

.. hint::

	These options can be set when generating the agent.

Example ``[waptwua]`` section in :file:`wapt-get.ini` file:

.. code-block:: ini

	[waptwua]
	enabled =true
	offline =true
	default_allow =false
	allow_direct_download=false
	download_scheduling=12h
	install_at_shutdown=true
	install_scheduling=12h
	install_delay=7d

The :guilabel:`install_scheduling` option will try every 12 hours
to install updates on client.
It is not in graphical options due to a potential danger. Indeed,
trying to install updates on your IT infrastructure
while working hours can impact your production.

When you create the :file:`waptagent.exe` from your console,
these options are equivalent to this:

  .. figure:: wapt-wua-agent-options.png
    :align: center
    :alt: WAPT Windows Update agent options

.. hint::

  if :guilabel:`default_allow` option is ``True`` and Wapt WUA is enabled too,
  clients will contact the WAPT Server and ask to download the missing
  updates. The clients will install missing updates on their own
  at time of upgrade.

Example package source code to modify ``[waptwua]`` settings:

.. code-block:: python

   def install():
    inifile_writestring(WAPT.config_filename,'waptwua','enabled','true')
    inifile_writestring(WAPT.config_filename,'waptwua','offline','true')
    inifile_writestring(WAPT.config_filename,'waptwua','filter',"Type='Software' or Type='Driver'")
    inifile_writestring(WAPT.config_filename,'waptwua','install_at_shutdown','true')
    inifile_writestring(WAPT.config_filename,'waptwua','download_scheduling','7d')
    inifile_writestring(WAPT.config_filename,'waptwua','allowed_severities','Critical,Important')

Using WAPTWUA from the console
------------------------------

The :guilabel:`WAPT Windows Update Agent` tab in the WAPT console
comes with two sub-menus to manage WAPTWUA.

WAPTWUA Package
+++++++++++++++

The :guilabel:`WAPTWUA Package` tab allows you to create *waptwua* rules packages.

* when this type of package is installed on a machine, it indicates
  to the WAPTWUA agent the authorized or forbidden
  :abbr:`KBs (Knowledge Base articles)`;

* when several *waptwua* packages are installed on a machine,
  the different rules will be merged;

* when a :file:`cab` is neither mentioned as authorized,
  nor mentioned as prohibited, WAPT agents will then
  take the value of ``default_allow`` in :file:`wapt-get.ini`;

If a Windows update has not yet been downloaded to the WAPT server,
then the WAPT agent will flag the update as *MISSING*.

.. note::

  * if the WAPTWUA agent configuration is set to ``default_allow = True``,
    then it will be necessary to specify the forbidden :file:`cab`;

  * if the WAPTWUA agent configuration is set to ``default_allow = False``,
    then it will be necessary to specify the authorized :file:`cab`;

.. hint::

  * to test updates on a small set of computers,
    you can set WAPTWUA default value to ``default_allow = False``;

  * you can test updates on a small sample of hosts and if everything is good,
    you can release the updates to the entire fleet of computers;

.. figure:: wapt_console-wua.png
  :align: center
  :alt: Creating a *waptwua* Package

  Creating a *waptwua* Package

Windows Updates list tab
++++++++++++++++++++++++

The :guilabel:`Windows Update List` tab lists all needed Windows Updates.

.. important::

   The server does not scan the :file:`wsussc2.cab` itself,
   it lets the WUA wapt agents do it.
   If an update seems to you as missing from the list, you must run a scan
   on one of the machines present in the console.
   If you run a WUA scan on a Windows 7 agent, the CAB and Windows 7
   files will be displayed on the Windows Update List tab.

The left pane displays updates categories, allowing you to filter by:

* criticality;

* product;

* classification;

In the right panel grid, if the :guilabel:`Downloaded on` column is empty,
it means that the update has not yet been downloaded by the WAPT server
and is not present on the WAPT server (This update is not missing on any host).

* you can force the download of an update by
  :menuselection:`right-click --> Download`;

* you can also force the download of the :file:`wsusscn2.cab` file with the
  :guilabel:`Download WSUSScan cab from Microsoft Web Site` button;

* you can see the Windows Updates download on the server
  with the :guilabel:`Show download task` button;

.. hint::

  To cleanup your :file:`waptwua` folder, you can remove
  no longer needed Windows updates. WAPT server will only re-download
  deleted updates if one of the WAPT equipped hosts requests it;

.. figure:: wapt-wua-windows-update-list.png
  :align: center
  :alt: List Windows Update

Launch WUA on clients
+++++++++++++++++++++

From the console you have three options.

.. figure:: wapt-wua-console-button.png
  :align: center
  :alt: List of wua button on console

The :guilabel:`Trigger the scan of pending Windows Updates` button
will launch the scan on the client and list all updates flagged for the OS.
You can scan the client from the console like that or by
using :command:`wapt-get waptwua-scan` from the command-line.

.. hint::

  Every 30 minutes, the WAPT Server will look for updates that have been requested
  at least once by WAPT Clients and that have not yet been downloaded and cached.
  If an update is pending, the WAPT Server will download it from official
  Microsoft servers.

  You can force this scan with the :guilabel:`Download index and missing cabs
  from Microsoft Web site` button in tab :menuselection:`Windows Updates -->
  Windows Updates list`

.. figure:: wapt-wua-console-pending.png
  :align: center
  :alt: WUA pending example

If you want to download from the console,
use the :guilabel:`Trigger the download of pending Windows Updates` button.

The command-line for downloading kb from the client is
:command:`wapt-get waptwua-download`, it will scan the current status of Windows
against current rules, download missing kb and send the result to the server.

If you want to install the pending update(s), use :command:`wapt-get waptwua-install`
from the command-line prompt.

If you want to trigger the installation from the console,
click on :guilabel:`Trigger the install of pending Windows Updates` button.

.. hint::

  When you want to install the pending updates stored in cache,
  the WAPT Service triggers the :abbr:`WUA (Windows Update Agent)` service.

  The WAPT Service will enable and start the WUA Service temporarily
  to install the updates. When updates are installed, waptservice will stop
  and disable the WUA service until the next cycle.

Video demonstration
-------------------

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/x36gAaT31Ko" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
