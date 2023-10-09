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


#######################################
04. Phase curve fit analysis (Advanced)
#######################################

.. This section should provide a brief, top-level description of the page.

**Contact authors:** Melissa Graham and Yumi Choi

**Last verified to run:** 

**Targeted learning level:** Advanced


.. _DP0-3-Portal-3-Intro:

Introduction
============

_TBD_

Phase curve fits and absolute magnitudes
----------------------------------------

For Solar System objects, absolute magnitudes (`H`) are defined to be for an object 1 AU from the Sun and 1 AU 
from the observer, and at a phase angle (the angle Sun-object-Earth) of 0 degrees.
Absolute magnitudes are derived by fitting a function (the slope parameter `G12`) to the relationship between 
reduced magnitude :math:`H(\alpha)` and phase angle :math:`\alpha` (i.e., the phase curve), and evaluating the function at a phase angle of 0 deg.
The results of phase curve fits in each of the LSST's four filters, griz, are stored in the ``SSObject`` table.
Note that rotation curves or complex geometry of solar system objects are not included in DP0.3 simulations. 
Thus, any changes over time in an object’s apparent magnitude are due only to changes in its distance and phase angle.

A suitable beginner-level reference to the simple H and G magnitude system (`HG model`) for asteroids is
`Dymock 2007 <https://adsabs.harvard.edu/full/2007JBAA..117..342D>`_. 
This paper describes the reduced magnitude, which is corrected for distance, :math:`H(\alpha)`, as:

.. math::

    H(\alpha) = V - 5 \log_{10}(r \Delta),

where :math:`\alpha` is the phase angle, :math:`\Delta` is the topocentric distance, 
`r` is the heliocentric distance, and `V` is the apparent magnitude.

