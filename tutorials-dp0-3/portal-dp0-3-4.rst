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

**Contact authors:** Melissa Graham

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
Absolute magnitudes are derived by correcting for distance, fitting a function (the `G` parameter) to the relationship between 
absolute magnitude and phase (i.e., the phase curve), and evaluating the function at a phase of 0 deg.
The results of phase curve fits in each of the LSST's six filters, ugrizy, are stored in the ``SSObject`` table.

A suitable beginner-level reference to the H and G magnitude system for asteroids is
`Dymock 2007 <https://adsabs.harvard.edu/full/2007JBAA..117..342D>`_. 
This paper describes the "reduced magnitude", which is corrected for distance, :math:`H(\alpha)`, as:

.. math::

    H(\alpha) = V - 5 log(r \Delta),

where :math:`\alpha` is the phase angle, :math:`\Delta` is the topocentric distance, 
`r` is the heliocentric distance, and `V` is the apparent magnitude.

The absolute magnitude `H` can be derived by fitting a function, where the choice of 
form for this function has several options.
Dymock (2007) presents a simpler version with a single parameter `G`, using the equation:

.. math::

    H = H(\alpha) + 2.5 log((1-G)\phi_1(\alpha) +G \phi_2(\alpha)),

where:

.. math::
    \phi_i (\alpha) = exp(-A_i tan(0.5 \alpha)^{Bi}).

In the above equation, 
:math:`A_1` = 3.33, 
:math:`B_1` = 0.63, 
:math:`A_2` = 1.87, and 
:math:`B_2` = 1.22.

However, it is important to understand that there are other options for fitting phase curves.

**MENTION WHAT WAS USED TO GET THE FIT RESULTS IN SSOBJECT, WHICH IS G12 NOT G. DESCRIBE HOW DIFFERENT.**
**IF THEY'RE REALLY DIFFERENT, REPLACE THE ABOVE WITH A DESCRIPTION OF G12, NOT JUST G.**

**Note** that no time domain evolution in object brightness was included in the DP0.3 simulation
(e.g., rotation curves for non-spherical objects, outgassing events).




.. _DP0-3-Portal-3-Step-3:

Step 3. Plot the phase curve for the TNO
========================================

**CANNOT BE DONE WITH SSOBJECTID = -735085100561880491**

**DO NOT USE TNO; USE MBA WITH A GOOD PHASE-CURVE FIT.**

3.1. Execute the following ADQL query to retrieve the r-band magnitudes, phase angles,
heliocentric and topocentric distances, and time of the observations for the TNO.

.. code-block:: SQL 

    SELECT ds.mag, ds.filter, ds.midPointTai, 
    ss.phaseAngle, ss.topocentricDist, ss.heliocentricDist 
    FROM dp03_catalogs.DiaSource AS ds 
    JOIN dp03_catalogs.SSSource AS ss ON ds.diaSourceId = ss.diaSourceId
    WHERE ss.ssObjectId = -735085100561880491
    AND ds.filter = 'r'

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


