.. Reminder for header structure:
   Niveau 1: ====================
   Niveau 2: --------------------
   Niveau 3: ++++++++++++++++++++
   Niveau 4: """"""""""""""""""""
   Niveau 5: ^^^^^^^^^^^^^^^^^^^^

.. meta::
    :description: WAPT Community and WAPT Enterprise
    :keywords: WAPT Community, WAPT Enterprise, WAPT, documentation

.. _WAPT_Enterprise:

WAPT Community and WAPT Enterprise
==================================

.. toctree::
  :maxdepth: 1

  wapt-enterprise-community-comparison.rst

Main functional benefits of the Enterprise version of WAPT
----------------------------------------------------------

.. figure:: ./icons/wapt_enterprise.png
   :align: center
   :alt: Logo WAPT Enterprise

WAPT is designed to help IT system administrators manage the lifecycle
of their installed base of Windows applications, drivers, OSes
and configurations in system and user context.

With WAPT Enterprise, you benefit automatically from the base functions
included in WAPT Community to help you deploy, upgrade and remove software
and configurations on your Windows devices, from a central console.

WAPT is an *opencore* model and the **Enterprise** version is based
on the **Community** version with the following features designed
to answer the needs of larger Organisations:

* **Active Directory authentication** of WAPT package developers,
  package deployers, self-service users and for the initial registering
  of the WAPT agents with the WAPT Server. In addition, the display
  of WAPT equipped devices in the WAPT console follow the same structure
  as the hierarchical structure of the Organization's Active Directory
  :abbr:`OU (Organizational Units)`;

* **role separation between package developers and package deployers**.
  This way, central IT teams may build the software packages because they know
  the Organization's security guidelines, and local IT teams may deploy
  the WAPT packages because they know the needs of their user base.
  Such a separation is implemented using differentiated sets of keys
  (i.e. **Code Signing** SSL certificates for package developers and **Simple**
  SSL certificates for package deployers);

* **differentiated self service**
  WAPT Enterprise allows you to apply lists of allowed packages
  to groups in Active Directory.
  Allowed users are free to install qualified packages from their list
  of approved packages without having to submit a ticket to their IT teams.

* **WAPT WUA**
  WAPT allows to manage the Windows Updates on your endpoints.

* **advanced reporting for corporate teams**.
  This reporting completes the operational reporting already available
  in the WAPT console; reports help WAPT operators demonstrate their efficacy
  with WAPT for insuring a greater level of security and conformity
  for their networks, systems, software and applications.

* **dynamic repository configuration**.
  Starting with WAPT 1.8, repository replication can be enabled using a WAPT agent
  installed on an existing machine, a dedicated appliance or Virtual Machine.

  The replication role is deployed through a WAPT package that enables
  the :program:`Nginx web server` and configures scheduling, packages types,
  packages sync, and much more.

  This feature allows WAPT agents to find dynamically their closest available
  WAPT repository from a list of rules stored on the WAPT server.

The Enterprise version of WAPT is particularly advisable for Organizations:

* that manage large installed bases of devices (generally above 300 units);

* that are spread geographically with many subsidiaries or production sites;

* that require a strong traceability of actions performed on the installed base
  of devices for reasons of audit or security;

Description of services available with the WAPT Enterprise contract
-------------------------------------------------------------------

Access to future improvements in WAPT Enterprise
++++++++++++++++++++++++++++++++++++++++++++++++

By subscribing to a WAPT Enterprise contract and by maintaining
your subscription valid, you benefit from the future improvements brought into
the core of WAPT and you benefit automatically from all future improvements
to the WAPT Enterprise version.

A lapsing of your subscription will automatically switch your WAPT instance
back to its corresponding Community version; advanced functions only available
in the Enterprise version will no longer be accessible.

Direct telephone support for your daily usage of WAPT
+++++++++++++++++++++++++++++++++++++++++++++++++++++

When your subscription reaches above a certain volume, Tranquil IT, the creator
of WAPT, allows you a privileged access to its core team of WAPT experts
and developers.

We give you access to a dedicated telephone hot-line with a direct answer
to satisfy your needs for support.

We are committed to providing you with reliable and pertinent answers
on the subscribed perimeter, quickly.

By subscribing or renewing your WAPT Enterprise contract, you will receive
a notification indicating the practicalities to access our support.

.. attention::

  The support concerns only the use in your Organization
  of the WAPT Enterprise software; additional support for adapting,
  personalizing, debugging or creating WAPT packages may be obtained
  with prepaid support tickets.

Up to two individuals in your Organisation may communicate
with our direct support.

Price and preferential access to WAPT training
++++++++++++++++++++++++++++++++++++++++++++++

You may choose to train your IT team on any particularity of WAPT.

WAPT Enterprise subscribers benefit from a privileged access to Tranquil IT's
training advisers and a 50% discount on standard training prices.

Why does Tranquil IT display a 300 device limit for WAPT Community on her commercial documentation ?
----------------------------------------------------------------------------------------------------

Tranquil IT displays a 300 device limit on her commercial documentation
for the WAPT Community version.

.. note::

  There is **no technical restriction to using the Community version**,
  it is available as free software.

  Tranquil IT's philosophy regarding free software is to give back a little
  of what we took, so it is important to us to keep our original promise
  to give systems administrators a mean to deploy, maintain up-to-date
  and remove software and configurations on their installed base
  of Windows devices.

What you will find in the WAPT Enterprise version are features
that are designed to help administer large installed bases and we meet people
in that situation daily.

As a general rule, we have observed that advanced management needs start
to be felt when the number of devices goes over 300-400 units.
