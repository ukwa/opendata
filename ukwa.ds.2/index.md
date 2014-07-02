---
layout: bootstrap
title: JISC UK Web Domain Dataset (1996-2010)
doi: 10.5259/ukwa.ds.2/1
---

In partnership with [archive.org](http://www.archive.org/) and JISC, we have obtained access to the subset of the Internet Archive's web collection that relates to the UK. The JISC UK Web Domain Dataset (1996-2010) contains all of the resources from the Internet Archive that were hosted on domains ending in '.uk', or that are required in order to render those UK pages.

It is composed of 470466 files, mostly arc.gz, with 4494 warc.gz. Total size: 32TB, Average 71 MB per archive file, but this is very variable because the crawler does not split resources across archives.

This dataset cannot be made generally available, but can be used to generate secondary datasets, and these can be made available under open license terms.

Before interpreting results from this dataset, or any secondary datasets based upon it, please refer to the [known issues with this dataset][#Issues] (below).

Secondary datasets
------------------

* [JISC UK Web Domain Dataset (1996-2010) Format Profile]({{ site.baseurl }}/ukwa.ds.2/fmt)
* [JISC UK Web Domain Dataset (1996-2010) Geoindex]({{ site.baseurl }}/ukwa.ds.2/geo)
* [JISC UK Web Domain Dataset (1996-2010) Host Link Graph]({{ site.baseurl }}/ukwa.ds.2/host-linkage)

{% include cite_doi.md %}

In partnership with
-------------------

[<img src="{{ site.baseurl }}/images/jisc-logo-sml.png"/>](http://www.jisc.ac.uk/)
[<img src="{{ site.baseurl }}/images/ia-logo-sml.png"/>](http://www.archive.org/)


Issues
------

This corpus has been assembled from a range of sources, each exploiting different crawl configurations, and this should be borne in mind when attempting to interpret the data.

### Sources ### 
 
The Internet Archive (IA) web collection comes from a variety of sources. The crawls run by the IA Web Group for different archiving partners, the Web Wide crawls and other misc crawls run by IA, as well as data donations from Alexa and other companies and institutions. IA is not able to share the names of these companies, but can state that they include a few vertical search engines, and some other Google-like companies. The IA collection does not include any CommonCrawl data, and so neither does this .uk extraction.

### Crawl Policies ###

This complex array of sources means that comprehensive documentation of the crawl configuration for all crawls is not available. Each of these archiving initiatives has its own crawling policies with regard to revisits, de-duplication, maximum capture size etc. For example, the IA Web Group generally imposes a file size limit of 100 MB on records for some partner crawls. 

A significant portion of the data, particularly from the earliest years, some from Alexa. IA have no visibility into how this data is crawled. This data is also embargoed for a period of 6 months, after which we are able to ingest it into our repositories and make available via the Wayback Machine.

Before 2008, IA only used the ARC format, although some crawls may have used early forms of de-duplication even before the WARC format provided a standard way of supporting revisit events.

In 2008, IA started to write data into WARC files, while continuing to write data into ARC files for some more time as well. Again, this was just the Web gGroup’s policy and the Web Wide crawls run by IA. Other donating institutions could have still been writing ARC files and donating them.

Since 2008, de-duplication was turned on some select cases. Also, it would be turned off depending on the partner’s needs, or the start of a new calendar year etc. De-duplication was not imposed on a Web Wide scale, but limited to smaller collections that were being crawled on a regular basis.
 
Also, since 2008, Alexa is text only data (no images, videos etc.).

### Extraction ###

The extracted data contains all captures of .uk in the Archive (for the given time range). A capture stored in an ARC file was extracted into an ARC file, while a capture that was stored in a WARC file was extracted into a WARC file. No limits on resource sizes were placed in the extraction. 
 
Also, after extracting all these (W)ARCs, we generated WAT files to find embedded resources not belonging to .uk to be included for extraction as well. A second round of extraction copied over these embedded resources.