The absolute magnitude `H` can be derived by fitting a function, where the choice of 
form for this function has several options 
(see `Muinonen et al. 2010 <https://ui.adsabs.harvard.edu/abs/2010Icar..209..542M>)`_. 
Dymock (2007) presents a simpler version with a single parameter `G`, using the equation:

.. math::

    H = H(\alpha) + 2.5 \log_{10}((1-G)\phi_1(\alpha) + G\phi_2(\alpha)),

where:

.. math::
    \phi_i(\alpha) = exp(-A_i tan(0.5\alpha)^{Bi}).

In the above equation, 
:math:`A_1` = 3.33, 
:math:`B_1` = 0.63, 
:math:`A_2` = 1.87, and 
:math:`B_2` = 1.22.

To better accommodate various observational effects (e.g., photometric quality, incomplete phase angle sampling) 
a more sophisticated `HG1G2 model` (a linear three-parameter function) and its nonlinear two-parameter version 
`HG12 model` were developed by Muinonen et al. (2010). The two-parameter `HG12 model` is generally very effective
for deriving reliable values of absolute magnitude when the phase angle sampling is not optimal (e.g., poor phase
angle coverage at a range of phase angle). Thus, the LSST data products will compute estimated parameters of the
`HG12 model` and this will be the focus of this tutorial. The `HG12 model` expresses the `G1` and `G2` parameters
as a piecewise linear function of a single parameter, `G12`:

.. math::

    H(\alpha) = H − 2.5 \log_{10}[G1\phi_1(\alpha)+G2\phi_2(\alpha) + (1-G1-G2)\phi_3(\alpha)], 

where:

:math:`G1 = 0.9529 \times G12 + 0.02162 and G2 = -0.6125 \times G12 + 0.5572 for G12 \ge 0.2` and 
:math:`G1 = 0.7527 \times G12 + 0.06164 and G2 = -0.9612 \times G12 + 0.6270 for G12 < 0.2`.
  
**MENTION WHAT WAS USED TO GET THE FIT RESULTS IN SSOBJECT, WHICH IS G12 NOT G. DESCRIBE HOW DIFFERENT.**
**IF THEY'RE REALLY DIFFERENT, REPLACE THE ABOVE WITH A DESCRIPTION OF G12, NOT JUST G.**

**Note** that no time domain evolution in object brightness was included in the DP0.3 simulation
(e.g., rotation curves for non-spherical objects, outgassing events).

.. _DP0-3-Portal-4-Step-2:  

Step 2. Explore the population of the Main Belt Asteroids
=========================================================

Step 2.1.  The Main Belt Asteroids (MBAs) are located, roughly, in the band of semi-major axes ``a`` between 1.6 au and 4.2 au - the definition is not uniform in the literature.  
The location of the Belt is between Mars's and Jupiter's orbits.  
Here, we will plot the distribution of the number of MBAs as a function of ``a``, eccentricities ``e`` and inclinations ``incl`` in the region above.  
Note that semi-major axes are not directly available in the ``dp03_catalogs_10yr.MPCORB`` table, so the constraint on ``a`` is derived from perihelion ``q`` and eccentricity ``e``.  
First, execute the query below to select a good number of MBAs, in the range 1.6 au < ``a`` < 5.5 au (somewhat larger than the definition above), to explore the distribution of their properties.  
You might want to increase the "Row limit" to 200,000 to have an appreciable sample of objects by entering this number in the box on the lower left.  

.. code-block:: SQL 

    SELECT mpc.ssObjectId, mpc.e, mpc.incl, mpc.q, mpc.peri, 
    sso.numObs, sso.ssObjectId, sso.g_H, sso.r_H, sso.i_H, sso.z_H 
    FROM dp03_catalogs_10yr.MPCORB as mpc 
    JOIN dp03_catalogs_10yr.SSObject as sso 
    ON mpc.ssObjectId = sso.ssObjectId 
    WHERE mpc.ssObjectId < 9223370875126069107 
    AND mpc.ssObjectId > 7331137166374808576 
    AND (mpc.q / (1-mpc.e)) > 1.6 
    AND (mpc.q / (1-mpc.e)) < 5.2
    AND sso.numObs > 200 

In the query above, in order to have the query execution not to take too long, we restrict the number of returned objects to have their ``mpc.ssObjectId`` in the limited range.  
We also select only the objects with more than 200 observations.  The query will return about 130,000 objects.  

Step 2.2.  Plot the distribution of semi-major axes ``a``, eccentricities ``e`` and inclinations ``incl`` of orbits of the objects in your query.  
The execution of the query will result in a blank panel for the plot, with a comment "Cannot display the requested data."  
To plot the distribution of ``a`` you need to click on the "plot settings" icon (two gears), click on "add a new chart,"  select "Histogram" for "Plot Type."  
Enter "q / (1-e)" as the "column or expression" and "100" for number of bins as on the screenshot below.  

.. figure:: /_static/portal_tut04_step02a.png
    :width: 400
    :name: portal_tut04_step02a
    :alt: A screenshot illustrating the selection of plot parameters to plot the histogram of the distribution of semi-major axes of the Main Belt Asteroids.


Clicking "Apply" will result in the following table + plot below.  
You should close the chart stating "cannot display requested data" by clicking the blue "X" mark in its upper right hand corner.  
Note that the distribution of asteroids as a function of semi-major axis is not uniform, but it reveals a number of peaks and gaps where there are very few (or no) objects. 
These are known as Kirkwood gaps, which arise due to resonances between the asteroid's and Jupiter's orbital periods.  

.. figure:: /_static/portal_tut04_step02b.png
    :width: 600
    :name: portal_tut04_step02b
    :alt: A screenshot illustrating the the distribution of semi-major axes of the Main Belt Asteroids.  


You can also explore the eccentricities of asteroids' orbits, by "adding a new chart" with "e" as the "column or expression.  
("Histogram" as the plot type will be selected automatically as youve chose it in the previous part.)  
This will appear as a new plot revealing the distribution of ``e``.  
There are only a few high-eccentricity objects extracted via your query - you can see those more clearly by selecting "log" for "Y" under chart options.  
Finally, produce the third plot, revealing the distribution of orbital inclinatons.  
Do so by clicking again on two gears, "adding a new plot" and selecting "incl" as the expression.  

.. figure:: /_static/portal_tut04_step02c.png
    :width: 600
    :name: portal_tut04_step02b
    :alt: A screenshot illustrating the the distribution of semi-major axes, orbital ellipticities, and orbital inclinations of the Main Belt Asteroids.  


Plots of the distribution of semi-major axes, ecenticities, and orbital inclinations of objects located between 1.6 and 5.5 au.  
Note a small population of objects with high eccentricities (``e`` > 0.4).  
Those are probably comets which happen to be travelling in the region selected by you.  
Also note an increased number of objects arounf 5.5 au - those are Trojan Asteroids, not considered to be a part of the MBA population.  

Step 2.3.  Explore the relationship between inclination as well as eccentricity as a function of semi-major axis.  
You don't have to re-execture the ADQL query as all parameters are already extracted.  
Make another plot by clicking the two gears, and select "Add new chart" and enter "Heatmap" as the "Plot type."  
As an aside, selecting "Heatmap" is more illustrative than plotting individual points.  
First select "q / (1-e)" for X-axis, and "e" for Y-axis, and click on "OK."  Then repeat, by clicking on two gears, and selecting "Add new chart."  
This time, select "q / (1-e)" for X-axis, and "incl" for Y-axis, and click on "OK."  
You will need to get rid of the three charts from Step 2.2 - to do so, close the three plots you've made in 2.2 by clicking the blue "X" on each of them.  
This will result in the plot as below.  

.. figure:: /_static/portal_tut04_step02d.png
    :width: 600
    :name: portal_tut04_step02d
    :alt: A screenshot illustrating the the distribution eccentricity (left) and orbital inclination (right) as a function of semi-major axes of the Main Belt Asteroids.  

**COMMENTS FROM MLG BELOW.  GM'S FIX IS IN 3.1**

**CANNOT BE DONE WITH SSOBJECTID = -735085100561880491**

**DO NOT USE TNO; USE MBA WITH A GOOD PHASE-CURVE FIT.**

.. _DP0-3-Portal-4-Step-3:  

Step 3. Select a well-observed MBA, and plot its phase curve
============================================================

3.1. Execute the following ADQL query to retrieve the r-band magnitudes, phase angles,
heliocentric and topocentric distances, and time of the observations for a well-observed MBA.  
We need an object with large number of observations.  
To identify one, return to the table retrieved in Step 2.  
Click on the header of the column "numObs" - this orders the rows in the table in the ascending order of the number of obsservations.  
The second click provides the descending order.  
We arbitrarily selected the sixth most-observed object in the Table.  
We selected that specific MBA - with ``ssObjectId`` = ``8810278553610239375``.

.. code-block:: SQL 

    SELECT ds.mag, ds.band, ds.midPointMjdTai, 
    ss.phaseAngle, ss.topocentricDist, ss.heliocentricDist 
    FROM dp03_catalogs_10yr.DiaSource AS ds 
    JOIN dp03_catalogs_10yr.SSSource AS ss ON ds.diaSourceId = ss.diaSourceId
    WHERE ss.ssObjectId = 8810278553610239375
    AND ds.band = 'r'

**GM:  Got only this far**

3.2. Use the plot "Settings" function to add new scatter plots showing the r-band magnitude and phase angle
as a function of time (right two plots, below), and see that these quantities are not correlated with time.
Add a new scatter plot showing the r-band magnitude as a function of phase angle, which are correlated.

.. figure:: /_static/MLG_portal_tut03_step03a.png
    :name: portal_tut03_step03a
    :alt: A screenshot of three plots showing magnitude and phase angle are not correlated with time, and that magnitude is correlated with phase angle.

    Three plots demonstrating that magnitude and phase angle are correlated with each other, but not with time.

3.3. Delete the two plots with time on the x-axis, leaving only the magnitude vs. phase angle plot.

3.4. Create a new column to hold the distance-corrected r-band magnitudes.
In the table panel, click on the icon to add a new column (the narrow rectangle to the left of a + sign).
In the pop-up window, set the "Name" to "reduced_mag" and the "Expression" to be ``mag - 5 * log10(topocentricDist * heliocentricDist)``.
Click "Add Column".

3.5. Use the plot "Settings" funtion to plot reduced magnitude as a function of phase angle.

3.6. _Create new columns to hold :math:`\phi_1(\alpha)` and :math:`\phi_2(\alpha)`._

3.7. _Get the G and H parametrs for r-band from the ``SSObject`` table._

3.8. _Create another new column that is :math:`H_{fit}(\alpha) = H - 2.5 log((1-G)\phi_1(\alpha) +G \phi_2(\alpha))`._
_The right side of that equation is now just based on phase angle and the fit H and G from ``SSObject``._

3.9. _Overplot :math:`H_{fit}(\alpha)` as a new trace on the existing :math:`H(\alpha)` vs. phase angle plot._
_All the points should look line a "line". Does it look like a "fit" to the data?_


