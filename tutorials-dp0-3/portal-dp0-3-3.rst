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


######################################################################
03. Analyze a well-sampled TNO in a Deep Drilling Field (Intermediate)
######################################################################

.. This section should provide a brief, top-level description of the page.

**Contact authors:** Greg Madejski and Melissa Graham

**Last verified to run:** July 6, 2023

**Targeted learning level:** Intermediate


.. _DP0-3-Portal-3-Intro:

Introduction
============

This tutorial demonstrates how to identify a population of `Trans-Neptunian Objects <https://en.wikipedia.org/wiki/Trans-Neptunian_object>`_ 
(TNOs) in the simulated DP0.3 catalogs.
TNOs are defined by having orbits with semi-major axes beyond the orbit of Neputne (> 30.1 AU).
As the semi-major axis (``a``) can be derived from the orbit's ellipticiy (``e``) and perihelion distance (``q``) as
``a`` = ``q``/(1. - ``e``), and as both ellipticity and perihelion are available in the ``MPCORB`` table,
a sample of TNOs can be identified in the DP0.3 data set (see Step 1).

Compared to Solar System objects closer to Earth, such as Main Belt Asteroids or Near-Earth Objects (NEOs),
TNOs move relatively slowly across the sky.
This relatively slow movement means that TNOs that fall within an LSST Deep Drilling Field (DDF) can stay within that
field, and LSST can accumulate thousands of observations of them.
This tutorial explores one such TNO (see Step 2).

More information about the LSST DDFs can be found on the `LSST DDF webpage <https://www.lsst.org/scientists/survey-design/ddf>`_
and in Section 2.6 of the Survey Cadence Optimization Committee's Phase 2 Recommendations report 
(`PSTN-055 <https://pstn-055.lsst.io/>`_).
Note that DP0.2 did not include DDF observations, so the ability to explore science with a DDF-like cadence this is unique to the DP0.3 simulation.

This tutorial assumes the successful completion of the beginner-level DP0.3 Portal tutorials,
and uses the Astronomy Data Query Language (ADQL), which is similar to SQL (Structured Query Language).
For more information about the DP0.3 catalogs, tables, and columns, see the :ref:`DP0-3-Data-Products-DPDD`.  


.. _DP0-3-Portal-3-Step-1:

Step 1. Identify a population of TNOs
=====================================

1.1. Log into the Rubin Science Platform at `data.lsst.cloud <https://data.lsst.cloud>`_ and select the Portal Aspect.
At upper right, next to "TAP Services" choose to "Show", and then select "LSST DP0.3 SSO" from the drop-down menu that appears at the top.

1.2. At upper right, next to "View" choose "Edit ADQL".
Enter the following ADQL statement into the ADQL Query box.
It will return the ellipticiety (``e``), perihelion distance (``q``), and inclination (``incl``) for a
random subset of objects in the ``MPCORB`` table.
For an explanation of why this constraint on ``ssObjectId`` returns a random sample, see Step 2 of
DP0.3 Portal tutorial 01, "Introduction to DP0.3: the ``MPCORB`` and ``SSObject`` tables".

.. code-block:: SQL 

    SELECT e, q, incl 
    FROM dp03_catalogs.MPCORB 
    WHERE ssObjectId > 9000000000000000000 

1.3. Set the "Row Limit" to be 200000 and click "Search".

1.4. The default results view will show a heatmap plot of ``q`` vs. ``e`` at left, and the table view at right.

.. figure:: /_static/MLG_portal_tut03_step01a.png
    :name: MLG_portal_tut03_step01a
    :alt: A screenshot of the default results view for the query.

    The default results view for the query, with heatmap at left and table at right.

1.5. Create a column of semi-major axis, ``a``.
In the upper right column of the table panel, click on the icon to add a column (a tall narrow rectangle to the left of a + sign).
In the pop-up window to "Add a column", set the "Name" to "a", the "Expression" to "q/(1-e)", the "Units" to "AU",
and the "Description" to "semi-major axis".
Click "Add Column", and see the new column appear in the table.

