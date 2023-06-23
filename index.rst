.. Review the README on instructions to contribute.
.. Review the style guide to keep a consistent approach to the documentation.
.. Static objects, such as figures, should be stored in the _static directory. Review the _static/README on instructions to contribute.
.. Do not remove the comments that describe each section. They are included to provide guidance to contributors.
.. Do not remove other content provided in the templates, such as a section. Instead, comment out the content and include comments to explain the situation. For example:
	- If a section within the template is not needed, comment out the section title and label reference. Do not delete the expected section title, reference or related comments provided from the template.
    - If a file cannot include a title (surrounded by ampersands (#)), comment out the title from the template and include a comment explaining why this is implemented (in addition to applying the ``title`` directive).

.. This is the label that can be used for cross referencing this file.
.. Recommended title label format is "Directory Name"-"Title Name" -- Spaces should be replaced by hyphens.
.. _Rubin-Observatory-Documentation-DP0-3:
.. Each section should include a label for cross referencing to a given area.
.. Recommended format for all labels is "Title Name"-"Section Name" -- Spaces should be replaced by hyphens.
.. To reference a label that isn't associated with an reST object such as a title or figure, you must include the link and explicit title using the syntax :ref:`link text <label-name>`.
.. A warning will alert you of identical labels during the linkcheck process.

####################################################################
Vera C. Rubin Observatory Documentation for Data Preview 0.3 (DP0.3)
####################################################################

.. This section should provide a brief, top-level description of the page.
.. Important::

    This documentation area is under heavy development and only in the very early stages of design.
    It should not be used nor consulted for a place of information at this time.

This site provides information about the Rubin Observatory's Data Preview 0.3 (DP0.3).

.. Important::

    Documentation for Data Preview 0.2 (DP0.2) and DP0.3 shall be used concurrently.
	See `Documentation for DP0.2 <https://dp0-2.lsst.io>`_ for:
	  - getting started with DP0 (becoming a DP0 delegate),
	  - account creation for the Rubin Science Platform (RSP),
	  - getting help with issues and report bugs, and
	  - collaborating with others and joining virtual seminars.

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    *


.. _Rubin-Observatory-Documentation-DP0-3-Data-Products:

DP0.3 data products
===================

The data set used for Phase 3 of DP0 (DP0.3) contains Solar System catalog data products only.
It was created by LSST Solar System Science Collaboration members.
For simulated extragalactic data products, see the `Documentation for DP0.2 <https://dp0-2.lsst.io>`_ instead.

.. toctree::
    :maxdepth: 2
    :glob:

    data-products-dp0-3/index


.. _Rubin-Observatory-Documentation-DP0-3-Tutorials:

DP0.3 Tutorials
===============

Tutorials include hands-on executable tutorials and demonstrations based on science use-cases to 
help scientists and students learn to use the DP0.3 data products and the Rubin Science Platform.

.. toctree::
    :maxdepth: 2
    :glob:

    tutorials-dp0-3/index



.. _Rubin-Observatory-Documentation-DP0-3-Documentation-Project-Information:

Documentation project information
=================================

Information on this documentation project and how to contribute to it.

.. toctree::
    :maxdepth: 2
    :glob:
    :titlesonly:

    project/index
