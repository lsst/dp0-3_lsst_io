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

##############################
DP0.3 Table Access and Queries
##############################

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

.. _Unpopulated-Columns:

Unpopulated columns
~~~~~~~~~~~~~~~~~~~

DP0.3 has been simulated and provided on a best-effort basis. There are at present a number of unpopulated columns in the DP0.3 tables, as listed here:

`DiaSource` : ``ra_dec_Cov``

`SSSource` : ``mpcUniqueId``, ``predictedDecErr``, ``predictedMagnitude``, ``predictedMagnitudeErr``, ``predictedRaDecCov``, ``predictedRaErr``, ``residualDec``, ``residualRa``

`SSObject` : ``maxExtendedness``, ``medianExtendedness``, ``minExtendedness``, ``MOID``, ``MOIDDeltaV``, ``MOIDEclipticLongitude``, ``MOIDTrueAnomaly``, ``u_Chi2``, ``u_G12``, ``u_G12Err``, ``u_H``, ``u_H_uG12_Cov``, ``u_HErr``, ``u_Ndata``, ``y_Chi2``, ``y_G12``, ``y_G12Err``, ``y_H``, ``y_H_yG12_Cov``, ``y_HErr``, ``y_Ndata``

`MPCORB` : ``arc``, ``arcEnd``, ``arcStart``, ``computer``, ``flags``, ``lastIncludedObservation``, ``mpcNumber``, ``n``, ``nobs``, ``nopp``, ``pertsLong``, ``pertsShort``, ``reference``, ``rms``, ``uncertaintyParameter``

These columns may be updated in the future to fill in their values.

Table sizes
~~~~~~~~~~~

Within a given simulated data set (1-year or 10-year), the ``DiaSource`` and ``SSSource`` tables are the same size, and each contains ~650 million rows:
one for every detection of every moving object in the ``SSObject`` table.

The ``SSObject`` table has ~2.0 million (~4.4 million) rows in the 1-year (10-year) DP0.3 dataset. The ``MPCORB`` table has ~14.5 million rows, regardless of whether the 1-year or 10-year data set is used.
The ``SSObject`` table is a subset of all objects in ``MPCORB`` which were detected by LSST in the simulation.

Column summary values
~~~~~~~~~~~~~~~~~~~~~

ADQL has functions that can return quantitative properties of the columns. 
The following ADQL functionality (at least) is available with the RSP TAP Service:

.. code-block:: SQL

    SELECT COUNT(numObs), MIN(numObs), MAX(numObs), AVG(numObs), SUM(numObs) 
    FROM dp03_catalogs_1yr.SSObject

Table joins
~~~~~~~~~~~

The ``DiaSource`` and ``SSSource`` tables are 1:1 and can be joined on the ``diaSourceId`` column.

All rows of the ``SSObject`` table have a match with ``MPCORB`` (but not vice versa),
and the two tables can be joined on the ``ssObjectId`` column.

The ``DiaSource`` and ``SSSource`` tables are N:1 with both the ``SSObject`` and ``MPCORB`` tables.
They *can* be joined on the ``ssObjectId`` column, but caution and testing should be used here.
The N:1 nature of these joins means that the data retrieved can contain columns of repeated values,
be larger than expected, and take a long time to execute.


Non-random subsets
~~~~~~~~~~~~~~~~~~

When exploring, if a small but not necessarily random subset of objects is all you need,
use the ``SELECT TOP`` and provide a small number, like 100.

.. code-block:: SQL

    SELECT TOP 100 * FROM dp03_catalogs_1yr.SSObject


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
for ~24,000 random ``SSObjects``, use:

.. code-block:: SQL

    SELECT g_H, r_H, i_H, z_H
    FROM dp03_catalogs_1yr.SSObject
    WHERE ssObjectId > 9000000000000000000

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
     - :math:`H_u` fit failure: the u-band absolute magnitude fit failed due to poor phase coverage or not enough data. Note however that u-band detections are not included in DP0.3.
   * - 4
     - :math:`H_g` fit failure: the g-band absolute magnitude fit failed due to poor phase coverage or not enough data.
   * - 8
     - :math:`H_r` fit failure: the r-band absolute magnitude fit failed due to poor phase coverage or not enough data.
   * - 16
     - :math:`H_i` fit failure: the i-band absolute magnitude fit failed due to poor phase coverage or not enough data.
   * - 32
     - :math:`H_z` fit failure: the z-band absolute magnitude fit failed due to poor phase coverage or not enough data.
   * - 64
     - :math:`H_y` fit failure: the y-band absolute magnitude fit failed due to poor phase coverage or not enough data. Note however that y-band detections are not included in DP0.3.
   * - 2048
     - Linking failure: the detections in ``diaSource`` were not successfully linked.

|

Note that the linking failure flag will only exist for simulated objects, 
as a real object that is not linked will not be in the ``SSObject`` table.

Example: an object whose absolute magnitude fit failed in the g and r bands will have a ``flags`` value of 12 (in binary, 1100).

Truth data
~~~~~~~~~~

Truth information is embedded within the DP0.3 ``DiaSource`` tables in the following four columns: ``raTrue`` (true RA i.e., without simulated measurement noise), ``decTrue`` (true Dec i.e., without simulated measurement noise), ``magTrueVband`` (true magnitude in the V band i.e., without simulated measurement noise), and ``nameTrue``.

Regarding ``nameTrue``: a value starting with 'S' or 'CEN' indicates that the source is a simulated ("fake") minor body. Otherwise, ``nameTrue`` provides the designation of the relevant real minor body.

The ``MPCORB`` tables contain injected rather than measured orbital parameters, so in this sense the MPCORB tables can be thought of as "truth tables".
