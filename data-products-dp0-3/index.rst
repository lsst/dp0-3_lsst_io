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

*Mention how these DP0.3 tables would be Prompt (i.e., updated daily) in the future with real data but are otherwise for DP0.3 simulation are "frozen" at 10 years (any maybe we will have a 1 year too).*

*Mention how this simulation is completely distinct from DP0.2.*


.. _DP0-3-Data-Products-DPDD-Schema-Browser:

Schema browser
--------------

*Provide a link to schema browser, and mention how the Portal aspect serves as schema browser too.*



.. _DP0-3-Data-Products-DPDD-Catalogs:

Catalogs
--------

*Explain TAP endpoint.*

.. list-table:: SSObject DP0.3 table.
   :widths: 100 200 390
   :header-rows: 1

   * - column name
     - data type
     - description
   * - ssObjectId
     - long
     - Unique identifier.
   * - discoverySubmissionDate
     - double
     - The date the LSST first linked and submitted the discovery observations to the MPC. May be NULL if not an LSST discovery. The date format will follow general LSST conventions (MJD TAI, at the moment).
   * - firstObservationDate
     - double
     - The time of the first LSST observation of this object (could be precovered)
   * - arc
     - float
     - Arc of LSST observations
   * - numObs
     - int
     - Number of LSST observations of this object
   * - MOID
     - float
     - Minimum orbit intersection distance to Earth
   * - MOIDTrueAnomaly
     - float
     - True anomaly of the MOID point
   * - MOIDEclipticLongitude
     - float
     - Ecliptic longitude of the MOID point
   * - MOIDDeltaV
     - float
     - DeltaV at the MOID point
   * - uH
     - float
     - Best fit absolute magnitude (u band)
   * - uG12
     - float
     - Best fit G12 slope parameter (u band)
   * - uHErr
     - float
     - Uncertainty of H (u band)
   * - uG12Err
     - float
     - Uncertainty of G12 (u band)
   * - uH_uG12_Cov
     - float
     - H-G12 covariance (u band)
   * - uChi2
     - float
     - Chi^2 statistic of the phase curve fit (u band)
   * - uNdata
     - int
     - The number of data points used to fit the phase curve (u band)
   * - gH
     - float
     - Best fit absolute magnitude (g band)
   * - gG12
     - float
     - Best fit G12 slope parameter (g band)
   * - gHErr
     - float
     - Uncertainty of H (g band)
   * - gG12Err
     - float
     - Uncertainty of G12 (g band)
   * - gH_gG12_Cov
     - float
     - H-G12 covariance (g band)
   * - gChi2
     - float
     - Chi^2 statistic of the phase curve fit (g band)
   * - gNdata
     - int
     - The number of data points used to fit the phase curve (g band)
   * - rH
     - float
     - Best fit absolute magnitude (r band)
   * - rG12
     - float
     - Best fit G12 slope parameter (r band)
   * - rHErr
     - float
     - Uncertainty of H (r band)
   * - rG12Err
     - float
     - Uncertainty of G12 (r band)
   * - rH_rG12_Cov
     - float
     - H-G12 covariance (r band)
   * - rChi2
     - float
     - Chi^2 statistic of the phase curve fit (r band)
   * - rNdata
     - int
     - The number of data points used to fit the phase curve (r band)
   * - iH
     - float
     - Best fit absolute magnitude (i band)
   * - iG12
     - float
     - Best fit G12 slope parameter (i band)
   * - iHErr
     - float
     - Uncertainty of H (i band)
   * - iG12Err
     - float
     - Uncertainty of G12 (i band)
   * - iH_iG12_Cov
     - float
     - H-G12 covariance (i band)
   * - iChi2
     - float
     - Chi^2 statistic of the phase curve fit (i band)
   * - iNdata
     - int
     - The number of data points used to fit the phase curve (i band)
   * - zH
     - float
     - Best fit absolute magnitude (z band)
   * - zG12
     - float
     - Best fit G12 slope parameter (z band)
   * - zHErr
     - float
     - Uncertainty of H (z band)
   * - zG12Err
     - float
     - Uncertainty of G12 (z band)
   * - zH_zG12_Cov
     - float
     - H-G12 covariance (z band)
   * - zChi2
     - float
     - Chi^2 statistic of the phase curve fit (z band)
   * - zNdata
     - int
     - The number of data points used to fit the phase curve (z band)
   * - yH
     - float
     - Best fit absolute magnitude (y band)
   * - yG12
     - float
     - Best fit G12 slope parameter (y band)
   * - yHErr
     - float
     - Uncertainty of H (y band)
   * - yG12Err
     - float
     - Uncertainty of G12 (y band)
   * - yH_yG12_Cov
     - float
     - H-G12 covariance (y band)
   * - yChi2
     - float
     - Chi^2 statistic of the phase curve fit (y band)
   * - yNdata
     - int
     - The number of data points used to fit the phase curve (y band)
   * - maxExtendedness
     - float
     - maximum `extendedness` value from the DIASource
   * - minExtendedness
     - float
     - minimum `extendedness` value from the DIASource
   * - medianExtendedness
     - float
     - median `extendedness` value from the DIASource
   * - flags
     - long
     - Flags, bitwise OR tbd.

