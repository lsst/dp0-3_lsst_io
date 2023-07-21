.. Review the README on instructions to contribute.
.. Review the style guide to keep a consistent approach to the documentation.
.. Static objects, such as figures, should be stored in the _static directory. Review the _static/README on instructions to contribute.
.. Do not remove the comments that describe each section. They are included to provide guidance to contributors.
.. Do not remove other content provided in the templates, such as a section. Instead, comment out the content and include comments to explain the situation. For example:
	- If a section within the template is not needed, comment out the section title and label reference. Do not delete the expected section title, reference or related comments provided from the template.
    - If a file cannot include a title (surrounded by ampersands (#)), comment out the title from the template and include a comment explaining why this is implemented (in addition to applying the ``title`` directive).

.. This is the label that can be used for cross referencing this file.
.. Recommended title label format is "Directory Name"-"Title Name" -- Spaces should be replaced by hyphens.
.. _Data-Products-DP0-3-Data-Simulation:
.. Each section should include a label for cross referencing to a given area.
.. Recommended format for all labels is "Title Name"-"Section Name" -- Spaces should be replaced by hyphens.
.. To reference a label that isn't associated with an reST object such as a title or figure, you must include the link and explicit title using the syntax :ref:`link text <label-name>`.
.. A warning will alert you of identical labels during the linkcheck process.


####################
The DP0.3 Simulation
####################

.. This section should provide a brief, top-level description of the page.

The DP0.3 data set is a catalog of real and simulated solar system and interstellar objects, hosted on the Rubin Science Platform (RSP). 
It simulates a 10-year Rubin survey using the LSST baseline v3.0 cadence (see page 44 of the `Survey Cadence Optimization Committee's Phase 2 Recommendations) <https://pstn-055.lsst.io/PSTN-055.pdf>`_ and covers
hundreds of millions of detections of millions of objects.  The baseline v3.0 cadence includes the North Ecliptic Spur and deep drilling fields, two of which are close to the equator
with low declination, so solar system objects will be observed. Revisit rates are driven by the need for solar system science with visits being 33 min apart.  
Also contained is a NEO microsurvey at sunset and sunrise.  The simulation has a population of Trans Neptunian Objects (TNO) (26k), Main Belt Asteroids (MBA) (4m), Interstellar objects (ISOs) (2k), 
Hildas and Trojean Asteroids (100k), and Near Earth Objects (NEO) (37k). 
`ObjectsInField <https://github.com/eggls6/objectsInField>`_ was used to generate an ephemeris from an object catalog and the Rubin cadence,  
from which source detection and measurement were simulated using 
`SurveySimPostProcessing <https://github.com/dirac-institute/survey_simulator_post_processing/tree/master>`_. 

The catalog accounts for astrometric scatter and photometric variations based on the objects's color class [one of two point populations], 
the exposure’s telescope filter, and the object’s phase angle. However, we do not include rotation curves or complex geometry. In other words,  
each DP0.3 object is a uniform, textured sphere in one of two color classes. Object's magnitude change is from the distance and phase angle. 
You can access the simulation by following the instructions in the tutorial section.

.. _Data-Products-DP0-3-Data-Simulation-Real-Objects:

Real objects from the MPC
=========================

The DP0.3 simulation contains all objects in the `Minor Planet Center Orbit (MPCORB) Database <https://www.minorplanetcenter.net/iau/MPCORB.html>`_
as of May 1 2023, except for the ~400 objects that have no absolute magnitudes. 
Out of these objects, Rubin detects 97% (1.2 million) of them in the simulated 10-year survey and includes them in the DP0.3 catalog.


.. _Data-Products-DP0-3-Data-Simulation-Fake-Objects:

Synthetic object populations
============================

We include 91% of the `Synthetic Solar System Model (S3M) catalog <https://iopscience.iop.org/article/10.1086/659833/pdf>`_ 
(see “Combining real and synthetic moving objects” for details) and 12,148 simulated interstellar objects. 
24% (3.2 million) of the S3M objects and 20% (2,429) of the ISOs are detected and appear in the catalog. 

Objects were simulated in two color classes: S and C (silicaceous and carbonaceous, see `Veres <https://arxiv.org/pdf/1706.09398.pdf>`_ for more details), 
with colors and slope parameters as shown in table 1. 



+-------+------+------+-----+-----+-----+-----+-----+
| Color | V-u  | V-g  | V-r | V-i | V-z | V-y | GS  |
+=======+======+======+=====+=====+=====+=====+=====+
|     c |-1.614|-0.302|0.172|0.291|0.298|0.303|0.15 |
+-------+------+------+-----+-----+-----+-----+-----+
|     s |-1.927|-0.395|0.255|0.455|0.401|0.406|0.15 |
+-------+------+------+-----+-----+-----+-----+-----+

Table 1 - dp0-3 color classes


.. _Data-Products-DP0-3-Data-Simulation-Combo:

Combining real and synthetic moving objects
===========================================

To combine the real and synthetic populations while maintaining S3M’s well-chosen orbital distributions, we use the Hybrid Solar System Catalogue Creator (Hybridcat). 
Hybridcat removes the closest-matching synthetic object to each real object, creating a population with all of MPCORB and most of S3M that closely matches S3M’s orbital distributions.


.. _Data-Products-DP0-3-Data-Simulation-Truth-Data:

Truth data
==========

**Truth Objects**: The full set of simulated objects, along with their orbital and physical parameters, can be found in the [truth table]. 
The true (no-scatter) astrometry is provided in the “AstRATrue” and “AstDecTrue” columns.

**UPDATE!** 

**_decTrue**: declination scatter-less astrometry for each detection

**_magTrue**: magnitude scatter-less astrometry for each detection

**_name**: name of object that generated the detection

**_raTrue**: right ascension scatter-less astrometry for each detection

**_V**: V magnitude scatter-less astrometry for each detection


