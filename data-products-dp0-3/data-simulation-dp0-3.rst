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

*TBD*.


.. _Data-Products-DP0-3-Data-Simulation-Real-Objects:

Real objects from the MPC
=========================

*The entire MPC as of May X 2023.*



.. _Data-Products-DP0-3-Data-Simulation-Fake-Objects:

Fake object populations
=======================

*Describe and characterize the simulated objects.*



.. _Data-Products-DP0-3-Data-Simulation-Combo:

Combining real and fake moving objects
======================================

*Describe the replacement process and property distribution preservations.*





.. _Data-Products-DP0-3-Data-Simulation-Truth-Data:

Truth data
==========

*Do users have truth data for comparisons?*

.. _Data-Products-DP0-3-Flags:

DP0.3 Flags
===========

As part of the absolute magnitude fitting process, let's define some flags for failure cases. These will be bitwise flags, so that the combinations of multiple flags are unique. 

- Success! `FLAG = 0` 
- Orbit fitting failure `FLAG = 1`: the diaSource detections do not fit a sensible orbit for a moving object (eg unusually high chi2/dof) 
- $H_u$ fit failure ``FLAG = 2`` : the u band absolute magnitude fit failed due to poor phase coverage or not enough data
- $H_g$ fit failure ``FLAG = 4`` : the g band absolute magnitude fit failed due to poor phase coverage or not enough data
- $H_r$ fit failure ``FLAG = 8`` : the r band absolute magnitude fit failed due to poor phase coverage or not enough data
- $H_i$ fit failure ``FLAG = 16`` : the i band absolute magnitude fit failed due to poor phase coverage or not enough data
- $H_z$ fit failure ``FLAG = 32`` : the z band absolute magnitude fit failed due to poor phase coverage or not enough data
- $H_y$ fit failure ``FLAG = 64`` : the y band absolute magnitude fit failed due to poor phase coverage or not enough data
- Linking failure: ``FLAG = 2048`` : the detections in diaSource were not successfully linked. Note that this will only exist for simulated objects, as a real object that is not linked will not be in `SSObject`! This is being simulated using difi (https://github.com/moeyensj/difi/tree/main)

Example: an object whose photometry failed in u and y band will have `FLAG = 66` (in binary, `1000010`). 

Note that ``bool(flag & reference)`` is ``True`` if ``reference`` is part of the ``flag``. So, for example, ``bool(66 & 64) = True`` and ``bool(66 & 4) = False``.