|
.. list-table:: DiaSource DP0.3 table.
   :widths: 100 200 390
   :header-rows: 1

   * - column name
     - data type
     - description
   * - diaSourceId
     - long
     - Unique id.
   * - ccdVisitId
     - long
     - Id of the ccdVisit where this diaSource was measured. Note that we are allowing a diaSource to belong to multiple amplifiers, but it may not span multiple ccds.
   * - diaObjectId
     - long
     - Id of the diaObject this source was associated with, if any. If not, it is set to NULL (each diaSource will be associated with either a diaObject or ssObject).
   * - ssObjectId
     - long
     - Id of the ssObject this source was associated with, if any. If not, it is set to NULL (each diaSource will be associated with either a diaObject or ssObject).
   * - _name
     - char
     - 
   * - ssObjectReassocTime
     - timestamp
     - Time when this diaSource was reassociated from diaObject to ssObject (if such reassociation happens, otherwise NULL).
   * - midPointTai
     - double
     - Effective mid-exposure time for this diaSource.
   * - ra
     - double
     - RA-coordinate of the center of this diaSource.
   * - raSigma
     - float
     - Uncertainty of ra.
   * - decl
     - double
     - Decl-coordinate of the center of this diaSource.
   * - declSigma
     - float
     - Uncertainty of decl.
   * - ra_decl_Cov
     - float
     - Covariance between ra and decl.
   * - snr
     - float
     - The signal-to-noise ratio at which this source was detected in the difference image.
   * - filter
     - char
     - 
   * - mag
     - float
     - Magnitude. This is a placeholder and should be replaced by flux.
   * - magSigma
     - float
     - Magnitude. This is a placeholder and should be replaced by flux.
   * - _V
     - float
     - 
   * - _magTrue
     - float
     - 
   * - _raTrue
     - double
     - 
   * - _decTrue
     - double
     - 

|
.. list-table:: SSSource DP0.3 table.
   :widths: 100 200 390
   :header-rows: 1

   * - column name
     - data type
     - description
   * - ssObjectId
     - long
     - Unique identifier of the object.
   * - diaSourceId
     - long
     - Unique identifier of the observation
   * - mpcUniqueId
     - long
     - MPC unique identifier of the observation
   * - eclipticLambda
     - double
     - Ecliptic longitude
   * - eclipticBeta
     - double
     - Ecliptic latitude
   * - galacticL
     - double
     - Galactic longitude
   * - galacticB
     - double
     - Galactic latitute
   * - phaseAngle
     - float
     - Phase angle
   * - heliocentricDist
     - float
     - Heliocentric distance
   * - topocentricDist
     - float
     - Topocentric distace
   * - predictedMagnitude
     - float
     - Predicted magnitude
   * - predictedMagnitudeSigma
     - float
     - Prediction uncertainty (1-sigma)
   * - residualRa
     - double
     - Residual R.A. vs. ephemeris
   * - residualDec
     - double
     - Residual Dec vs. ephemeris
   * - predictedRaSigma
     - float
     - Predicted R.A. uncertainty
   * - predictedDecSigma
     - float
     - Predicted Dec uncertainty
   * - predictedRaDecCov
     - float
     - Predicted R.A./Dec covariance
   * - heliocentricX
     - float
     - Cartesian heliocentric coordinates (at the emit time)
   * - heliocentricY
     - float
     - 
   * - heliocentricZ
     - float
     - 
   * - heliocentricVX
     - float
     - Cartesian heliocentric velocities (at the emit time)
   * - heliocentricVY
     - float
     - 
   * - heliocentricVZ
     - float
     - 
   * - topocentricX
     - float
     - Cartesian topocentric coordinates (at the emit time)
   * - topocentricY
     - float
     - 
   * - topocentricZ
     - float
     - 
   * - topocentricVX
     - float
     - Cartesian topocentric velocities (at the emit time)
   * - topocentricVY
     - float
     - 
   * - topocentricVZ
     - float
     - 

