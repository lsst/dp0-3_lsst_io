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

**Credits:** This tutorial incorporates material from the DP0.3 tutorial notebook on the introduction 
to phase curves by Christina Williams and Yumi Choi.


.. _DP0-3-Portal-3-Intro:

Introduction
============

This portal tutorial is the same demonstration used in the tutorial notebook DP03_04a to illustrate the 
phase curves of solar system objects, but fouces on Main Belt Asteroids (MBAs).

Phase curve fits and absolute magnitudes
----------------------------------------

Solar system objects in the DP0.3 catalogs change position and brightness between each Rubin image as they orbit about
the Sun over time. In the DP0.3 catalogs, their intrinsic properties and orbital parameters are known, and are used to 
estimate what the measurements would be in a given image, and how they change between images. From these simulated 
observations, it is possible to reconstruct their intrinsic properties and orbital parameters in the same way as will 
be done using the real LSST data. 

An important way to characterize intrinsic properties of a solar system object is by measuring its "phase curve", 
which is the object brightness as a function of its "solar phase angle" (the angle made between the line of sight 
from the object to the Sun, and the line of sight from the object to Earth). For Solar System objects, absolute 
magnitudes (`H`) are defined to be for an object 1 au from the Sun and 1 au from the observer, and at a phase 
angle :math:`\alpha` (the angle Sun-object-Earth) of 0 degrees. Absolute magnitudes are derived by fitting a 
function to the relationship between reduced magnitude :math:`H(\alpha)` and phase angle :math:`\alpha` 
(i.e., the phase curve), and evaluating the function at a phase angle of 0 degrees. The reduced magnitude, 
which is corrected for distance, :math:`H(\alpha)`, as:

.. math::

    H(\alpha) = m - 5 \log_{10}(d_{t} d_{h}),

where :math:`\alpha` is the phase angle, :math:`d_{t}` is the topocentric distance, 
`d_{h}` is the heliocentric distance, and `m` is the apparent magnitude.

The absolute magnitude `H` can be derived by fitting a function, where the choice of 
form for this function has several options 
(see `Muinonen et al. 2010 <https://ui.adsabs.harvard.edu/abs/2010Icar..209..542M>`_). 
The simple two-parameter model (`HG model`) for asteroids provides a best fit for the absolute magnitude `H` and
the slope parameter `G`. The `HG model` parameters were used to predict the observed parameters for each object. 
These truth values are defined in the ``MPCORB`` table as `mpcH` (intrinsic absolute magnitude in `V` band) and 
`mpcG` (intrinsic slope, which has a constant value of 0.15 for all DP0.3 objects). The `HG model` has the form:

.. math::

    H = H(\alpha) + 2.5 \log_{10}((1-G)\phi_1(\alpha) + G\phi_2(\alpha)).

To better accommodate various observational effects (e.g., photometric quality, incomplete phase angle sampling) 
a more sophisticated `HG1G2 model` (a linear three-parameter function) and its nonlinear two-parameter version 
`HG12 model` were developed (`Muinonen et al. 2010 <https://ui.adsabs.harvard.edu/abs/2010Icar..209..542M>`_). 
The two-parameter `HG12 model` is generally very effective for deriving reliable values of absolute magnitude when 
the phase angle sampling is not optimal (e.g., poor phase angle coverage at a range of phase angle). Thus, the LSST 
data products will compute estimated parameters of the `HG12 model` and this will be the focus of this tutorial. 
The `HG12 model` expresses the `G1` and `G2` parameters as a piecewise linear function of a single parameter, `G12`:

.. math::

    H(\alpha) = H − 2.5 \log_{10}[G1\phi_1(\alpha)+G2\phi_2(\alpha) + (1-G1-G2)\phi_3(\alpha)], 

where:

:math:`G1 = 0.9529 \times G12 + 0.02162`, :math:`G2 = -0.6125 \times G12 + 0.5572` for :math:`G12 \ge 0.2`, and 
:math:`G1 = 0.7527 \times G12 + 0.06164`, :math:`G2 = -0.9612 \times G12 + 0.6270` for :math:`G12 < 0.2`.

