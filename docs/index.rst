mast-aladin
===========

``mast-aladin`` is an Aladin-lite widget for Jupyter notebooks built on top of
`ipyaladin <https://github.com/cds-astro/ipyaladin>`_ for use with 
`MAST <https://mast.stsci.edu/>`_ data products from the Space Telescope Science
Institute. 

Key Features
************

* **Runs on the** `Roman Research Nexus <https://roman.science.stsci.edu/hub/login?next=%2Fhub%2F>`_,
  or on your local machine in a Jupyter notebook
* **Browse all-sky imaging survey atlases** from surveys
  across the spectrum including SDSS, Pan-STARRS, WISE, GALEX, and more
* **Interactivity** via the familiar Aladin-Lite UI *and* via a Python API
* Plot **observation footprints** and **source catalogs** from MAST

.. .. raw:: html

..    <div id="aladin-lite-div" style="width: 500px; height: 400px"></div>
..    <script type="text/javascript" src="https://aladin.cds.unistra.fr/AladinLite/api/v3/latest/aladin.js" charset="utf-8"></script>

..    <script type="text/javascript">
..    // Initialize Aladin Lite inside the div
..    var aladin = A.aladin('#aladin-lite-div', {
..       fov: 360,
..       projection: "AIT",
..       cooFrame: 'equatorial',
..       showCooGrid: true,
..       survey: "https://stpubdata.s3.us-east-1.amazonaws.com/mast/skybackgrounds/DSSColor"
..    });
..    </script>


Contents
********

.. toctree::
   :maxdepth: 2

   installation
   getting_started
   performance_catalog
   api
