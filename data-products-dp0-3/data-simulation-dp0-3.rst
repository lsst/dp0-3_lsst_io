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

The DP0.3 catalog is a simulated 10-year Rubin detection and object catalog of real and simulated solar system and interstellar objects using the 
baseline v3.0 cadence `(see page 44) <https://pstn-055.lsst.io/PSTN-055.pdf>`_. `ObjectsInField <https://github.com/eggls6/objectsInField>`_ was used to generate an ephemeris, from which source detection and measurement were simulated using 
`SurveySimPostProcessing <https://github.com/dirac-institute/survey_simulator_post_processing/tree/master>`_. The catalog includes hundreds of millions of detections of millions of simulated objects. 
Instructions for accessing the simulation can be found in the tutorial section.


.. _Data-Products-DP0-3-Data-Simulation-Real-Objects:

Real objects from the MPC
=========================

The DP0.3 simulation includes all objects from the May 1 2023 MPCORB except for the ~400 without listed absolute magnitudes. Of those objects, 
97% (1.2 million) are detected by Rubin in the 10-year simulated survey and appear in the DP0.3 catalog. 


.. _Data-Products-DP0-3-Data-Simulation-Fake-Objects:

Synthetic object populations
============================

We include 91% of the S3M catalog (see below for details) and 12,148 simulated interstellar objects in the simulation. 24% (3.2 million) 
of the S3M objects and 20% (2,429) of the ISOs are detected and appear in the catalog. 
Objects were simulated in two color classes: S and C, with colors and slope parameters as shown in table 1. [You can find object color class at X]. 


+-------+------+------+-----+-----+-----+-----+-----+
| Color | V-u  | V-g  | V-r | V-i | V-z | V-y | GS  |
+=======+======+======+=====+=====+=====+=====+=====+
|     c |-1.614|-0.302|0.172|0.291|0.298|0.303|0.15 |
+-------+------+------+-----+-----+-----+-----+-----+
|     s |-1.927|-0.395|0.255|0.455|0.401|0.406|0.15 |
+-------+------+------+-----+-----+-----+-----+-----+

[Veres https://arxiv.org/pdf/1706.09398.pdf]


.. _Data-Products-DP0-3-Data-Simulation-Combo:

Combining real and fake moving objects
======================================

(Get update from JK)To combine the real and synthetic populations while maintaining S3M’s well-chosen orbital distributions, 
we use the Hybrid Solar System Catalogue Creator (Hybridcat). Hybridcat removes the closest-matching synthetic object to each real object, 
leaving S3M’s orbital distribution minimally changed while including all known solar system objects. 
Hybridcat is available by pip install or on github.


.. _Data-Products-DP0-3-Data-Simulation-Truth-Data:

Truth data
==========

The full set of simulated objects, along with their orbital and physical parameters, can be found here: [link]. 
The true (no-scatter) astrometry is provided in the “AstRATrue” and “AstDecTrue” columns. 