The results of phase curve fits (`H` and `G12`) in the four LSST filters, `griz`, are stored in the ``SSObject`` table. 
The explanation for the absence of `u` and `y` bands in DP0.3 catalogs can be found in the `DP0.3 documentation 
<https://dp0-3.lsst.io/data-products-dp0-3/data-simulation-dp0-3.html>`_.
Note that rotation curves or complex geometry of solar system objects are not included in DP0.3 simulations. 
Thus, any changes over time in an object’s apparent magnitude are due only to changes in its distance and phase angle.

.. _DP0-3-Portal-4-Step-1:  

Step 1. Query the DP0.3 tables for the Main Belt Asteroids
==========================================================

Step 1.1. Log into the Rubin Science Platform at data.lsst.cloud and select the Portal Aspect. At upper right, next to 
"TAP Services" choose to "Show", and then select "LSST DP0.3 SSO" from the drop-down menu that appears at the top. 

Step 1.2. At upper right, next to "View" choose "Edit ADQL". Enter the query statement below into the ADQL Query box and  
execute the query to select a good number of MBAs with a fair number of total observations (``numObs`` > 100) 
to explore the distribution of their properties. Following the population definitions used by the 
`JPL Horizons small body database query tool <https://ssd.jpl.nasa.gov/tools/sbdb_query.html>`_, we select MBAs
as objects with semi-major axes ``a`` between 2.0 au and 3.25 au and perihelion distance ``q`` > 1.666 au.
Note that semi-major axes are not directly available in the ``MPCORB`` table, so the constraint 
on ``a`` is derived from perihelion ``q`` and eccentricity ``e``. You might want to increase the "Row limit" to 
100,000 to have an appreciable sample of objects by entering this number in the box on the lower left. 
In order to have the query execution not to take too long, we restrict the number of returned objects to have their 
``mpc.ssObjectId`` in the limited range.   

.. code-block:: SQL 

    SELECT mpc.ssObjectId, mpc.e, mpc.q, mpc.mpcG, mpcH, 
    sso.numObs,
    sso.g_H, sso.g_Herr, sso.g_G12, sso.g_G12err, sso.g_Ndata, 
    sso.r_H, sso.r_Herr, sso.r_G12, sso.r_G12err, sso.r_Ndata,
    sso.i_H, sso.i_Herr, sso.i_G12, sso.i_G12err, sso.i_Ndata, 
    sso.z_H, sso.z_Herr, sso.z_G12, sso.z_G12err, sso.z_Ndata
    FROM dp03_catalogs_10yr.MPCORB as mpc 
    JOIN dp03_catalogs_10yr.SSObject as sso 
    ON mpc.ssObjectId = sso.ssObjectId 
    WHERE mpc.ssObjectId < 9223370875126069107 
    AND mpc.ssObjectId > 7331137166374808576 
    AND (mpc.q / (1-mpc.e)) > 2.0 
    AND (mpc.q / (1-mpc.e)) < 3.25
    AND (mpc.q > 1.666)
    AND sso.numObs > 100 

Step 1.3. Plot the distribution of semi-major axes ``a`` of orbits of the objects in your query.  
The execution of the query will result in a blank panel for the plot, with a comment "Cannot display the requested data."  
To plot the distribution of ``a`` you need to click on the "Chart options and tools" icon (two gears), click on "add a new chart", 
select "Histogram" for "Plot Type", enter "q / (1-e)" as the "column or expression" and "100" for number of bins as on the screenshot below.  

.. figure:: /_static/portal_tut04_step01a.png
    :width: 400
    :name: portal_tut04_step01a
    :alt: A screenshot illustrating the selection of plot parameters to plot the histogram of the distribution of semi-major axes of MBAs.

Clicking "Ok" will result in the following table + plot below.  
Close the chart stating "cannot display requested data" by clicking the blue "X" mark in its upper right hand corner.  
Note that the distribution of asteroids as a function of semi-major axis is not uniform, but it reveals a number of peaks and gaps 
where there are very few (or no) objects. 
These are known as Kirkwood gaps, which arise due to resonances between the asteroid's and Jupiter's orbital periods.  

