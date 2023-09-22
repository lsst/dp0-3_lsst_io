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
03. Explore Trans-Neptunian Objects (TNOs) in DP0.3 (Intermediate)
##################################################################

.. This section should provide a brief, top-level description of the page.

**Contact authors:** Greg Madejski and Melissa Graham

**Last verified to run:** September 15, 2023

**Targeted learning level:** Intermediate


.. _DP0-3-Portal-3-Intro:

Introduction
============

This tutorial demonstrates how to identify and explore a population of `Trans-Neptunian Objects <https://en.wikipedia.org/wiki/Trans-Neptunian_object>`_ 
(TNOs) in the simulated DP0.3 catalogs.
TNOs are defined by having orbits with semi-major axes beyond the orbit of Neputne (> 30.1 AU).
As the semi-major axis (``a``) can be derived from the orbit's ellipticiy (``e``) and perihelion distance (``q``) via
``a`` = ``q``/(1. - ``e``), and as both ellipticity and perihelion are available in the ``MPCORB`` table,
a sample of TNOs can be identified in the DP0.3 data set (see Step 1).  
Their properties (specifically, the relationship between their semi-major axis and eccentricity, as well as the distribution of their derived diameters) will be explored in Step 2.  
Note that some of the objects might not be moving in elliptical orbits (``e > 1`` - meaning they are not bound to the Solar System, but moving on parabolic or hyperbolic orbits).  
Such objects will be excluded from this tutorial, as an application of the formula above would result in a negative value of ``a``.  

Compared to the Solar System objects closer to the Earth, such as Main Belt Asteroids or Near-Earth Objects (NEOs), TNOs move relatively slowly across the sky.
This relatively slow movement means that TNOs that fall within an LSST Deep Drilling Field (DDF) can stay within that
field, and LSST can accumulate thousands of observations of them.
This tutorial explores the position on the sky of one such TNO (Step 3) and plots time-domain quantities such as magnitude and phase angle (Step 4).  
Finally, it provides a visualization of its trajectory projected into 2D (see Step 5).  

More information about the LSST DDFs can be found on the `LSST DDF webpage <https://www.lsst.org/scientists/survey-design/ddf>`_
and in Section 2.6 of the Survey Cadence Optimization Committee's Phase 2 Recommendations report 
(`PSTN-055 <https://pstn-055.lsst.io/>`_).
Note that DP0.2 did not include DDF observations, so the ability to explore science with a DDF-like cadence is unique to the DP0.3 simulation.

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
It will return the ellipticity (``e``), perihelion distance (``q``), and inclination (``incl``) for a
random subset of objects in the ``MPCORB`` table.
For an explanation of why this constraint on ``ssObjectId`` returns a random sample, see Step 2 of
DP0.3 Portal tutorial 01, "Introduction to DP0.3: the ``MPCORB`` and ``SSObject`` tables".

.. code-block:: SQL 

    SELECT e, q, incl 
    FROM dp03_catalogs_10yr.MPCORB 
    WHERE ssObjectId > 9000000000000000000 


1.3. Set the "Row Limit" to be 200000 and click "Search".


1.4. The default results view will show a heatmap plot of ``q`` vs. ``e`` at left, and the table view at right.

.. figure:: /_static/portal_tut03_step01a.png
    :width: 600
    :name: portal_tut03_step01a
    :alt: A screenshot of the default results view for the query.

    The default results view for the query, with the table at right and the heatmap at left.    


1.5.  Exclude the objects moving on unbound orbits.  
Note that a small fraction of the objects - roughly one in a thousand - have derived eccentricities > 1 meaning those are not bound to the Solar System.  
Those objects can be excluded from further analysis by entering ``< 1`` in the box underneath the table heading ``e``, and hitting "enter."  
This will result in a slightly modified display as below.  

.. figure:: /_static/portal_tut03_step01b.png
    :width: 600
    :name: portal_tut03_step01b
    :alt: A screenshot of the default results view for the modified query.

    The view for the query with ``e < 1``.    


1.6. Create a new column in the table, containing semi-major axis, ``a``.
In the upper right column of the table panel, click on the icon to add a column (a tall narrow rectangle to the left of a + sign).
In the pop-up window to "Add a column", set the "Name" to "a", the "Expression" to "q/(1-e)", the "Units" to "au",
and the "Description" to "semi-major axis".  
Click "Add Column", and see the new column appear in the table.