.. figure:: /_static/MLG_portal_tut03_step01b.png
    :width: 400
    :name: MLG_portal_tut03_step01b
    :alt: A screenshot of the pop-up window to add a column.

    The "Add a column" pop-up window.

1.6. Create a scatter plot of inclination vs. semi-major axis.
In the plot panel, click the "Settings" icon (double gears), and select "Add New Chart".
Set the "Plot Type" to "Scatter", the "X" to "a", "Y" to "incl".
Set the "X Min" to "0", the "X Max" to 60, the "Y Min" to 0, and the "Y Max" to 80.
Set the axis labels as shown in the figure below.
Click "OK".

.. figure:: /_static/MLG_portal_tut03_step01c.png
    :width: 400
    :name: MLG_portal_tut03_step01c
    :alt: A screenshot of the plot parameters pop-up window.

    Create a new plot with these parameters.

1.7. Delete the default plot by clicking on the blue cross in the upper right corner, so that only
the newly-created plot appears (it should look like the plot below).
TNOs appear as a distinct population with ``a`` > 30.1 AU in this parameter space.

.. figure:: /_static/MLG_portal_tut03_step01d.png
    :width: 600
    :name: MLG_portal_tut03_step01d
    :alt: A screenshot of the inclination versus semi-major axis showing a clear population of TNOs.

    The population of TNOs has x-values greater than 30 AU.

1.8. Clear the query and results and return to the RSP TAP Search form.


.. _DP0-3-Portal-3-Step-2:

Step 2. Find and explore a well-observed TNO
============================================

2.1. Follow steps 1.1 and 1.2 above to navigate to the ADQL query interface, and enter the query below.
This query has the same basis as the one used above in step 1.2, with three changes.
One, it joins with the ``DiaSource`` table to retrive the number of ``DiaSources`` (i.e., detections) associated with each object.
Two, it applies a constraint that the semi-major axis be between 30 and 100 AU.
Three, it uses a different constraint on ``ssObjectId`` to return a different random subset.

.. code-block:: SQL 

    SELECT mpc.ssObjectId, COUNT(ds.ssObjectId), mpc.e, mpc.q 
    FROM dp03_catalogs.MPCORB AS mpc 
    JOIN dp03_catalogs.DiaSource AS ds ON mpc.ssObjectId = ds.ssObjectId 
    WHERE mpc.ssObjectId < -7000000000000000000 
    AND mpc.q > 30 * (1 - mpc.e) 
    AND mpc.q < 100 * (1 - mpc.e) 
    GROUP BY mpc.ssObjectId, mpc.e, mpc.q 


2.2. The default results view plots the first two columns against each other, ``ssObjectId`` and ``COUNT``,
which is not particularly useful but it does show the number of detections for the most oft-detected TNOs 
is in the thousands.
Click twice on the ``COUNT`` in the table to short descending by count.

.. figure:: /_static/MLG_portal_tut03_step02a.png
    :name: MLG_portal_tut03_step02a
    :alt: A screenshot of the default results view with the table sorted by count.

    The default results view from the ADQL query above.


**WHY DOES THIS QUERY NOT CONTAIN ``ssObjectId`` = -735085100561880491 ????**

**IT SHOULD CONTAIN IT. IT'S HOW I WAS GOING TO SEGUAY FROM STEP 1 TO 2!! :(**

2.3. **SKIP THIS STEP FOR NOW; FIGURE OUT HOW TO GO FROM THE ABOVE TO BELOW LATER**


2.4. Return to the ADQL query interface and use the following statement to retrieve the
sky coordinates, magnitudes, filter, and time of observations (``midPointTai``) for 
the oft-observed TNO with ``ssObjectId`` = -735085100561880491.

.. code-block:: SQL 

    SELECT ra, decl, mag, filter, midPointTai 
    FROM dp03_catalogs.DiaSource 
    WHERE ssObjectId = -735085100561880491


