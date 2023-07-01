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


##############################################################
01. Introduction to the DP0.3 in the RST Portal (Beginner)
##############################################################

.. This section should provide a brief, top-level description of the page.

**Contact authors:** Greg Madejski and Melissa Graham

**Last verified to run:** June 26, 2023

**Targeted learning level:** Beginner

**Introduction:** This tutorial provides an introduction to the content of the sumulated Rubin Observatory Solar System data accessible via the Rubin Data Preview DP0.3.  

The tutorial consists of several parts, with all parts aiming to illustrate varius features of the DP0.3.  First part demonstrates how to plot the celestial posiition of a single, pre-selected Solar system object on the sky as a funtion of time.  The object, with the ``ssObjectId`` of ``-735085100561880491`` happens to be well-observed, with about 14,000 observations.  The second part illustrates how to extract the apparent magnitude of object as a function of time (the light curve).  

This tutorial assumes the successful completion of the beginner-level Portal tutorial 01 (prepared for the Data Previews 02), and uses the 
Astronomy Data Query Language (ADQL), which is similar to SQL (Structured Query Language).

For more information about the DP0.3 catalogs, tables, and columns, visit the DP0.3 Data Products Definition Document (DPDD) 
:ref:`DP0-3-Data-Products-DPDD` or the DP0.3 Catalog Schema Browser (it is at https://dm.lsst.org/sdm_schemas/browser/dp03.html ).  

.. _DP0-3-Portal-1-Step-1:
=============================================================================
Step 1. Plot the position of a single object on the sky as a function of time
=============================================================================

1.1.  Log on to the Rubin Science Platform, and select the Portal option.  In order to access the DP0.3 Tap Service, you need to click on the ``Show`` button on the upper right side of the screen (marked as (1) on the screenshot below).  In the "Select TAP Service" box, you should click on the down-arrow, and choose the ``LSST DP0.3 SSO`` entry.  In the box below that, for ``Table Collection``, you need to select ``dp03_caalogs``, and for ``Table``, select ``dp03_catalogs.DiaSurce``.  In the ``Output Column Selection and Constraints`` select the ``decl``, ``midPointTai``, and ``ra`` entries by clicking the respective boxes next to the ``Name`` column.  Since you want to plot the celestial position of a single object, also click the box next to the ``ssObjectId`` line, and enter ``= -735085100561880491`` in the ``constraints`` box.  Make sure the boxes by ``Spatial`` and ``Temporal`` constraints (under ``Enter Constraints``) are unchecked.  Also make sure that the ``Row limit`` box is set to ``50000`` (should default to this value).  

** Screenshot **

1.2.  Execute the search by clicking the ``Search`` button on lower left, marked as (2) on the screenshot above.  This will generate the plot as below.  Click the ``Bi-view Tables`` button on the upper right to display only the scatter plot and the table.  

** Screenshot **

1.3.  The plot below does not give you the information about the epochs of individual pointings.  You can use the color of individual points to illustrate the time evolution of the object's position.  To do so, click on the two gears on the upper right, which will bring the box below.  There, enter ``ra`` and ``decl`` respectively for the x and y axis.  Enter ``midPointTai`` in the ``Color Map`` box.  Note that entering the first one or two characters in that box will return a choice of entries matching those characters.  You can enter any choice for the ``Color Scale`` box, but an easy to visualize choice is ``Rainbow`` since the order of colors is likely familiar to anyone.  Feel free to select another color scale!  

Note the loop-like structure in the plot.  This is of course expected - you are plotting the position of the object as seen from the Earth, resulting in epicycle-like behavior.  

.. _DP0-3-Portal-1-Step-2:
==============================================================================
Step 2. Plot the magnitude of a single object on the sky as a function of time
==============================================================================

2.1.  Return to the "chart options and tools" box by clicking the two-gear icon on the upper right.   Now select "midPointTai" for x, and "mag" for y axis, as in the screenshot below.  You can also restrict the range of observation times, to examine the behavior of the object during, say, one year.  

** screenshot **

2.2.  To make sure you are plotting the magnitude as measured in the same filter (band), you need to enter ``= i`` in the box just below the "Filter" column heading, and hit "Enter."  This should result in a plot as below.  

** Screenshot **

===========================================================================
Step 3. Plot various derived parameters single object as a function of time
===========================================================================

3.1. In this part, we will plot various parameters of an object as a function of time.  This requires joining multiple tables because not all tables contain the observation epoch, ``midPointTai``.  Specifically, 

Need to do a JOINT ADQL search:  

.. code-block:: SQL 

   SELECT
   diasrc.ra, diasrc.decl, diasrc.diaObjectId, diasrc.diaSourceId, diasrc.midPointTai, diasrc.ccdVisitId, 
    sss.phaseAngle, sss.topocentricDist, sss.heliocentricDist, sss.ssObjectId
   FROM dp03_catalogs.DiaSource AS diasrc 
   JOIN dp03_catalogs.SSSource AS sss 
   ON diasrc.diaSourceId = sss.diaSourceId
   WHERE sss.ssObjectId = -735085100561880491