.. figure:: /_static/portal_tut03_step01c.png
    :width: 400
    :name: portal_tut03_step01c
    :alt: A screenshot of the pop-up window to add a column.

    The "Add a column" pop-up window.  


1.7. Create a scatter plot of inclination vs. semi-major axis.
In the plot panel, click the "Settings" icon (double gears), and select "Add New Chart".
Set the "Plot Type" to "Scatter", the "X" to "a", "Y" to "incl".
In the "Chart Options" dropdown menu, set the "X Min" to "0", the "X Max" to 60, the "Y Min" to 0, and the "Y Max" to 80.  
Click "OK".

.. figure:: /_static/portal_tut03_step01d.png
    :width: 400
    :name: portal_tut03_step01d
    :alt: A screenshot of the plot parameters pop-up window.

    Create a new plot with these parameters.


1.8. Delete the default plot by clicking on the blue cross in the upper right corner, so that only the newly-created plot appears (it should look like the plot below).
TNOs appear as a distinct population with ``a`` > 30.1 au in this parameter space.

.. figure:: /_static/portal_tut03_step01e.png
    :width: 600
    :name: portal_tut03_step01e
    :alt: A screenshot of the inclination versus semi-major axis plot, showing a clear population of TNOs.

    The population of TNOs has x-values greater than 30 au.  

1.9.  Notice how in the plot above, the majority of objects returned by the query were closer to the Sun than 30.1 au.  
In fact, only about 600 of the moving objects from the query were TNOs.
The total number of TNOs is estimated to be far less than Main Belt Asteroids, and due to their distance they move more slowly and are fainter, and so are harder to detect and characterize.
In the next step, a revised query will be used to only retrieve objects with semi-major axis greater than 30.1 au.


.. _DP0-3-Portal-3-Step-2:

Step 2. Explore the properties of a population of TNOs
======================================================

2.1.  Now that the population of the Trans-Neptunian Objects has been identified, it is possible to further explore their properties.  
To study the properties of a larger sample of TNOs, return to the ADQL query interface by clicking on "RSP TAP Search" tab, and clicking on "Edit ADQL" button.  

2.2.  Clear the ADQL query, and execute a query below, simiar to the one in Step 1.2, but which includes only objects at ``a`` > 30.1 au.  
Also include the absolute H magnitude ``mpcH`` which will be used in the derivation of diameters of TNOs in the subsequent step (2.4) below.  

.. code-block:: SQL 

    SELECT e, incl, q, mpcH 
    FROM dp03_catalogs_10yr.MPCORB
    WHERE q / (1 - e) > 30.1 AND e < 1 

Keep the "Row limit" to 200000, and click "Search."  By default, you will generate a plot of inclination vs. eccentricity.  


2.3.  Plot the eccentricity of the orbit ``e`` as a function of the semi-major axis ``a``.  
This time (in contrast to Step 1.6 but accomplishing the same goal), calculate ``a`` from ``e`` and ``q`` via 
setting appropriate plot parameters rather than creating another column in the right-hand table.  
To do so, click on the "plot settings" (two gears) on the left-hand panel, and click on "add new chart."  
Select "heatmap" for the plot type, and enter "q/(1-e)" for the X-axis, and "e" for the y-axis.  
Increase the number of bins to 200 for both x and y to improve the resolution of the heatmap.  
Chose any color map you find compelling.  
The plot parameters used here are below.  
In particular, the X-axis is restricted to ``30 < a < 100`` au to illustrate at more detail the region from Neptune's orbit to about three times its orbit.  

.. figure:: /_static/portal_tut03_step02a.png
    :width: 400
    :name: portal_tut03_step02a
    :alt: A screenshot of the plot parameters for the eccentricity vs. semi-major axis plot 

    The plot parameters for the eccentricity vs. semi-major axis plot.  


2.4.  Click on "OK" or "Apply" in the "Plot Parameters" window.  Then delete the "incl vs. e" plot (the leftmost panel).  This will result in the plot as below.  

.. figure:: /_static/portal_tut03_step02b.png
    :width: 600
    :name: portal_tut03_step02b
    :alt: A screenshot of the plot of the eccentricity vs. semi-major axis 

    The plot of the distribution of the eccentricity vs. semi-major axis of Solar System objects at semi-major axis beyond 30 au.  

Note that there is a clear indication of two distinct populations.  
The majority of the objects have low eccentricity, and a semi-major axis of about 80 au.   
Those are commonly known as Trans-Neptunian Objects (TNOs).  
In addition, there is a separate population of high-eccentricity objects, and those are comets.  


