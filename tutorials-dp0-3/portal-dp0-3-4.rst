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

**Last verified to run:** November 15, 2023

**Targeted learning level:** Beginner


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

TBD: Why can't one do this with DP0.2 searches?

1.2 In the "Enter Constraints" box, under "spatial constraints" click on the multi-object button. A window will pop up to allow one to upload a text file containing ra and dec coordinates for sources of interest. The format of this catalog must be one of those listed (IPAC, CSV, TSV, VOTABLE, or FITS table format). For this example, we will use an ascii catalog with columns of RA and Dec in tab separated format (TSV). Other columns can also be present in the file, but note that the header names and columns must not have multiple spaces or tabs. The uploader is agnostic about header labels, because you can choose which columns to use later (i.e. ra and dec can be labeled in whatever way you like). Click the browse button to find the file on your machine and click the upload button.

`link catalog for user upload <https://github.com/lsst/dp0-3_lsst_io/blob/tickets/PREOPS-3619/_static/portal_tut04_useruploadcat1.cat>`_

1.3 After uploading, the window will show a list of the columns it found, named according to the header. Make sure that the ra and dec columns in your file are labeled "ra" and "dec" and are displayed in the list. Then click the "Load Table" button.

1.4 If the table loaded the ra and dec correctly, you should see the table filename displayed next to "Upload Table", and listed next to "position columns" should show "ra, dec (from the uploaded table)".

.. figure:: /_static/portal_tut04_step01a.png
    :width: 600
    :name: portal_tut04_step01a
    :alt: A screenshot of the search query if the user-supplied catalog has uploaded and identified the correct columns for search.
A screenshot of the search query if the user-supplied catalog has uploaded and identified the correct columns for search.

TBD: Why can't you manually specify the header name of the ra/dec columns if they don't comply with the expected format?

