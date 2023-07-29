.. Review the README on instructions to contribute.
.. Review the style guide to keep a consistent approach to the documentation.
.. Static objects, such as figures, should be stored in the _static directory. Review the _static/README on instructions to contribute.
.. Do not remove the comments that describe each section. They are included to provide guidance to contributors.
.. Do not remove other content provided in the templates, such as a section. Instead, comment out the content and include comments to explain the situation. For example:
	- If a section within the template is not needed, comment out the section title and label reference. Do not delete the expected section title, reference or related comments provided from the template.
    - If a file cannot include a title (surrounded by ampersands (#)), comment out the title from the template and include a comment explaining why this is implemented (in addition to applying the ``title`` directive).

.. This is the label that can be used for cross referencing this file.
.. Recommended title label format is "Directory Name"-"Title Name" -- Spaces should be replaced by hyphens.
.. _Data-Products-DP0-3-Data-Products:
.. Each section should include a label for cross referencing to a given area.
.. Recommended format for all labels is "Title Name"-"Section Name" -- Spaces should be replaced by hyphens.
.. To reference a label that isn't associated with an reST object such as a title or figure, you must include the link and explicit title using the syntax :ref:`link text <label-name>`.
.. A warning will alert you of identical labels during the linkcheck process.

###################
DP0.3 Data Products
###################

.. This section should provide a brief, top-level description of the page.


.. _DP0-3-Data-Products-Introduction:


The SSSC Simulated Data Set
===========================

The LSST Solar System Science Collaboration (SSSC) created the simulated data set which
is being used for DP0.3.

.. toctree::
    :maxdepth: 2
    :glob:

    data-simulation-dp0-3



.. _DP0-3-Data-Products-DPDD:

DP0.3 Data Products Definition Document (DPDD)
==============================================

Future data previews and Operations-era LSST data releases will produce images and catalogs that more closely 
resemble the plan laid out in the `Data Products Definition Document <https://ls.st/dpdd/>`_ (DPDD).
Several of the future data products that are listed in the DPDD are not available for DP0
(e.g., columns in the planned moving object tables in Section 3.3.3 of the DPDD).

In the future, for real LSST survey data, the tables that DP0.3 is meant to emulate will be Prompt products 
that are updated nightly (``DiaSource`` and ``SSObject``) 
or products of the moving object pipeline that are updated daily (``SSSource`` and ``MPCORB``).
However, for DP0.3 these data products are static, created as they would be after 1 year of LSST, and at the end of the 10-year survey.

The DP0.3 solar system simulation is completely distinct from the `DESC DC2 <https://arxiv.org/abs/2010.05926>`_ simulated data set used for DP0.2.
The two simulations use different observing strategy simulations, different object truth simulations, and cover different areas.
There is no way to, for instance, see a DP0.3 simulated asteroid detection in a DESC DC2 simulated image.

Due to time constraints, DP0.3 does not contain u- or y-band detections. This decision was made in part because the majority of objects will have very low signal-to-noise ratio in u and y, and object discoverability is driven by the gri bands. Also, :doc:`a subset of DP0.3 columns </data-products-dp0-3/table-access-and-queries>` are unpopulated at present.


.. _DP0-3-Data-Products-DPDD-Schema-Browser:

Schema browser
--------------

A  :doc:`schema browser </data-products-dp0-3/schema>` for the four DP0.3 solar system tables (``DiaSource``, ``SSSource``, ``SSObject``, ``MPCORB``) is available.

The `RSP Portal aspect <https://data.lsst.cloud>`_ includes lists of column names and their descriptions for DP0.3 tables, and so can also be used as a schema browser.

.. _DP0-3-Data-Products-DPDD-Catalogs:

Catalogs
--------

.. list-table:: Catalog data available for DP0.3.
   :widths: 100 390
   :header-rows: 1

   * - TAP Name
     - description
   * - DiaSource
     - Astrometric and photometric measurements for solar system objects detected in difference images (19 columns).
   * - SSSource
     - Single-epoch solar system source information corresponding to a specific difference image detection (29 columns).
   * - SSObject
     - Table of linked solar system objects (groupings of difference image detections; 55 columns).
   * - MPCORB
     - MPC-style information for injected solar system objects (27 columns).

|

`DiaSource`:
This table is the first to be generated in real time, as it is updated during the night by the Prompt Processing pipeline.
*In the future*, with real data, the ``DiaSource`` table will contain measurements for *all* sources detected with a 
signal-to-noise ratio of at least 5 in a difference image.
*For DP0.3*, the ``DiaSource`` table only contains the simulated detections of moving objects (no static-sky time-domain
objects, and no artifacts).

`SSSource`:
This table contains the 2-d (sky) coordinates and 3-d distances and velocities for every ``SSObject`` at the time of every LSST
observation of that ``SSObject``. 
The ``SSSource`` and ``DiaSource`` tables are 1:1, as they each contain data per observation, 
whereas ``SSObject`` and ``MPCORB`` contains data per object.

`SSObject`:
During Rubin Operations, Prompt Processing will occur during the night, detecting sources in difference images 
(``DiaSources``) and associating them into static-sky transients and variables (``DiaObjects``, not included in DP0.3).
The Solar System Processing which occurs in the daytime links together the ``DiaSources`` 
for moving objects into ``SSObjects``, and measures properties such as phase curve fits and absolute magnitudes,
which are stored in the ``SSObject`` table.

`MPCORB`:
During Rubin Operations, Solar System Processing will occur in the daytime, after a night of observing.
It will link together the difference-image detections of moving objects and report discoveries to the Minor Planet Center (MPC), 
as well as compute derived properties (magnitudes, phase curve fits, coordinates in various systems).
The MPC will calculate the orbital parameters and these results will be passed back to Rubin, and stored and made available to 
users as the MPCORB table (the other derived properties are stored in the other three tables described above).

Note that the 1-year and 10-year versions of each DP0.3 table have the same :doc:`schema </data-products-dp0-3/schema>`.

.. _DP0-3-Data-Products-DPDD-Access:

Table access and queries
------------------------

For information and advice about accessing and querying the DP0.3 tables, please see the :doc:`table access and queries page </data-products-dp0-3/table-access-and-queries>`.

.. toctree::
    :maxdepth: 2
    :glob:

    table-access-and-queries
