---
title: Crawled URL Index
subtitle: JISC UK Web Domain Dataset (1996-2013)
doi: 10.5259/ukwa.ds.2/cdx/1
---

In order to enable access to web archives, we use [CDX files](https://archive.org/web/researcher/cdx_file_format.php) to act as indexes so that we can look up which ARC or WARC files contain which URLs and responses. 

The original CDX files were generated for us by the Internet Archive, with one CDX file for each ARC or WARC file. This makes it easy for us to manage those files, but it is not very convenient for researchers to have to download and deal with over half a million separate small files. Therefore, we have processed those CDX files and aggregated the  data into 18 separate CDX files -- one per year of crawling activity. Please note that the individual CDX files are not sorted.

Schema
------

There are a few variations on the CDX format, but for this dataset, the CDX lines look like this:

<pre>
vanguard.ntu.ac.uk/ 19961018104851 http://vanguard.ntu.ac.uk:80/ text/html 200 2TAC6RS2DMTHHFVWCSDHNL6W6RIIOQIV - 34954008 DOTUK-HISTORICAL-1996-2010-GROUP-AA-XABEGS-20110428000000-00000.arc.gz
</pre>

These space-separated fields can be interpreted as follows:

vanguard.ntu.ac.uk/
: This is the canonicalized version of the URL (the 'key' of the index)

19961018104851
: Time of capture (in `YYYYMMDDHHMMSS` format)

http://vanguard.ntu.ac.uk:80/
: The actual URL crawled

text/html
: The `Content-Type` (as returned in the original server response)

200
: HTTP status code reported by the server

2TAC6RS2DMTHHFVWCSDHNL6W6RIIOQIV
: Checksum (this is the Base32 encoded form of the SHA1 digest of the response payload).

-
: This is the redirect URL (i.e. the `Location` header, populated only for 3** responses, "-" for others).

34954008 
: This is the offset of the record in the WARC/ARC file.

DOTUK-HISTORICAL-1996-2010-GROUP-AA-XABEGS-20110428000000-00000.arc.gz
: This is the WARC/ARC which contains the record (coupled with the above offset, used to determine the exact location).


Download
--------

This large dataset cannot be hosted on GitHub. It can be downloaded from [here](http://www.webarchive.org.uk/datasets/ukwa.ds.2/cdx/) instead, as compressed files containing the CDX data for each year of crawler activity.


{% include cite_doi.md %}

{% include jia_cc0.md %}