2.5. The default results view will show the "Coverage" map at upper left.
In the future, with real LSST data, this map would have an underlay of the LSST deeply stacked image. 
Since DP0.3 has no images, the "Coverage" map only shows the overlay of RA vs. Dec, which is
redundant with the default plot.
At upper right, click on "Bi-view Tables" to hide the "Coverage" map and show only the table and plot.

.. figure:: /_static/MLG_portal_tut03_step02b.png
    :name: MLG_portal_tut03_step02b
    :alt: The default results view after clicking on bi-view tables.

    The "Bi-view Tables" results view for the query of ``ssObjectId`` = -735085100561880491.


2.6. Set the color of individual points to represent the time of the observation to 
better illustrate how the object moves across the sky.
In the plot panel, click on the "Settings" icon (double gears) to open the "Plot Parameters"
pop-up window.
Under "Trace Options", for "Color Map" enter ``midPointTai`` and for "Color Scale" enter "Rainbow".
Then click "Apply".

.. figure:: /_static/MLG_portal_tut03_step02c.png
    :width: 600
    :name: MLG_portal_tut03_step02c
    :alt: A screenshot of the plot of sky coordinates colored as a function of time.

    The 10 loops in the object's path on the sky is a result of Earth's orbital period and the 10-year LSST duration.



**BELOW, SPLIT STEP 3 INTO 3. PLOTTING ORBIT FROM SSSOURCE AND 4. PLOTTING PHASE CURVE FROM DIASOURCE+SSOBJECT JOIN**

**DO NOT PLOT MAG vs TIME. IT IS NOT MEANINGFUL IN DP0.3. ONLY MAG VS PHASE.**

**FOR 4. see what Yumi and Christina are doing for phase curve fits. I've hacked out a way to overplot a phase curve funtion and can tell you later.**

.. _DP0-3-Portal-3-Step-3:

Step 3. Plot various derived parameters of a single object as a function of time
================================================================================

3.1. In this part, we will plot various parameters of an object as a function of time.  
This requires joining multiple tables because not all tables contain the observation epoch, ``midPointTai``.  
Specifically, we will be joining the ``dp03_catalogs.DiaSource`` table (from which we get the time of the observation, ``midPointTai``) with the ``dp03_catalogs.SSSource`` table, using the ``diaSourceId`` column present in both tables.  
As an example, we can add the phase angle of the object, as well as the topocentric and heliocentric distance to the object so we can plot those quantities as a function of time.  
This can be done via an ADQL search.  To execute it, click on the ``RSP TAP Search`` and then on ``Edit ADQL`` button, and enter the following ADQL commands:  

.. code-block:: SQL 

   SELECT
   diasrc.ra, diasrc.decl, diasrc.diaObjectId, diasrc.diaSourceId, diasrc.midPointTai, diasrc.ccdVisitId, 
   sss.phaseAngle, sss.topocentricDist, sss.heliocentricDist, sss.ssObjectId
   FROM dp03_catalogs.DiaSource AS diasrc 
   JOIN dp03_catalogs.SSSource AS sss 
   ON diasrc.diaSourceId = sss.diaSourceId
   WHERE sss.ssObjectId = -735085100561880491

3.2.  Executing this search resulted in additional columns beyond the RA, Dec, and magnitude in the previous Step.  
This is shown on the screenshot below.  
Note that the plot on the right, by default, is the first two columns of the table on the left.  

.. figure:: /_static/portal_tut03_step03a.png
    :name: portal_tut03_step03a

Now, we can plot those newly retrieved quantities against time:  two obvious plots would be the topocentric and heliocentric distance, both as a function of MJD time.  
In both cases, we need to appropriately change the "Chart Options and Tools" - probably straightforward, similar to what we've done previously.  

.. figure:: /_static/portal_tut03_step03b.png
    :name: portal_tut03_step03b

===================================
Step 4.  Exercises for the learner: 
===================================

(1) Plot the histogram of the number of visits to the solar System objects in the ``dp03_catalogs.SSObject`` for objects observed more than 1000 times.  

(2) Repeat the steps above for another object with a large number of observations (say another one with ``numObs`` > 10,000).  

