.. Review the README on instructions to contribute.
.. Review the style guide to keep a consistent approach to the documentation.
.. Static objects, such as figures, should be stored in the _static directory. Review the _static/README on instructions to contribute.
.. Do not remove the comments that describe each section. They are included to provide guidance to contributors.
.. Do not remove other content provided in the templates, such as a section. Instead, comment out the content and include comments to explain the situation. For example:
	- If a section within the template is not needed, comment out the section title and label reference. Do not delete the expected section title, reference or related comments provided from the template.
    - If a file cannot include a title (surrounded by ampersands (#)), comment out the title from the template and include a comment explaining why this is implemented (in addition to applying the ``title`` directive).

.. This is the label that can be used for cross referencing this file.
.. Recommended title label format is "Directory Name"-"Title Name" -- Spaces should be replaced by hyphens.
.. _Tutorials-Examples-DP0-3-Portal-2:
.. Each section should include a label for cross referencing to a given area.
.. Recommended format for all labels is "Title Name"-"Section Name" -- Spaces should be replaced by hyphens.
.. To reference a label that isn't associated with an reST object such as a title or figure, you must include the link and explicit title using the syntax :ref:`link text <label-name>`.
.. A warning will alert you of identical labels during the linkcheck process.


#################
02. Introduction to DP0.3: the ``SSSource`` and ``DiaSource`` tables (beginner)
#################

.. This section should provide a brief, top-level description of the page.

**Contact authors:** Greg Madejski and Melissa Graham

**Last verified to run:** Thu July 27 2023

**Targeted learning level:** beginner

**Introduction:**

This tutorial is a direct sequel to Portal tutorial 01: Introduction to DP0.3: the ``MPCORB`` and ``SSObject`` tables.
Those two tables contain derived parameters for individial simulated Solar System objects.

This tutorial focuses on the DP0.3 ``SSSource`` and ``DiaSource`` tables, which contain measured and derived
values for individial simulated Solar System objects on a per-observation basis.


The ``SSSource`` table
----------------------

The daytime Solar System Processing willalso report discoveries and data for moving objects
to the Minor Planet Center (MPC; minorplanetcenter.net), which computes the orbital elements
(eccentricity, inclination, etc.).
These orbital elements are then used to compute the instantaneous 3D sky location, distances, and velocities
at the time of each observation.
These results are stored in the ``SSSource`` table, which has a 1:1 relationship with the ``DiaSource`` table.


The ``DiaSource`` table
-----------------------

During Rubin Operations, Prompt Processing will occur during the night, detecting sources in 
difference images with signal-to-noise ratio > 5 (``DiaSources``, see Section 6).
DIA stands for difference image analysis.
After detection, the Prompt pipelines associate them into static-sky transients
and variables (``DiaObjects``, not included in DP0.3).
The Solar System Processing occurs in the daytime, after a night of observing,
links together the ``DiaSources`` for moving objects into ``SSObjects``.

With real data, the ``DiaSource`` catalog would contain sources due to artifacts (spurious sources), 
static-sky variables and transients, and moving objects.
However, the DP0.3 ``DiaSource`` catalog contains only moving objects.
Thus every DP0.3 ``DiaSource`` (every row of the table) has a ``ssObjectId``, an 
identifier that associates the source with the object in the ``SSObject`` table.

The DP0.3 ``DiaSource`` catalog contains the measured quantities (sky coordinates, apparent magnitude, error),
metadata (filter, time of observation),
and true values (true sky coordinates, true V-band apparent magnitude) for 
every difference-image detection.


.. _DP0-3-Portal-2-Step-1:

Step 1. Here
============

1.1. TBD