|
.. list-table:: MPCORB DP0.3 table.
   :widths: 100 200 390
   :header-rows: 1

   * - column name
     - data type
     - description
   * - mpcDesignation
     - char
     - MPCORB: Number or provisional designation (in packed form)
   * - mpcNumber
     - int
     - MPC number (if the asteroid has been numbered; NULL otherwise). Provided for convenience.
   * - ssObjectId
     - long
     - LSST unique identifier (if observed by LSST)
   * - mpcH
     - float
     - MPCORB: Absolute magnitude, H
   * - mpcG
     - float
     - MPCORB: Slope parameter, G
   * - epoch
     - double
     - MPCORB: Epoch (in MJD, .0 TT)
   * - tperi
     - double
     - MPCORB: MJD of pericentric passage
   * - peri
     - double
     - MPCORB: Argument of perihelion, J2000.0 (degrees)
   * - node
     - double
     - MPCORB: Longitude of the ascending node, J2000.0 (degrees)
   * - incl
     - double
     - MPCORB: Inclination to the ecliptic, J2000.0 (degrees)
   * - e
     - double
     - MPCORB: Orbital eccentricity
   * - n
     - double
     - MPCORB: Mean daily motion (degrees per day)
   * - q
     - double
     - MPCORB: Perihelion distance (AU)
   * - uncertaintyParameter
     - char
     - MPCORB: Uncertainty parameter, U
   * - reference
     - char
     - MPCORB: Reference
   * - nobs
     - int
     - MPCORB: Number of observations
   * - nopp
     - int
     - MPCORB: Number of oppositions
   * - arc
     - float
     - MPCORB: Arc (days), for single-opposition objects
   * - arcStart
     - timestamp
     - MPCORB: Year of first observation (for multi-opposition objects)
   * - arcEnd
     - timestamp
     - MPCORB: Year of last observation (for multi-opposition objects)
   * - rms
     - float
     - MPCORB: r.m.s residual (")
   * - pertsShort
     - char
     - MPCORB: Coarse indicator of perturbers (blank if unperturbed one-opposition object)
   * - pertsLong
     - char
     - MPCORB: Precise indicator of perturbers (blank if unperturbed one-opposition object)
   * - computer
     - char
     - MPCORB: Computer name
   * - flags
     - int
     - MPCORB: 4-hexdigit flags. See https://minorplanetcenter.net//iau/info/MPOrbitFormat.html for details
   * - fullDesignation
     - char
     - MPCORB: Readable designation
   * - lastIncludedObservation
     - float
     - MPCORB: Date of last observation included in orbit solution

|





.. _DP0-3-Data-Products-DPDD-ADQL Recipies:

ADQL Recipes
------------

`Astronomical Data Query Language <https://www.ivoa.net/documents/ADQL/20180112/PR-ADQL-2.1-20180112.html>`_ (ADQL) advice, recommendations, best practices, and recipes, can be found in the `DP0.2 documentation <https://dp0-2.lsst.io/data-access-analysis-tools/adql-recipes.html>`_.

