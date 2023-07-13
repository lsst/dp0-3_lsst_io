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

#############################
DP0.3 Data Access and Queries
#############################

.. This section should provide a brief, top-level description of the page.

.. _DP0-3-Table-Access:

The best way to learn about accessing and querying the DP0.3 tables is to work through
the set of :doc:`DP0.3 tutorials </tutorials-dp0-3/index>`.

The DP0.3 tables are available via the Table Access Protocol (TAP) service in the Rubin Science Platform. 
TAP provides standardized access to the catalog data for discovery, search, and retrieval.
`Full documentation for TAP <https://www.ivoa.net/documents/TAP/>`_ is provided by the 
`International Virtual Observatory Alliance <https://ivoa.net>`_ (IVOA).

The TAP service uses a query language similar to SQL (Structured Query Language) called 
the `Astronomical Data Query Language <https://www.ivoa.net/documents/ADQL/20180112/PR-ADQL-2.1-20180112.html>`_ (ADQL).
The language is used by the IVOA to represent astronomy queries posted to Virtual Observatory (VO) services (such as TAP).
The `documentation for ADQL <https://www.ivoa.net/documents/latest/ADQL.html>`_ includes more information about syntax and keywords.

Note that not all ADQL functionality is supported by the RSP for Data Preview 0.
TAP and ADQL can be used in both the Notebook and Portal aspects.

.. Important::
    If a query takes longer than you expect, please submit a `GitHub Issue <https://github.com/rubin-dp0/Support>`__
    or post in the "Support - Data Preview 0" category of the `Rubin Community Forum <https://community.lsst.org/>`_.
    Rubin staff are happy to investigate and to help tweak queries for optimal execution.


Table sizes
~~~~~~~~~~~

The ``DiaSource`` and ``SSSource`` tables are the same size, and each contains over a billion rows:
one for every detection of every moving object in the ``SSObject`` table.

The ``SSObject`` table has 10.2 million rows and the ``MPCORB`` table has 14.6 million rows.
The ``SSObject`` table is a subset of all objects in ``MPCORB`` which were detected by LSST
in the simulation.


Column summary values
~~~~~~~~~~~~~~~~~~~~~

ADQL has functions that can return quantitative properties of the columns. 
The following ADQL functionality (at least) is available with the RSP TAP Service:

.. code-block:: SQL

    SELECT COUNT(numObs), MIN(numObs), MAX(numObs), AVG(numObs), SUM(numObs) 
    FROM dp03_catalogs.SSObject


Table joins
~~~~~~~~~~~

The ``DiaSource`` and ``SSSource`` tables are 1:1 and can be joined on ``diaSourceId`` column.

All rows of the ``SSObject`` table have a match with ``MPCORB`` (but not vice versa),
and the two tables can be joined on that ``ssObjectId`` column.

The ``DiaSource`` and ``SSSource`` tables are N:1 with both the ``SSObject`` and ``MPCORB`` tables.
They *can* be joined on the ``ssObjectId`` column, but caution and testing should be used here.
The N:1 nature of these joins means that the data retrieved can contain columns of repeated values,
be larger than expected, and take a long time to execute.


Non-random subsets
~~~~~~~~~~~~~~~~~~

When exploring, if a small but not necessarily random subset of objects is all you need,
use the ``SELECT TOP`` and provide a small number, like 100.

.. code-block:: SQL

    SELECT TOP 100 * FROM dp03_catalogs.SSObject


Random subsets
~~~~~~~~~~~~~~

Due to how the DP0.3 tables are stored, retrieving the first N objects that meet a
query's constraints might not be a truly random subset.

To retrieve a random subset, make use of the fact that the ``ssObjectId`` column is a 
randomly assigned 64-bit long unsigned integer. 
Since ADQL interprets a 64-bit long unsigned integer as a 63-bit *signed* integer, 
these range from about -922e16 to 922e16, but this will be fixed in the future so 
that all identifiers are positive numbers.
Until then, for example, to retrieve the *griz* absolute magnitudes (``H``) 
for ~1.2e5 random ``SSObjects``, use:

.. code-block:: SQL

    SELECT gH, rH, iH, zH
    FROM dp03_catalogs.SSObject
    WHERE ssObjectId > 9000000000000000000


Unpopulated rows and columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DP0.3 has been simulated and provided on a best-effort basis.
Some of the columns or rows may be unpopulated, or populated with ``NaN`` (not-a-number) values.


Flagged rows
~~~~~~~~~~~~

The process to derive absolute magnitudes (``H``) with phase curve fits produces failure flags.
These are bitwise flags, so that the combinations of multiple flags are unique.
They are stored in the ``flags`` column of the ``SSObject`` table.

.. list-table:: ``SSObject`` ``flags`` column.
   :widths: 50 540
   :header-rows: 1

   * - Value
     - Meaning
   * - 0
     - Success!
   * - 1
     - Orbit fitting failure: the ``diaSource`` detections do not fit a sensible orbit for a moving object (e.g., they have an unusually high chi-squared per degree of freedom).
   * - 2
     - $H_u$ fit failure: the u-band absolute magnitude fit failed due to poor phase coverage or not enough data.
   * - 4
     - $H_g$ fit failure: the g-band absolute magnitude fit failed due to poor phase coverage or not enough data.
   * - 8
     - $H_r$ fit failure: the r-band absolute magnitude fit failed due to poor phase coverage or not enough data.
   * - 16
     - $H_i$ fit failure: the i-band absolute magnitude fit failed due to poor phase coverage or not enough data.
   * - 32
     - $H_z$ fit failure: the z-band absolute magnitude fit failed due to poor phase coverage or not enough data.
   * - 64
     - $H_y$ fit failure: the y-band absolute magnitude fit failed due to poor phase coverage or not enough data.
   * - 2048
     - Linking failure: the detections in ``diaSource`` were not successfully linked.

|

Note that the linking failure flag will only exist for simulated objects, 
as a real object that is not linked will not be in the ``SSObject`` table.

Example: an object whose photometry failed in u and y band will have ``flags`` value of 66 (in binary, 1000010).
