.. Review the README on instructions to contribute.
.. Review the style guide to keep a consistent approach to the documentation.
.. Static objects, such as figures, should be stored in the _static directory. Review the _static/README on instructions to contribute.
.. Do not remove the comments that describe each section. They are included to provide guidance to contributors.
.. Do not remove other content provided in the templates, such as a section. Instead, comment out the content and include comments to explain the situation. For example:
	- If a section within the template is not needed, comment out the section title and label reference. Do not delete the expected section title, reference or related comments provided from the template.
    - If a file cannot include a title (surrounded by ampersands (#)), comment out the title from the template and include a comment explaining why this is implemented (in addition to applying the ``title`` directive).

.. This is the label that can be used for cross referencing this file.
.. Recommended title label format is "Directory Name"-"Title Name" -- Spaces should be replaced by hyphens.
.. _Tutorials-DP0-3-Tutorials:
.. Each section should include a label for cross referencing to a given area.
.. Recommended format for all labels is "Title Name"-"Section Name" -- Spaces should be replaced by hyphens.
.. To reference a label that isn't associated with an reST object such as a title or figure, you must include the link and explicit title using the syntax :ref:`link text <label-name>`.
.. A warning will alert you of identical labels during the linkcheck process.

###############
DP0.3 Tutorials
###############

.. This section should provide a brief, top-level description of the page.

These tutorials are for DP0 delegates using the Rubin Science Platform (RSP) deployed at the Interim Data Facility (IDF; the Google Cloud).

Before following these tutorials, delegates should follow the `getting started checklist in the documentation for DP0.2 <https://dp0-2.lsst.io/dp0-delegate-resources/index.html#getting-started-with-dp0-checklist>`_ and:

| 1. have gotten their :ref:`Delegate-Homepage-RSP-Accounts` and be able to log in at `data.lsst.cloud <https://data.lsst.cloud/>`_,
| 2. be familiar with this list of :doc:`/data-access-analysis-tools/rsp-warnings`,
| 3. have reviewed the basic introductions to the RSP's :ref:`Tools-RSP-Portal` or :ref:`Tools-RSP-Notebook`, and
| 4. know their options for :ref:`Delegate-Homepage-Getting-Support`.


All RSP tutorials are created by Rubin staff and adhere to
the set of guidelines and best practices described in `RTN-045 <https://rtn-045.lsst.io/>`_,
unless otherwise noted (e.g., the `contributed tutorials <https://dp0-2.lsst.io/tutorials-examples/index.html#contributed-tutorials>`_).

`Suggest a new tutorial topic <https://community.lsst.org/t/suggest-a-new-dp0-2-tutorial/6556>`_.


.. _DP0-3-Tutorials-Whats-New:

Major Changes Log
=================

.. toctree::
    :titlesonly:
    :glob:

    major-updates-log-dp0-3



.. _DP0-3-Tutorials-Portal:

Portal tutorials
================

Step-by-step demonstrations of how to use the DP0.3 data products in the Portal Aspect.

.. toctree::
    :titlesonly:
    :glob:

    portal-dp0-3-1
    portal-dp0-3-2
    portal-dp0-3-3



.. _DP0-3-Tutorials-Notebooks:

Notebook tutorials
==================

All Jupyter Notebook tutorials are kept in the `tutorial-notebooks repository <https://github.com/rubin-dp0/tutorial-notebooks>`_
of the ``rubin-dp0`` GitHub Organization.

The contents of the ``prod`` branch of that repository are made available (and automatically updated) in the folder ``notebooks/tutorial-notebooks``
which appears in all users' home directories.

**List of Notebook tutorials:**
See the repository's `README file <https://github.com/rubin-dp0/tutorial-notebooks/blob/main/README.md>`_ for the most up-to-date
list of available tutorials with descriptions.



.. _DP0-3-Tutorials-Contributed:

Contributed tutorials
=====================

**Where do contributed tutorials go?** 
In the shared GitHub repository `delegate-contributions-dp03 <https://github.com/rubin-dp0/delegate-contributions-dp03>`_.
Contributions are stored in sub-directories by topic; view the readme files in each sub-directory for more information 
about the contents and who contributed them.

**Who can contribute a tutorial?**
Everyone is welcome to contribute tutorials or science demonstrations to this repo.
All are welcome to drop in to a `Stack Club <https://dp0-2.lsst.io/dp0-delegate-resources/index.html#stack-club>`_ session 
to workshop a tutorial topic or get assistance.

**How are contributions made?**
The `README <https://github.com/rubin-dp0/delegate-contributions-dp03/blob/main/README.md>`_ file for this repo 
contains instructions and best practices for contributions.
Rubin staff do not apply any quality control reviews to the contributed content in this repo.

**What topics can be contributed?**
Any and all topics are welcome, so long as they can be covered by the DP0.3 data set. 
Here is a short list of potential science topics that DP0.3 could be useful for.

 * analysis of the comet population
 * identifying interstellar objects
 * searching for alien spacecraft (no really!)
 * identifying sub-populations of main-belt asteroids or TNOs
 * correlating astrometric/photometric uncertainties with the accuracy of derived properties
