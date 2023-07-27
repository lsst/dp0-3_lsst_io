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
DP0.3 Table Schema
###################

.. This section should provide a brief, top-level description of the page.


This schema page will eventually be replaced with `official schema from LSST Data Management <https://dm.lsst.org/sdm_schemas/browser/>`_.

.. _DP0-3-Table-Schema:

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
   * - u_H
     - float
     - Best fit absolute magnitude (u band)
   * - u_G12
     - float
     - Best fit G12 slope parameter (u band)
   * - u_HErr
     - float
     - Uncertainty of H (u band)
   * - u_G12Err
     - float
     - Uncertainty of G12 (u band)
   * - u_H_uG12_Cov
     - float
     - H-G12 covariance (u band)
   * - u_Chi2
     - float
     - Chi^2 statistic of the phase curve fit (u band)
   * - u_Ndata
     - int
     - The number of data points used to fit the phase curve (u band)
   * - g_H
     - float
     - Best fit absolute magnitude (g band)
   * - g_G12
     - float
     - Best fit G12 slope parameter (g band)
   * - g_HErr
     - float
     - Uncertainty of H (g band)
   * - g_G12Err
     - float
     - Uncertainty of G12 (g band)
   * - g_H_gG12_Cov
     - float
     - H-G12 covariance (g band)
   * - g_Chi2
     - float
     - Chi^2 statistic of the phase curve fit (g band)
   * - g_Ndata
     - int
     - The number of data points used to fit the phase curve (g band)
   * - r_H
     - float
     - Best fit absolute magnitude (r band)
   * - r_G12
     - float
     - Best fit G12 slope parameter (r band)
   * - r_HErr
     - float
     - Uncertainty of H (r band)
   * - r_G12Err
     - float
     - Uncertainty of G12 (r band)
   * - r_H_rG12_Cov
     - float
     - H-G12 covariance (r band)
   * - r_Chi2
     - float
     - Chi^2 statistic of the phase curve fit (r band)
   * - r_Ndata
     - int
     - The number of data points used to fit the phase curve (r band)
   * - i_H
     - float
     - Best fit absolute magnitude (i band)
   * - i_G12
     - float
     - Best fit G12 slope parameter (i band)
   * - i_HErr
     - float
     - Uncertainty of H (i band)
   * - i_G12Err
     - float
     - Uncertainty of G12 (i band)
   * - i_H_iG12_Cov
     - float
     - H-G12 covariance (i band)
   * - i_Chi2
     - float
     - Chi^2 statistic of the phase curve fit (i band)
   * - i_Ndata
     - int
     - The number of data points used to fit the phase curve (i band)
   * - z_H
     - float
     - Best fit absolute magnitude (z band)
   * - z_G12
     - float
     - Best fit G12 slope parameter (z band)
   * - z_HErr
     - float
     - Uncertainty of H (z band)
   * - z_G12Err
     - float
     - Uncertainty of G12 (z band)
   * - z_H_zG12_Cov
     - float
     - H-G12 covariance (z band)
   * - z_Chi2
     - float
     - Chi^2 statistic of the phase curve fit (z band)
   * - z_Ndata
     - int
     - The number of data points used to fit the phase curve (z band)
   * - y_H
     - float
     - Best fit absolute magnitude (y band)
   * - y_G12
     - float
     - Best fit G12 slope parameter (y band)
   * - y_HErr
     - float
     - Uncertainty of H (y band)
   * - y_G12Err
     - float
     - Uncertainty of G12 (y band)
   * - y_H_yG12_Cov
     - float
     - H-G12 covariance (y band)
   * - y_Chi2
     - float
     - Chi^2 statistic of the phase curve fit (y band)
   * - y_Ndata
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
   * - nameTrue
     - char
     - 
   * - ssObjectReassocTime
     - timestamp
     - Time when this diaSource was reassociated from diaObject to ssObject (if such reassociation happens, otherwise NULL).
   * - midPointMjdTai
     - double
     - Effective mid-exposure time for this diaSource.
   * - ra
     - double
     - RA-coordinate of the center of this diaSource.
   * - raErr
     - float
     - Uncertainty of ra.
   * - dec
     - double
     - Dec-coordinate of the center of this diaSource.
   * - decErr
     - float
     - Uncertainty of dec.
   * - ra_dec_Cov
     - float
     - Covariance between ra and dec.
   * - snr
     - float
     - The signal-to-noise ratio at which this source was detected in the difference image.
   * - band
     - char
     - 
   * - mag
     - float
     - Magnitude. This is a placeholder and should be replaced by flux.
   * - magErr
     - float
     - Magnitude error. This is a placeholder and should be replaced by flux error.
   * - magTrueVband
     - float
     - 
   * - raTrue
     - double
     - 
   * - decTrue
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
   * - predictedMagnitudeErr
     - float
     - Prediction uncertainty (1-sigma)
   * - residualRa
     - double
     - Residual R.A. vs. ephemeris
   * - residualDec
     - double
     - Residual Dec vs. ephemeris
   * - predictedRaErr
     - float
     - Predicted R.A. uncertainty
   * - predictedDecErr
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