1.5 Still under the "spatial" constraint inputs but below where the table was uploaded, next to "position columns", the user must indicate which of the DP0.3 catalog columns to use for the spatial matching (i.e. from among the header names listed to the right below "output column selection and constraints". Here, click the arrow next to "position columns" and enter "ra" into the "Lon column" and "dec" into the "Lat column". Leave the search radius at the default of 10 arcseconds.

1.6 For a first look, lets ignore the "Temporal" constraint and make sure the box is unchecked. This search will return whether any moving object was ever detected within a search radius of 10 arcseconds of these locations in the uploaded table. 

.. figure:: /_static/portal_tut04_step01b.png
    :width: 600
    :name: portal_tut04_step01b
    :alt: A screenshot of the search query if the user-supplied catalog has uploaded and identified the correct columns for search.
A screenshot of the search query result. The multiple observations of 3 SSObjects from the user-uploaded table can be seen as the clustered objects

1.7 Now, hit the back button and return to the search query page. For a second example, now also set a "Temporal" constraint for the search by clicking the box. We are now interested to know if there were there moving objects identified in the survey at these coordinates on a specific night (for this example, we will pick a day for which we know this is the case from the mjd column of the user-supplied catalog). Click the Temporal box and make sure the "temporal column" box contains "midPointMjdTai" (referring again to the column in the DP0.3 DiaObject table to use for temporal matching). Click the MJD specification and enter an MJD (62000, a day that we know one of our sample objects was observed in the catalog).

1.8 It can be useful to save the search for later. In this case it can be automated with search query commands that are output by the "populate and edit ADQL query" button. Repeat Step 7, but instead of hitting the "search" button, hit the "populate and edit ADQL" button on the bottom right. This will take you to "advanced ADQL interface" where you can see the reproducible search code snippet to perform the search (e.g. in a notebook) on the right. In the schema browser on the left you can see the user-supplied catalog as a searchable table under TAP_UPLOAD. 

.. figure:: /_static/portal_tut04_step01c.png
    :width: 600
    :name: portal_tut04_step01c
    :alt: A screenshot of the "advanced ADQL interface".
A screenshot of the "advanced ADQL interface" which allows one to see the ADQL search corresponding to the one entered into the portal user interface, for future use with a TAP service.


.. _DP0-3-Portal-4-Step-2:

Step 2. ADQL table join with user-uploaded list of SSObject IDs
======================================================

2.1 Return to the main portal user interface, and unclick the spatial and temporal boxes. Make sure the box labeled "Object ID search" is clicked. Clicking the down arrow then gives access to the upload button to supply a catalog containing IDs. Click the "add" button and navigate on your machine to the catalog of IDs to be used. Then click the "load table" button. 

`link catalog for user upload <https://github.com/lsst/dp0-3_lsst_io/blob/tickets/PREOPS-3619/_static/portal_tut04_useruploadcat2.cat>`_

2.2 Back on the main user interface click the arrow next to "uploaded object id" where it says "unset". This will lower the option to select which column to use as the ID. Click the magnifying glass near "ID" and in the window that pops open, select the "SSObjectID" header keyword from the table you uploaded, and hit OK. The object ID box should now contain ssObjectId (or whatever header label is used for ID in the user suppled catalog). 


2.3 Now go below to the "object ID (from table)" section and click the arrow to open the box that allows one to specify which type of ID in the catalog to the right to match on. The default will say ccdVisitId, but for this exercise we will instead match on SSObjectId, since we want to retrieve information for specific solar system bodies identififed by their unique identifier. Click the magnifying glass to open a navigation window to choose which ID from the DP0.3 table to use, and select SSObjectId.


.. figure:: /_static/portal_tut04_step02a.png
    :width: 600
    :name: portal_tut04_step02a
    :alt: A screenshot .
A screenshot of the portal user interface demonstrating the view after correctly uploading a table of IDs and identifying how to match to the DP0.3 catalog.

2.4 Hit the search button. Note: searching on IDs without a spatial constraint included can take several minutes since the database is [parsed by area TBD correct description]. In this example we search for 2 unique SSObjects from the user-supplied table, and the output looks as in the below screenshot. You can see the moving source observations for both sources over the 10yr survey lifetime. To view each object separately, go to the table column SSObjectID and you can filter by one ID or the other to plot single objects. 

.. figure:: /_static/portal_tut04_step02b.png
    :width: 600
    :name: portal_tut04_step02a
    :alt: A screenshot .
A screenshot of the portal user interface after searching the 10 year catlaog for 2 unique solar system objects based on their SSObjectIDs.

2.5 Now lets use the ADQL interace to perform the join on SSObjectID between the uploaded table and the DP0.3 table. Start over at the main portal interface and click the upper right botton called "Edit ADQL". It will take you to a page where you can manually type in the ADQL query. Make sure the button is clicked that says "Insert fully-qualified column names (recommended for table joins)". Click the "Add" button and navigate to your catalog (Here you can use the above catalog of IDs from earlier in Step 2). Once loaded, you should see it appear in the schema browser on the left under the "TAP_UPLOAD" folder. 

2.6 Add the uploaded table to the ADQL query build. Click the + box next to TAP_UPLOAD in the browser schema, and click the "upload_table" folder. It should populate the ADQL code to search the catalog that was uploaded to the right (clicking search now will just return the list of IDs contained in the catalog). Then, you can type in your query to search the DP0.3 catalogs for objects that match ssObjectIds, using a JOIN:

SELECT tab.ssObjectId_user, sso.ssObjectId, sso.numObs

FROM TAP_UPLOAD.upload_table as tab

JOIN dp03_catalogs_10yr.SSObject as sso 

ON tab.ssObjectId_user = sso.ssObjectId 

.. figure:: /_static/portal_tut04_step02c.png
    :width: 600
    :name: portal_tut04_step02c
    :alt: A screenshot .




.. _DP0-3-Portal-4-Step-3:

Step 3. More advanced stuff
============================================



        
- first do a query to generate results that include list of SSObject Id of interest

3.1 Back on the main query page, enter some example coordinates (e.g. 314.9407129, -31.5520653 from the first table we uploaded in Section 1) and search in a 100 arcsec radius cone, to retrieve a list of SSObjectIds. Do not delete the search results (they will stay active), but go back to the main query UI page by clicking the "RSP TAP Search" button in the top left.

- then return to query, use the "Loaded Table" option

3.2 Then, click the "multi-object" button under the spatial constraints area of the UI. A new window will open to interface with loaded tables. Click the "Loaded Tables" tab at the top of the pop-up, where you will see a list of the tables that have been uploaded by the user (which remain loaded in the system for timeframe TBD). 

[This does not seem right, and not sure what is purpose of going back to original search to identify some SSObjects, and also uploading the list of SSObjects from the user supplied table]

- do not delete query results first!! must keep them as "active result"

- do a new query (e.g., on SSSource) to get data for the SSOjbect Ids of interest identified with the first query

3.3 
 

.. _DP0-3-Portal-4-Step-4:

Step 4.  Exercises for the learner 
==================================

