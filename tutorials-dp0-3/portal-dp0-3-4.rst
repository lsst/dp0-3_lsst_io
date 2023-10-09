.. Review the README on instructions to contribute.
.. Review the style guide to keep a consistent approach to the documentation.
.. Static objects, such as figures, should be stored in the _static directory. Review the _static/README on instructions to contribute.
.. Do not remove the comments that describe each section. They are included to provide guidance to contributors.
.. Do not remove other content provided in the templates, such as a section. Instead, comment out the content and include comments to explain the situation. For example:
	- If a section within the template is not needed, comment out the section title and label reference. Do not delete the expected section title, reference or related comments provided from the template.
    - If a file cannot include a title (surrounded by ampersands (#)), comment out the title from the template and include a comment explaining why this is implemented (in addition to applying the ``title`` directive).

.. This is the label that can be used for cross referencing this file.
.. Recommended title label format is "Directory Name"-"Title Name" -- Spaces should be replaced by hyphens.
.. _Tutorials-Examples-DP0-3-Portal-1:
.. Each section should include a label for cross referencing to a given area.
.. Recommended format for all labels is "Title Name"-"Section Name" -- Spaces should be replaced by hyphens.
.. To reference a label that isn't associated with an reST object such as a title or figure, you must include the link and explicit title using the syntax :ref:`link text <label-name>`.
.. A warning will alert you of identical labels during the linkcheck process.


##################################################################
04. Using user-supplied catalogs in in DP0.3 (beginner)
##################################################################

.. This section should provide a brief, top-level description of the page.

**Contact authors:** Christina Williams and Melissa Graham

**Last verified to run:** September 15, 2023

**Targeted learning level:** Intermediate


.. _DP0-3-Portal-4-Intro:

Introduction
============

This tutorial demonstrates a functionality of the Portal aspect for user-uploaded tables and their use in queries for DP0.3 (postgres only, not qserve, so not available for DP0.2 yet)


How to make weblinks: `LSST DDF webpage <https://www.lsst.org/scientists/survey-design/ddf>`_
and in Section 2.6 of the Survey Cadence Optimization Committee's Phase 2 Recommendations report 
(`PSTN-055 <https://pstn-055.lsst.io/>`_).

This tutorial assumes the successful completion of the beginner-level DP0.3 Portal tutorials,
and uses the Astronomy Data Query Language (ADQL), which is similar to SQL (Structured Query Language).
For more information about the DP0.3 catalogs, tables, and columns, see the :ref:`DP0-3-Data-Products-DPDD`.  


.. _DP0-3-Portal-4-Step-1:

Step 1. Upload a user-supplied table of coordinates for use in cone searches
=====================================

1.1. Log into the Rubin Science Platform at `data.lsst.cloud <https://data.lsst.cloud>`_ and select the Portal Aspect.
At upper right, next to "TAP Services" choose to "Show", and then select "LSST DP0.3 SSO" from the drop-down menu that appears at the top.

1.2 In the "Enter Constraints" box, under "spatial constraints" click on the multi-object button. A window will pop up to allow one to upload a text file containing ra and dec coordinates for sources of interest. The format of this catalog must be one of those listed (IPAC, CSV, TSV, VOTABLE, or FITS table format). For this example, we will use an ascii catalog with columns of RA and Dec in tab separated format (TSV). Other columns can also be present in the file. [do we attach the example file here?] Click the browse button to find the file on your machine and click the upload button.

1.3 After uploading, the window will show a list of the columns it found, named according to the header. Make sure that the ra and dec columns in your file are labeled "ra" and "dec" and are displayed in the list. Then click the "Load Table" button.

1.4 If the table loaded the ra and dec correctly, you should see the table filename displayed next to "Upload Table", and listed next to "position columns" should show "ra, dec (from the uploaded table)".

.. _DP0-3-Portal-4-Step-2:

Step 2. ADQL table join with user-uploaded list of SSObject IDs
======================================================


.. _DP0-3-Portal-4-Step-3:

Step 3. More advanced stuff
============================================





.. **FIND MORE INTERESTING THINGS TO DO AND EXPLORE WITH THIS TNO!**

.. **PLOT DISTANCES OVER TIME, OR MAYBE GET THE HELIO XYZ AND PLOT OUT ORBITAL ARCS, ETC.**

.. **CONSULT WITH ANDRES WHO IS WORKING ON A TNO NB**



.. _DP0-3-Portal-4-Step-6:

Step 6.  Exercises for the learner 
==================================

