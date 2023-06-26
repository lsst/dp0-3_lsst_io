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

This site provides information about the Rubin Observatory's Data Preview 0.3 (DP0.3),
which only contains simulated Solar System objects.

.. Important::

    This page describes only the DP0.3 data products and tutorials. 
    Visit the `documentation for DP0.2 <https://dp0-2.lsst.io>`_ pages for:
     - getting started with DP0 (becoming a DP0 delegate),
     - creating and using your account in the Rubin Science Platform (RSP),
     - accessing Galactic and extragalactic simulated data products,
     - requesting help with issues and reporting bugs, and
     - collaborating with others and joining virtual seminars.

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

.. _Rubin-Observatory-Documentation-DP0-2-Quick-Links:

DP0.2 Quick Links
===================

- `How to get help <https://dp0-2.lsst.io/dp0-delegate-resources/index.html#getting-support>`_
- `Report bugs <https://dp0-2.lsst.io/dp0-delegate-resources/index.html#inform-and-improve-the-rsp>`_
- `How to access the RSP <https://dp0-2.lsst.io/data-access-analysis-tools/index.html#rubin-science-platform-rsp>`_
- `DPO virtual seminar schedule <https://dp0-2.lsst.io/dp0-delegate-resources/index.html#dp0-virtual-seminars>`_
- `The DESC DC2 DP0.2 static sky simulation <https://dp0-2.lsst.io/data-products-dp0-2/index.html#the-desc-dc2-data-set>`_

.. _Rubin-Observatory-Documentation-DP0-3-Data-Products:

DP0.3 data products
===================

The DP0.3 simulation was created by LSST Solar System Science Collaboration members,
and only contains catalog data products for Solar System objects.
For simulated Galactic and extragalactic data products, see the `documentation for DP0.2 <https://dp0-2.lsst.io>`_.

.. toctree::
    :maxdepth: 2
    :glob:

    data-products-dp0-3/index


.. _Rubin-Observatory-Documentation-DP0-3-Tutorials:

DP0.3 tutorials
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
