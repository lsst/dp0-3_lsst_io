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
However, for DP0.3 these data products are static, and created as they would be at the end of the LSST 10-year survey.

The DP0.3 solar system simulation is completely distinct from the `DESC DC2 <https://arxiv.org/abs/2010.05926>`_ simulated data set used for DP0.2.
The two simulations use different observing strategy simulations, different object truth simulations, and cover different areas.
There is no way to, for instance, see a DP0.3 simulated asteroid detection in a DESC DC2 simulated image.

.. _DP0-3-Data-Products-DPDD-Schema-Browser:

Schema browser
--------------

A  :doc:`schema browser </data-products-dp0-3/schema>` for the four DP0.3 solar system tables (DiaObject, SSSource, SSObject, MPCORB) is available.

The `RSP Portal aspect <https://data.lsst.cloud>`_ includes lists of column names and their descriptions for DP0.3 tables, and so can also be used as a schema browser.

.. _DP0-3-Data-Products-DPDD-Catalogs:

Catalogs
--------

_MLG: placeholder for the descriptions similar to intro NB_

.. list-table:: Catalog data available for DP0.2.
   :widths: 100 100 390
   :header-rows: 1

   * - TAP Name
     - table name
     - description
   * - DIASource
     - DIASource
     - Astrometric and photometric measurements for solar system objects detected in difference images (20 columns).
   * - SSSource
     - SSSource
     - Single-epoch solar system source information corresponding to a specific difference image detection (29 columns).
   * - SSObject
     - SSObject
     - Table of linked solar system objects (groupings of difference image detections; 55 columns).
   * - MPCORB
     - MPCORB
     - MPC-style information for linked solar system objects (27 columns).

|

.. _DP0-3-Data-Products-DPDD-ADQL Recipies:

Accessing and Querying the DP0.3 Tables
---------------------------------------

_MLG: placeholder for the details_

Table Access Procotol (TAP) provides standardized access to the catalog data for discovery, search, and retrieval.
`Full documentation for TAP <https://www.ivoa.net/documents/TAP/>`_ is provided by the International Virtual Observatory Alliance (IVOA).
The TAP service uses a query language similar to SQL (Structured Query Langage) called ADQL (Astronomical Data Query Language).
The `documentation for ADQL <https://www.ivoa.net/documents/latest/ADQL.html>`_ includes more information about syntax and keywords.

Notice: Not all ADQL functionality is supported by the RSP for Data Preview 0.

`Astronomical Data Query Language <https://www.ivoa.net/documents/ADQL/20180112/PR-ADQL-2.1-20180112.html>`_ (ADQL) advice, recommendations, best practices, and recipes:

ADQL is the `Astronomical Data Query Language <https://www.ivoa.net/documents/ADQL/>`_.
The language is used by the `IVOA <https://ivoa.net>`_ to represent astronomy queries posted to Virtual Observatory (VO) services, such as the Rubin LSST Table Access Protocol (TAP) service.
ADQL is based on the Structured Query Language (SQL).

ADQL can be used in both the Notebook and Portal aspects.

Learn more about the `TAP-accessible DP0.3 catalogs <https://dp0-2.lsst.io/data-products-dp0-2/index.html#catalogs>`__ which are used in the examples below.

.. Important::
    If a query takes longer than you expect, please submit a `GitHub Issue <https://github.com/rubin-dp0/Support>`__
    or post in the "DP0 RSP Service Issues" category of the Rubin Community Forum.
    Rubin staff are happy to investigate and to help tweak queries for optimal execution.


.. _Adql-Recipes-General-Advice:

General Advice
==============

**Use spatial constraints on RA and Dec.**
It is recommended to always start with spatial constraints for a small radius and then expand the search area.
Qserv stores catalog data sharded by coordinate (RA, Dec).
ADQL query statements that include constraints by coordinate do not requre a whole-catalog search,
and are typically faster (and can be *much* faster) than ADQL query statements which only include constraints for other columns.

**Use ``dectect_isPrimary`` = True.**
It is recommended to include ``detect_isPrimary = True`` in queries for the ``Object``, ``Source``, and ``ForcedSource`` catalogs.
This parameter is ``True`` if a source has no children, is in the inner region of a coadd patch, is in the inner region of a coadd tract, and is not detected in a pseudo-filter.
Including this constraint will remove any duplicates:
it will not include the parent *and* its deblended children (only deblended children), and
it will not include detections in the overlapping patch edge regions (only the non-overlapping inner regions).

Additional external resources for learning about SQL, ADQL, and Qserv include:
 - `W3 School's SQL Tutorial <https://www.w3schools.com/sql/default.asp>`__
 - `IVOA's ADQL Documentation <https://www.ivoa.net/documents/ADQL/20180112/PR-ADQL-2.1-20180112.html>`__


.. _Adql-Recipes-Explore-Tables:

Exploring tables
================

When learning about the contents of a table, it can be handy to simply retrieve all columns for "a bunch" (hundreds to thousands) of rows
and take a look at the results.
For this use-case, it is recommended to use the ``SELECT TOP`` statement, like in the example below that just retrieves the first 100 rows of the ``Object`` table.

