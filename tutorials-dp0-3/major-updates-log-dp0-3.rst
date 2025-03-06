.. Review the README on instructions to contribute.
.. Review the style guide to keep a consistent approach to the documentation.
.. Static objects, such as figures, should be stored in the _static directory. Review the _static/README on instructions to contribute.
.. Do not remove the comments that describe each section. They are included to provide guidance to contributors.
.. Do not remove other content provided in the templates, such as a section. Instead, comment out the content and include comments to explain the situation. For example:
    - If a section within the template is not needed, comment out the section title and label reference. Do not delete the expected section title, reference or related comments provided from the template.
    - If a file cannot include a title (surrounded by ampersands (#)), comment out the title from the template and include a comment explaining why this is implemented (in addition to applying the ``title`` directive).

.. This is the label that can be used for cross referencing this file.
.. Recommended title label format is "Directory Name"-"Title Name" -- Spaces should be replaced by hyphens.
.. _Tutorials-Examples-DP0-3-Major-Updates-Log:
.. Each section should include a label for cross referencing to a given area.
.. Recommended format for all labels is "Title Name"-"Section Name" -- Spaces should be replaced by hyphens.
.. To reference a label that isn't associated with an reST object such as a title or figure, you must include the link and explicit title using the syntax :ref:`link text <label-name>`.
.. A warning will alert you of identical labels during the linkcheck process.


#############################
Log of Major Tutorial Updates
#############################

All tutorial headers contain the date "last verified to run", and the version of the
LSST Science Pipelines that it was verified to run with. 


How to find version histories
=============================

Notebook tutorials
------------------

All Jupyter Notebook tutorial headers contain the date "last verified to run".
If the date in the file you are using does not match the date shown in that file in `the "main" branch of the tutorial-notebooks repository <https://github.com/lsst/tutorial-notebooks>`_, your version is out of date.

The history of a given tutorial can be accessed in GitHub by going to 
`the tutorial-notebooks repository <https://github.com/lsst/tutorial-notebooks>`_,
clicking on its file name and then clicking on "history" (near upper-right).


Portal and command line tutorials
---------------------------------

All tutorials for the Portal aspect, and for the command line (Notebook Aspect)
are kept in the `dp0-3_lsst_io repository <https://github.com/lsst/dp0-3_lsst_io>`_.

The full history for any given tutorial can be accessed via GitHub by going to the tutorial of interest in the repo
(e.g., the `DP0.2 beginner Portal tutorial <https://github.com/lsst/dp0-2_lsst_io/blob/main/tutorials-examples/portal-beginner.rst>`_), 
and clicking on "history" (near upper-right).


Major Updates Log
=================

Mar 6 2025
----------

The recommended image of the RSP at data.lsst.cloud was bumped to Weekly 2025_09.

All Jupyter Notebook tutorials were migrated to the new repository `lsst/tutorial-notebooks <https://github.com/lsst/tutorial-notebooks>`_.

The new tutorial notebooks repository no longer has a ``/data`` folder.
Instead, input data for notebook tutorials is stored in the new Git LFS repository `lsst/tutorial-notebooks-data <https://github.com/lsst/tutorial-notebooks-data>`_,
which is already cloned into the ``/project`` directory and accessed by the tutorials (users do not need to obtain the contents of ``/data`` themselves).

The tutorial notebook delivery mechanism in the Notebook Aspect of the RSP also changed.
With the old way, latest version of all notebooks were copied as read-only files into the folder ``/notebooks/tutorial-notebooks/`` in
all users' home directories whenever a new Notebook server was instantiated.
With the new way, users have a new menu bar item "Tutorials" which provides a drop down menu of all
the tutorials in the `tutorial-notebooks repository <https://github.com/lsst/tutorial-notebooks>`_.
Users select the desired tutorial, and a writeable version automatically opens and is saved into
the folder ``/notebooks/tutorials/``.

Dec 19 2024
-----------

The recommended image of the RSP at data.lsst.cloud was bumped to Weekly 2024_50,
and some DP0.3 tutorials had minor updates (addition of captions for all plots,
and a switch from synchronous to asynchronous TAP queries).


Nov 22 2024
-----------

Released new intermediate-level tutorial notebook 07 on interactive catalog
visualization with Bokeh, Holoviews, and Datashader.

Oct 31 2024
-----------

The recommended image of the RSP at data.lsst.cloud was bumped to Weekly 2024_42
(but this prompted no major changes to any tutorials).

Sep 19 2024
-----------

The recommended image of the RSP at data.lsst.cloud was bumped to Weekly 2024_37.

Aug 22 2024
-----------

The recommended image of the RSP at data.lsst.cloud was bumped to Weekly 2024_32.

Jun 3 2024
----------

Released new beginner-level tutorial notebook 06 on user-uploaded tables in TAP.

May 2 2024
----------

The recommended image of the RSP at data.lsst.cloud was bumped to Weekly 2024_16.

Apr 30 2024
-----------

Released one introductory-level :ref:`DP0-3-Tutorials-ES`. 

Apr 24 2024
-----------

DP0.3 Notebook tutorial 05 on near-Earth objects (NEOs) released.

Feb 1 2024
-----------

The recommended image of the RSP at data.lsst.cloud was bumped to Weekly 2024_04.

Jan 30 2024
-----------

The DP0.3 notebook tutorials 04a and 04b on phase curves have been updated to use the ``sbpy`` package, 
which is now included in the default user environment.

Dec 30 2023
-----------

Portal tutorials on phase curves (04) and user-uploaded tables (05) released.

Nov 30 2023
-----------

The recommended image of the RSP at data.lsst.cloud was bumped to Weekly 2023_47.

Sep 28 2023
-----------

DP0.3 Notebook tutorials 04a and 04b on phase curves released.

Sep 25 2023
-----------

DP0.3 Portal tutorial 03 on trans-Neptunian objects (TNOs) released.

Sep 21 2023
-----------

The recommended image of the RSP at data.lsst.cloud was bumped to Weekly 2023_37.

Sep 01 2023
-----------

DP0.3 notebook tutorial 03 on Trans-Neptunian Objects is released.

Aug 04 2023
-----------

DP0.3 notebook tutorial 02 on the Main Belt Asteroids is released.


July 31 2023
------------

First release of DP0.3 introductory tutorials: Portal tutorials 01 and 02, and Notebook tutorial 01.

