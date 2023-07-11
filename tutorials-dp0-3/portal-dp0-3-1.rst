.. Review the README on instructions to contribute.
.. Review the style guide to keep a consistent approach to the documentation.
.. Static objects, such as figures, should be stored in the _static directory. Review the _static/README on instructions to contribute.
.. Do not remove the comments that describe each section. They are included to provide guidance to contributors.
.. Do not remove other content provided in the templates, such as a section. Instead, comment out the content and include comments to explain the situation. For example:
	- If a section within the template is not needed, comment out the section title and label reference. Do not delete the expected section title, reference or related comments provided from the template.
    - If a file cannot include a title (surrounded by ampersands (#)), comment out the title from the template and include a comment explaining why this is implemented (in addition to applying the ``title`` directive).

.. This is the label that can be used for cross referencing this file.
.. Recommended title label format is "Directory Name"-"Title Name" -- Spaces should be replaced by hyphens.
.. _Tutorials-Examples-DP0-3-Portal-1:
.. Each section should include a label for cross referencing to a given area.
.. Recommended format for all labels is "Title Name"-"Section Name" -- Spaces should be replaced by hyphens.
.. To reference a label that isn't associated with an reST object such as a title or figure, you must include the link and explicit title using the syntax :ref:`link text <label-name>`.
.. A warning will alert you of identical labels during the linkcheck process.


##################################################################
Introduction to DP0.3: the MPCORB and SSObject catalogs (beginner)
##################################################################

.. This section should provide a brief, top-level description of the page.

**Contact authors:** Greg Madejski and Melissa Graham

**Last verified to run:** July 6, 2023

**Targeted learning level:** Beginner


.. _DP0-3-Portal-1-Intro:

Introduction
============

This tutorial demonstrates how to access the simulated Data Preview 0.3 (DP0.3) data set in the Rubin Science Platform's Portal Aspect.

For the DP0.3 simulation, only moving objects were simulated, and only catalogs were created (there are no images). 
The DP0.3 simulation is entirely independent of and separate from the DP0.2 simulation.
DP0.3 is a hybrid catalog that contains both real and simulated Solar System objects 
(asteroids, near-earth objects, Trojans, trans-Neptunian objects, and even a simulated spaceship... but no comets, major planets, or the Moon). 
See :ref:`DP0-3-Data-Products-Introduction` for more information about how the hybrid catalog was created.

The DP0.3 catalog data contains four tables: ``MPCORB``, ``SSObject``, ``SSSource``, and ``DiaSource``.
Their contents are described in the :ref:`DP0-3-Data-Products-DPDD`.
In Rubin Operations, these tables would be constantly changing, updated every day with the results of the previous night's observations. 
However, for DP0.3, a static 10-year catalog has been simulated.

This tutorial focuses on the first two tables, ``MPCORB`` and ``SSObject``, and 
:ref:`Tutorials-Examples-DP0-3-Portal-2` will focus on ``SSSource`` and ``DiaSource``.


The ``MPCORB`` table
--------------------

During Rubin Operations, Solar System Processing will occur in the daytime, after a night of observing.
It will link together the difference-image detections of moving objects and report discoveries
to the `Minor Planet Center <https://minorplanetcenter.net>`_ (MPC),
as well as compute derived properties (magnitudes, phase-curve fits, coordinates in various systems).

The MPC will calculate the orbital parameters and these results will be passed back to Rubin, and stored
and made available to users as the ``MPCORB`` table 
(the other derived properties are stored in the other three tables explored below).
The DP0.3 ``MPCORB`` table is a simulation of what this data product will be like after 10 years of LSST.

The MPC contains all reported moving objects in the Solar System, and is not limited to those detected by LSST. 
Thus, the ``MPCORB`` table will have more rows than the ``SSObject`` table.

For more information about Rubin's plans for Solar System Processing, see Section 3.2.2 of the 
`Data Products Definitions Document <https://docushare.lsstcorp.org/docushare/dsweb/Get/LSE-163/LSE-163_DataProductsDefinitionDocumentDPDD.pdf>`_.
Note that there remain differences between Table 4 of the DPDD, which contain the anticipated schema 
for the moving object tables, and the DP0.3 table schemas.


The ``SSObject`` table
----------------------

During Rubin Operations, Prompt Processing will occur during the night, detecting sources in 
difference images (``DiaSources``, see Section 6) and associating them into static-sky transients
and variables (``DiaObjects``, not included in DP0.3).

The Solar System Processing which occurs in the daytime, after a night of observing,
links together the ``DiaSources`` for moving objects into ``SSObjects``.
Whereas the ``MPCORB`` table contains the orbital elements for these moving objects,
the ``SSObjects`` contains the Rubin-measured properties such as phase curve fits and absolute magnitudes.

Note that no artifacts or spurious difference-image sources have been injected into the DP0.3 catalogs.


TAP and ADQL
------------

The DP0.3 data sets are available via the Table Access Protocol (TAP) service via the Portal Aspect,
and can be queried via either the "UI Assisted" table interface, 
or via the ADQL (Astronomical Data Query Language) interface.
This tutorial will demonstrate both interfaces.
TAP provides standardized access to catalog data for discovery, search, and retrieval.
Full `documentation for TAP <http://www.ivoa.net/documents/TAP>`_ is provided by the International Virtual Observatory Alliance (IVOA).
ADQL is similar to SQL (Structured Query Langage).
The `documentation for ADQL <http://www.ivoa.net/documents/latest/ADQL.html>`_ includes more information about syntax and keywords.



.. _DP0-3-Portal-1-Step-1:

Step 1. Plot histograms of orbital elements in the ``MPCORB`` table
===================================================================

1.1. Log in to the Rubin Science Platform at `data.lsst.cloud <https://data.lsst.cloud>`_ and select the Portal Aspect.

.. figure:: /_static/portal_tut01_step01a.png
    :name: portal_tut01_step01a
    :alt: The default view of the Portal Aspect.

    Fig 1. The default view of the Portal Aspect.

1.2. To access the DP0.3 TAP Service (DP0.2 is the default), in the upper right corner next to "TAP Services" click "Show". 
A new option will appear at the top, called "Select TAP Service".
Click on where it says "Using LSST DP0.2 DC2", and select "LSST DP0.3 SSO" from the drop-down menu.
In the upper right corner next to "TAP Services" click "Hide".

1.3. The top of the page now displays "LSST DP0.3 SSO Tables".
The default "Table Collection (Schema)" will be "dp03_catalogs" and the default "Table" will be "dp03_catalogs.DiaSource".
Change the "Table" to be "dp03_catalogs.MPCORB". 
Notice how the area under "Enter Constraints" automatically un-checks the "Spatial Constraints" box, as the 
``MPCORB`` table does not contain sky coordinates, and how the table under "Output Column Selection and Constraints"
automatically updates to display the columns of the ``MPCORB`` table.

.. figure:: /_static/portal_tut01_step01b.png
    :name: portal_tut01_step01b
    :alt: The Portal interface when it is prepared to query the ``MPCORB`` table.

    Fig 2. The Portal interface is prepared to query the ``MPCORB`` table.





Step 2. Create a color-color diagram from the ``SSObject`` table 
================================================================



Step 3. Exercises for the learner 
=================================

