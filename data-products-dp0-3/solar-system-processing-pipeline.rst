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

##########################################
The Solar System Processing (SSP) Pipeline
##########################################

.. _DP0-3-Solar-System-Processing:

.. image:: LSST-Solar-System-Processing-Infographic.png

Solar System Processing
=======================

The goal of the Solar System Processing pipeline is to link (identify) previously unknown ``SSObjects``, 
given an additional night of observing, 
and report the discoveries to the `Minor Planet Center <https://minorplanetcenter.net>`_ (MPC), 
as well as to compute physical (e.g., absolute magnitudes) and other auxiliary properties 
(e.g., predicted apparent magnitudes and coordinates in various coordinate systems) 
for known Solar System objects and their LSST observations. The majority of the 
pipeline's processing occurs in daytime, after a night of observing. 
The pipeline will deliver 
Daily Data Products for Solar System objects in the form of four catalogs:  
``SSObject``, ``SSSource``, ``DIASource``, and ``MPCORB``, which are described in the 
:doc:`DP0.3 Data Products </data-products-dp0-3/index>` documentation and the 
`Data Products Definition Document <https://lse-163.lsst.io>`_ (DPDD). 
The Solar System Processing pipeline is illustrated in the infographic provided above.
For more information on the moving object tracklet linking and orbit fitting
algorithm, see the :doc:`HelioLinC3D Tracklet Linking and Orbit Fitting software package page </data-products-dp0-3/heliolinc3d-tracklet-linking-orbit-fitting>` page.

The Solar System Processing pipeline steps
------------------------------------------

During operations, the pipeline will consist of the following steps that will repeat every 24 hours:

During nightly observing:
   1. Known Solar System objects are associated with difference image detections in real-time. Alerts are produced within 60 seconds for all signal-to-noise ratio (SNR)>=5 ``DIASources``. The Alert Production pipeline attempts association of ``DIASources`` with known Solar System objects in real-time, and if a match is found then the alert includes the corresponding ``SSObject`` catalog.
During the day following nightly observing:
   2. All ``DIASources`` detected on the previous night that have not been matched at a high confidence level (SNR>=5) to a known Object, ``DIAObject``, ``SSObject``, or an artifact, are analyzed by the HelioLinC3D moving object linking algorithm for potential pairs that form tracklets (consisting of detections in three pairs of images for a given visit within 15 days) that are consistent with being on the same Keplerian orbit around the Sun. For more information on the moving object tracklet linking and orbit fitting
algorithm, see the :doc:`HelioLinC3D Tracklet Linking and Orbit Fitting software package page </data-products-dp0-3/heliolinc3d-tracklet-linking-orbit-fitting>` page.
   3. Measurements of known objects and new discoveries are submitted to the Minor Planet Center (MPC) using the standard data-exchange protocols (e.g., the ADES format). The measurements of all ``DIASources`` detected on the previous night that have been matched at a high level of confidence (SNR>=5) to a known ``SSObject`` are also submitted to the MPC.
During the day before the coming night’s observing:
   4. The most up-to-date ``MPCORB`` catalog is downloaded from the Minor Planet Center (MPC) and ingested into the Prompt Products database to obtain all previously submitted LSST discoveries and detections as well as discoveries and detections by other contemporaneous programs made during the past 24 hours.
   5. The Daily Data Product catalogs are updated to include the new Solar System object discoveries included in the ingested ``MPCORB`` catalog. In particular, the ``SSObject`` catalog is updated to include the new discoveries from the ingested ``MPCORB`` catalog, and the ``SSSource`` and ``DIASource`` catalogs are updated to point to the relevant ``SSObject`` records for the new discoveries. In addition, the physical properties of all known ``SSObjects`` (e.g., absolute magnitudes, predicted apparent magnitudes, extendedness estimates, and light curve characteristics), as defined by the orbit catalog, are recomputed. Updated data are entered into the relevant tables.
   6. The Solar System Daily Data Products (``MPCORB``, ``SSObject``, ``DIASource``, & ``SSSource`` tables) are released.
   7. Precovery linking is attempted for all ``SSObjects`` whose orbits were updated in the above process (or are new). Where successful, newly discovered observations are queued up for submission to the Minor Planet Center.

Acronym definitions:
   * MPC = Minor Planet Center
   * SS = Solar System
   * DIA = difference image analysis
   * SNR = signal-to-noise ratio

More information
================

   * `Data Products Datasheet <http://ls.st/doc-29545>`_
   * `Data Products Definition Document <https://lse-163.lsst.io/>`_ (DPDD)
   * :doc:`DP0.3 Data Products </data-products-dp0-3/index>` documentation
   * :doc:`HelioLinC3D Tracklet Linking and Orbit Fitting software package documentation
