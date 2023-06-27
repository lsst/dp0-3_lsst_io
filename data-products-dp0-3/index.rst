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
Several of the future data products (e.g., specific table columns) that are listed in the DPDD are not available 
for DP0.

In the future, for real LSST survey data, the tables that DP0.3 is meant to emulate will be Prompt products (updated nightly). For DP0.3, it is as if you are seeing these Prompt products frozen at the end of the LSST 10-year survey.

The DP0.3 solar system simulation is completely distinct from the `DESC DC2 <https://arxiv.org/abs/2010.05926>`_ simulated data set used for DP0.2. You will not, for instance, be able to see a DP0.3 simulated asteroid detection in a DESC DC2 simulated image.


.. _DP0-3-Data-Products-DPDD-Schema-Browser:

Schema browser
--------------

*Provide a link to schema browser*

The RSP Portal aspect includes lists of column names and their descriptions for DP0.3 tables, and so can also be used as a schema browser.


.. _DP0-3-Data-Products-DPDD-Catalogs:

Catalogs
--------

Table Access Procotol (TAP) provides standardized access to the catalog data for discovery, search, and retrieval.
`Full documentation for TAP <https://www.ivoa.net/documents/TAP/>`_ is provided by the International Virtual Observatory Alliance (IVOA).
The TAP service uses a query language similar to SQL (Structured Query Langage) called ADQL (Astronomical Data Query Language).
The `documentation for ADQL <https://www.ivoa.net/documents/latest/ADQL.html>`_ includes more information about syntax and keywords.

Notice: Not all ADQL functionality is supported by the RSP for Data Preview 0.

.. _DP0-3-Data-Products-DPDD-ADQL Recipies:

ADQL Recipes
------------

`Astronomical Data Query Language <https://www.ivoa.net/documents/ADQL/20180112/PR-ADQL-2.1-20180112.html>`_ (ADQL) advice, recommendations, best practices, and recipes, can be found in the `DP0.2 documentation <https://dp0-2.lsst.io/data-access-analysis-tools/adql-recipes.html>`_.