2.5.  Plot the distribution of diameters of the Trans-Neptunian Objects derived from their absolute H magnitudes. 
For this you will need to use the formula below, where ``H`` is the absolute H magnitude, and ``A`` is the albedo.  
The equation which gives the diameter d in kilometers  is :math:`d = 10^{(3.1236 - 0.5 \times log(A) - 0.2 \times H)}` .  
Note that the query you executed in Step 2.1 already returned a column with the H magnitude, so you won't need to execute a new query for this step.  
For the purpose of this demonstration, we will use the albedo of 0.15.  
This is a common value in literature (see, e. g., `Vilenius et al. 2012. <https://arxiv.org/pdf/1204.0697.pdf>`_ 
We note that the derived diameter depends only weakly on the adopted albedo.  
Adopting albedo of 0.15, the above expression for ``d`` reduces to :math:`d = 10^{(3.536 - (0.2 \times H))}` km.  

2.6.  Add an additional column by clicking on the "add column" icon above the table.  
Enter ``D`` in the "name" field, and ``power(10,(3.536 - 0.2 * mpcH))`` in the expression field, as below, and click the "Add Column" button.  

.. figure:: /_static/portal_tut03_step02c.png
    :width: 400
    :name: portal_tut03_step02c
    :alt: screenshot illustrating the expression needed to make the new column containing the diameter of the TNO

    The screenshot illustrating the parameters for the new column containing the TNO's diameter.  


2.7.  Plot the distribution of diameters of TNOs extracted in the query of Step 2.1.  
To do so, in "Plot parameters" click on "Add New Chart," select "Histogram" and enter the parameters as below.  
Select log for y axis.  

.. figure:: /_static/portal_tut03_step02d.png
    :width: 400
    :name: portal_tut03_step02d
    :alt: screenshot illustrating the plot parameters for displaying the distribution of TNO's diameters

    The screenshot illustrating the plot parameters for the distribution of the TNO's diameters.  

2.8.  Click on the "Apply" or "OK" button.  This will result in the plot showing the distribution of TNO diameters extracted via your query.  

.. figure:: /_static/portal_tut03_step02e.png
    :width: 600
    :name: portal_tut03_step02e
    :alt: screenshot illustrating the distribution of TNO's diameters

    The screenshot illustrating the distribution of the TNO diameters in your sample, revealing that diameters of most TNOs are in the range of a few hundred kilometers.  


2.9. Clear the query and results and return to the RSP TAP Search form.

.. _DP0-3-Portal-3-Step-3:

Step 3. Find and explore a well-observed TNO
============================================

3.1. The goal of Step 3 is to identify a distant object with a large number of observations, so its position on the sky as a function of time can be plotted.  
Return to the ADQL query interface by clicking on "RSP TAP Search" tab, and clicking on "Edit ADQL" button.  
Enter the query below.  
This query has the same basis as the one used above in step 1.2, with three changes.
One, it joins with the ``DiaSource`` table to retrive the number of ``DiaSources`` (i.e., detections) associated with each object.
Two, it applies a constraint that the semi-major axis be between 30 and 100 AU.
Three, it uses a different constraint on ``ssObjectId`` to return a different random subset.

.. code-block:: SQL 

    SELECT mpc.ssObjectId, COUNT(ds.ssObjectId), mpc.e, mpc.q 
    FROM dp03_catalogs_10yr.MPCORB AS mpc 
    JOIN dp03_catalogs_10yr.DiaSource AS ds ON mpc.ssObjectId = ds.ssObjectId 
    WHERE mpc.ssObjectId < -700000000000000000 
    AND mpc.q > 30 * (1 - mpc.e) 
    AND mpc.q < 100 * (1 - mpc.e) 
    GROUP BY mpc.ssObjectId, mpc.e, mpc.q 


3.2.  Click on "Search" -  this search might take up to a minute.  


3.3. The default results view plots the first two columns against each other, ``ssObjectId`` and ``COUNT``,
which is not a particularly useful plot aside from showing that the number of detections for the most oft-detected objects in the outer Solar System 
is in the thousands.
Click twice on the ``COUNT`` column header to order the entries by descending count and identify the most oft-detected outer Solar System object.  

.. figure:: /_static/portal_tut03_step03a.png
    :width: 600
    :name: portal_tut03_step03a
    :alt: A screenshot of the default results view with the table sorted by count.

    The default results view from the ADQL query above.

The query returns about 12,600 objects.  


3.4.  Continue with the object with the largest number of observations - 12,103 of them! - with the ``ssObjectId`` = -735085100561880491.  
Examine its eccentricity.  Its modest eccentricity ``e = 0.1512`` implies that this is not a comet.  


3.5.  Return to the ADQL query interface and use the following statement to retrieve the sky coordinates, magnitudes, filter (``band``), and time of observations (``midPointMjdTai``) for the oft-observed TNO with ``ssObjectId`` as above.  

.. code-block:: SQL 

    SELECT ra, dec, mag, band, midPointMjdTai 
    FROM dp03_catalogs_10yr.DiaSource 
    WHERE ssObjectId = -735085100561880491


3.6. The default results view will show the "Coverage" map at upper left.
In the future, with real LSST data, this map would have an underlay of the LSST deeply stacked image. 
Since DP0.3 has no images, the "Coverage" map only shows the overlay of RA vs. Dec, which is redundant with the default plot.
At upper right, click on "Bi-view Tables" to hide the "Coverage" map and show only the table and plot.

.. figure:: /_static/portal_tut03_step03b.png
    :width: 600
    :name: portal_tut03_step03b
    :alt: The default results view after clicking on bi-view tables.

    The "Bi-view Tables" results view for the query of ``ssObjectId`` = -735085100561880491.


3.7. Set the color of individual points to represent the time of the observation to 
better illustrate how the object moves across the sky.
In the plot panel, click on the "Settings" icon (double gears) to open the "Plot Parameters"
pop-up window.
Under "Trace Options", for "Color Map" enter "midPointMjdTai" and for "Color Scale" enter "Rainbow".
Then click "Apply".

.. figure:: /_static/portal_tut03_step03c.png
    :width: 600
    :name: portal_tut03_step03c
    :alt: A screenshot of the plot of sky coordinates colored as a function of time.

    The 10 loops in the object's path on the sky is a result of Earth's orbital period and the 10-year LSST duration.  
    Purple color corresponds to earlier observtations, and the red color corresponds to the later observations.  


3.8. Clear the query and results and return to the RSP TAP Search form.

.. _DP0-3-Portal-3-Step-4:

Step 4. Plot the time-domain quantities for the TNO
===================================================

**Note** that no time domain evolution in object brightness was included in the DP0.3 simulation
(e.g., rotation curves for non-spherical objects, outgassing events).
All changes in the brightness of DP0.3 objects with time are due to changes in the distance and phase angle from Earth.  


4.1. Execute the following ADQL query to retrieve the r-band magnitudes, phase angles,
heliocentric and topocentric distances, and time of the observations for the TNO explored in Step 3.

.. code-block:: SQL 

    SELECT ds.midPointMjdTai, ds.mag, ds.band, 
    ss.phaseAngle, ss.topocentricDist, ss.heliocentricDist 
    FROM dp03_catalogs_10yr.DiaSource AS ds 
    JOIN dp03_catalogs_10yr.SSSource AS ss ON ds.diaSourceId = ss.diaSourceId
    WHERE ss.ssObjectId = -735085100561880491
    AND ds.band = 'r'


4.2. The default plot will have the r-band magnitude as a function of time.  
Use the plot "Settings" function to add new scatter plots showing the phase angle as a function of time, ``midPointMjdTai - 60000``  to show more clearly the time of observation.  
This will result in the left two plots, as on the screenshot below.   Note that these quantities are not correlated with time.

4.3.  Add a new scatter plot showing the r-band magnitude as a function of phase angle (right plot), showing that the phase angle and r-band magnitude are correlated.

.. figure:: /_static/portal_tut03_step04a.png
    :name: portal_tut03_step04a
    :width: 600
    :alt: A screenshot of three plots showing magnitude and phase angle are not correlated with time, and that magnitude is correlated with phase angle.

    Three plots demonstrating that magnitude and phase angle are correlated with each other, but not with time.


4.4.  Plot the topocentric and heliocentric distances of the object as a function of time already retrieved in Step 4.1.  
First, delete two of the the three plots prepared in Step 4.2 by clicking on the blue X in the upper right-hand part of the plot panels to make space for new plots.  
Then add a pair of new plots, clicking on the "plot settings."  
In both cases, enter ``midPointMjdTai - 60000`` for X-axis.  
For Y axis - enter ``topocentricDist`` for one plot, and ``heliocentricDist`` for the other.  
After you remove the panel containing the plot made in the previous step, you will see the plots as below.  

.. figure:: /_static/portal_tut03_step04b.png
    :width: 600
    :name: portal_tut03_step04b
    :alt: A screenshot of two plots showing the heliocentric and topocentric distance of the trans-Neptunian object as a function of time.

    Heliocentric and topocentric distance of the TNO as a function of time.  


4.5.  Note the periodic change of the topocentric distance with time resulting from the Earth's motion around the Sun - a different view of the same effect you saw in Step 3.  

.. _DP0-3-Portal-3-Step-5:

Step 5. View the 2-D projection of the TNO's orbit to visualize its 3-D trajectory
==================================================================================

5.1.  The goal of Step 5 is to visualize the 3-D trajectory of the well-observed trans-Neptunian object, via viewing the projections of its 3-D helio- and topocentric distances as a function of time into 2-D.  
Navigate to the ADQL query interface.  
Execute the query below to extract the helio- and topocentric X, Y, and Z distances of the TNO - so you can visualize its trajectory.  

.. code-block:: SQL 

    SELECT heliocentricX, heliocentricY, heliocentricZ,
    topocentricX, topocentricY, topocentricZ, ssObjectId
    FROM dp03_catalogs_10yr.SSSource
    WHERE ssObjectId = -735085100561880491


5.2.  Plot the heliocentric Y distance as a function of heliocentic X distance by clicking on the "plot setings" icon and selecting ``heliocenticY`` for y and ``heliocentricX`` for x. 
Note that the object moves slowly in heliocentric coordinate X as well as in Y (by a comparison to, e.g., Earth's motion), covering only a few au in 10 years.  
This is expected given its multi-au distance from the Sun.  

 .. figure:: /_static/portal_tut03_step05a.png
    :name: portal_tut03_step05a
    :width: 600
    :alt: A screenshot of a plot showing the heliocentric Y vs. heliocentric X distance of the trans-Neptunian object as a function of time.

Heliocentric Y vs. X distance of the trans-Neptunian object as a function of time.  


5.3.  Now plot the heliocentric Z distance as a function of heliocentric X distance.  Click on "Plot Settings" and click on "Add New Chart."  
Select ``heliocentricZ`` for y and ``heliocentricX`` for x.  
Click on "Apply" or "OK."  
Observe that the object's trajectory is not constant in Z - and that means that its orbit is not in the plane of the Ecliptic during the 
simunated Rubin observation, but the object does pass through the ecliptic plane when Z = 0.  

.. figure:: /_static/portal_tut03_step05b.png
    :name: portal_tut03_step05b
    :width: 600
    :alt: A screenshot of a plot showing the heliocentric Z vs. heliocentric Y distance of the trans-Neptunian object as a function of time.

Heliocentric Y vs. X distance of the trans-Neptunian object as a function of time. 


5.4  Next, plot the ``topocentricY`` vs. ``topocentricX`` and ``topocentricZ`` vs. ``topocentricX`` distances.   
On the same screen where you generated the plots in previous two steps, click on "Plot Settings" and click on "Add New Chart." 
First, select ``topocentricY`` for y and ``topocentricX`` for x. and click "Apply" or "OK."   
Next, click on "Plot Settings" and click on "Add New Chart."
There, the effect of position of the TNO on the sky as a result of Earth's orbital motion is clearly apparent.  

 .. figure:: /_static/portal_tut03_step05c.png
    :name: portal_tut03_step05c
    :width: 600
    :alt: A screenshot of two plots showing the heliocentric and topocentric distance of the trans-Neptunian object as a function of time.

    Visualization of the 3-D TNO's trajectory by viewing the 2-D projections of its trajectory as measured from the Sun (top two plots) and the Earth (bottom two plots).  

Note that the RSP Portal automatically displays four plots as a 2 x 2 grid.  

.. **FIND MORE INTERESTING THINGS TO DO AND EXPLORE WITH THIS TNO!**

.. **PLOT DISTANCES OVER TIME, OR MAYBE GET THE HELIO XYZ AND PLOT OUT ORBITAL ARCS, ETC.**

.. **CONSULT WITH ANDRES WHO IS WORKING ON A TNO NB**



.. _DP0-3-Portal-3-Step-6:

Step 6.  Exercises for the learner 
==================================

6.1. Plot the histogram of the number of visits to the Solar System objects in the ``dp03_catalogs.SSObject`` for objects observed more than 1000 times.  

6.2. Repeat the steps 4 and 5 for another object with a large number of observations (say another one with ``numObs`` > 2,000).  
Note that you already identified objects with large number of observations in Steps 3.1 and 3.2.  