.. figure:: /_static/portal_tut04_step01b.png
    :width: 600
    :name: portal_tut04_step01b
    :alt: A screenshot illustrating the the distribution of semi-major axes of MBAs.  

.. _DP0-3-Portal-4-Step-2:  

Step 2. Select a well-observed MBA, and plot its phase curve
============================================================

Step 2.1. Unique solar system objects in the ``SSObject`` and ``MPCORB`` tables will be observed many times over the full LSST survey. 
Individual observations of each unique object in each filter are recorded in the ``SSSource`` and ``diaSource`` tables. 
Below, we query these tables to obtain all of the individual observed time series data (we call indivObs) for an MBA that has 
more than 2000 observations. 

First, select MBAs with 2000 or more observations by entering ">2000" in the box underneath the table heading ``numObs`` 
and hitting "enter" as shown as below. This will leave only a small fraction of queried 100,000 MBAs above, 25 MBAs in this tutorial.
To go back to the originally retreived table by removing the applied filter, click the banned filter icon on the top right of the table.

.. figure:: /_static/portal_tut04_step02a.png
    :width: 600
    :name: portal_tut04_step02a
    :alt: A screenshot selecting MBAs that have more than 2000 observations.

Pick and copy one ``ssObjectId``. Hovering over a table cell shows you a triple-dot box. If you right click that box, there are two 
options pop up: "Copy to clipboard" and "View as plain text". Here, copy ``ssObjectId`` = ``7470575696289418102`` to clipboard and click 
"RSP TAP Search" button on the top left to go back to the ADQL Query page. 

.. figure:: /_static/portal_tut04_step02b.png
    :width: 300
    :name: portal_tut04_step02b
    :alt: A screenshot copying ssObjectId for a well-observed MBA.

Execute the following ADQL query to retrieve the apparent magnitudes, magnitude errors, filters, phase angles,
topocentric and heliocentric distances of the individual observations for a well-observed MBA.  

.. code-block:: SQL 

    SELECT
    dia.ssObjectId, dia.mag, dia.magErr, dia.band, 
    sss.phaseAngle, sss.topocentricDist, sss.heliocentricDist
    FROM dp03_catalogs_10yr.DiaSource as dia
    INNER JOIN dp03_catalogs_10yr.SSSource as sss ON dia.diaSourceId = sss.diaSourceId
    WHERE dia.ssObjectId = 7470575696289418102

Step 2.2. Use the plot "Settings" function to add new scatter plots showing the r-band magnitude and phase angle
as a function of time (right two plots, below), and see that these quantities are not correlated with time.
Add a new scatter plot showing the r-band magnitude as a function of phase angle, which are correlated.

.. figure:: /_static/MLG_portal_tut03_step03a.png
    :name: portal_tut03_step03a
    :alt: A screenshot of three plots showing magnitude and phase angle are not correlated with time, and that magnitude is correlated with phase angle.

    Three plots demonstrating that magnitude and phase angle are correlated with each other, but not with time.

2.3. Delete the two plots with time on the x-axis, leaving only the magnitude vs. phase angle plot.

2.4. Create a new column to hold the distance-corrected r-band magnitudes.
In the table panel, click on the icon to add a new column (the narrow rectangle to the left of a + sign).
In the pop-up window, set the "Name" to "reduced_mag" and the "Expression" to be ``mag - 5 * log10(topocentricDist * heliocentricDist)``.
Click "Add Column".

2.5. Use the plot "Settings" funtion to plot reduced magnitude as a function of phase angle.

2.6. _Create new columns to hold :math:`\phi_1(\alpha)` and :math:`\phi_2(\alpha)`._

2.7. _Get the G and H parametrs for r-band from the ``SSObject`` table._

3.8. _Create another new column that is :math:`H_{fit}(\alpha) = H - 2.5 log((1-G)\phi_1(\alpha) +G \phi_2(\alpha))`._
_The right side of that equation is now just based on phase angle and the fit H and G from ``SSObject``._

3.9. _Overplot :math:`H_{fit}(\alpha)` as a new trace on the existing :math:`H(\alpha)` vs. phase angle plot._
_All the points should look line a "line". Does it look like a "fit" to the data?_


