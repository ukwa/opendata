Tools
=====

Format Profile Tools
--------------------

The `fmt-tools` folder contains some scripts for processing the Format Profile data, as described [here](../datasets/ukwa.ds.2/fmt)


DataCite
--------

Scripts for updating the relevant DataCite metadata.

Previously, I updated metadata using

    $ cirneco metadata post doi.xml
    
and for the URL

    $ python ...path.to.tools.../datacite/post-doi.py $MDS_USERNAME $MDS_PASSWORD doi.resolve
    