.. code-block:: SQL

    SELECT TOP 100 * FROM dp03_catalogs.SSObject



.. _Adql-Recipes-Cone-Search:

Cone Search
===========

Retrieve the ``coord_dec`` and ``coord_ra`` columns from the ``Object`` table for objects within a 0.05 degree radius of RA = 62, Dec = -37.

.. code-block:: SQL

   SELECT * 
   FROM dp03_catalogs.DiaSource 
   WHERE CONTAINS(POINT('ICRS', ra, decl),CIRCLE('ICRS', 100, -10, 0.027777777777777776))=1


.. _Adql-Recipes-FluxToMags:

Convert fluxes to magnitudes
============================

As above, retrieve the ``coord_dec`` and ``coord_ra`` columns from the ``Object`` table for objects within a 0.05 degree radius of RA = 62, Dec = -37,
and also retrieve the g-band AB magnitude and magnitude error.
The ``scisql`` functions used below can be applied to any flux column.

.. code-block:: SQL

   SELECT coord_dec, coord_ra, 
   scisql_nanojanskyToAbMag(g_calibFlux) AS g_calibMag, 
   scisql_nanojanskyToAbMagSigma(g_calibFlux, g_calibFluxErr) as g_calibMagErr 
   FROM dp02_dc2_catalogs.Object 
   WHERE CONTAINS(POINT('ICRS', coord_ra, coord_dec), 
   CIRCLE('ICRS', 62, -37, 0.05)) = 1


.. _Adql-Recipes-Table-Joins:

Table joins
===========

Below, the Source and CcdVisit table are joined in order to obtain the date and seeing from the CcdVisit table.
Any two tables can be joined so long as they have an index in common.

This query also renames (nicknames) columns and tables using ``AS``,
and applies a spatial constraint, a temporal constraint (using ``obsStartMJD``), 
and constraints on the band, extendedness, and flux value.

Additional external resources on SQL table joins:
 - `W2 School's SQL tutorial: joins <https://www.w3schools.com/sql/sql_join.asp>`__
 - `The Data School: SQL Joins Explained Visually <https://dataschool.com/how-to-teach-people-sql/sql-join-types-explained-visually/>`__

.. code-block:: SQL

   SELECT src.ccdVisitId AS src_ccdVisitId, 
   src.extendedness AS src_extendedness, 
   src.band AS src_band, 
   scisql_nanojanskyToAbMag(src.psfFlux) AS src_psfAbMag, 
   cv.obsStartMJD AS cv_obsStartMJD, 
   cv.seeing AS cv_seeing 
   FROM dp02_dc2_catalogs.Source AS src 
   JOIN dp02_dc2_catalogs.CcdVisit AS cv 
   ON src.ccdVisitId = cv.ccdVisitId 
   WHERE CONTAINS(POINT('ICRS', coord_ra, coord_dec), 
   CIRCLE('ICRS', 62.0, -37, 1)) = 1 
   AND src.band = 'i' 
   AND src.extendedness = 0 
   AND src.psfFlux > 10000 
   AND cv.obsStartMJD > 60925 
   AND cv.obsStartMJD < 60955

.. _Adql-Recipes-ObjectIds:

Individual objects
==================

**Searches for individual objects can take a surprisingly long time.**
Recall that the TAP tables are sharded by RA,Dec, and when RA,Dec constraints are not provided (as in the example below),
the entire table must be searched, and this can take a long time despite the small amount of data returned.

In the above example, a single object was desired, and a statement like ``WHERE objectId=1486`` was used.
However, if more than a few single objects are desired and their ``objectId`` are known, a query built up of, e.g.,
``OR objectId=1487 OR objectId=1488 OR objectId=1489`` and so on would work, but there's a better way: ``WHERE objectId IN ()``.

Below, a list of just 12 ``objectId`` is put in a string called ``my_list``, formatted as a python tuple (with round brackets). 
This list could contain many more objects and be generated programmatically (e.g., from a different query, or by user analysis),
and then be included in the ADQL query statement and the TAP service would treat it the same way.
The number of results returned will equal the length of the list of ``objectId`` passed.

For this example, the 12 were selected to be bright stars with similar *g-r* and *i-z* colors,
so the query retrieves the *g*, *r*, *i*, and *z* band fluxes, but users should modify this to their own needs.

.. code-block:: python

    from lsst.rsp import get_tap_service, retrieve_query
    service = get_tap_service()
    
    my_list = "(1249537790362809267, 1252528461990360512, 1248772530269893180, "\
              "1251728017525343554, 1251710425339299404, 1250030371572068167, "\
              "1253443255664678173, 1251807182362538413, 1252607626827575504, "\
              "1249784080967440401, 1253065023664713612, 1325835101237446771)"
    
    query = "SELECT objectId, g_calibFlux, r_calibFlux, i_calibFlux, z_calibFlux "\
            "FROM dp02_dc2_catalogs.Object "\
            "WHERE objectId IN "+my_list
	    
    results = service.search(query)
    results.to_table()

