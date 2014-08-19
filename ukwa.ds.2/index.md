---
layout: bootstrap
title: JISC UK Web Domain Dataset (1996-2013)
doi: 10.5259/ukwa.ds.2/1
---

In partnership with the [Internet Archive](http://www.archive.org/) and [JISC](http://www.jisc.ac.uk/), we have obtained access to the subset of the Internet Archive's web collection that relates to the UK. The JISC UK Web Domain Dataset (1996-2013) contains all of the resources from the Internet Archive that were hosted on domains ending in '.uk', or that are required in order to render those UK pages.

The collection was deposited with us in two separate traches. The 1996-2010 tranch is composed of 470,466 files, mostly arc.gz, with 4,494 warc.gz files, and the total size is 32TB. The 2011-2013 tranch runs up to April of 2013 (i.e. until the enaction of the UK's Non-Print Legal Deposit legislation), is composed of 67,834 files (24,060 warc.gz files) with a total size of 26TB. The first version of this dataset corresponded to the first tranch, whereas the current version of the dataset includes both tranches.

This dataset cannot be made generally available here, but can be used to generate secondary datasets, and these can be made available under open license terms.

Before interpreting results from this dataset, or any secondary-datasets based upon it, please refer to the [known issues with this dataset](#issues).

Secondary datasets
------------------

* [JISC UK Web Domain Dataset (1996-2010) Format Profile]({{ site.baseurl }}/ukwa.ds.2/fmt)
* [JISC UK Web Domain Dataset (1996-2010) Geoindex]({{ site.baseurl }}/ukwa.ds.2/geo)
* [JISC UK Web Domain Dataset (1996-2010) Host Link Graph]({{ site.baseurl }}/ukwa.ds.2/host-linkage)
* [JISC UK Web Domain Dataset (1996-2013) Crawled URL Index]({{ site.baseurl }}/ukwa.ds.2/cdx)

{% include cite_doi.md %}

Issues
------

This corpus has been assembled from a few different sources, each exploiting different crawl configurations, and this should be borne in mind when attempting to interpret the data.

### Sources ### 
 
The Internet Archive (IA) web collection comes from crawls run by the IA Web Group for different archiving partners, the Web Wide crawls and other miscellaneous crawls run by IA, as well as data donations from Alexa and other companies or institutions. IA is not able to share the names of these companies, but can state that they include a few vertical search engines, and some other Google-like companies. The IA web collection does not include any [CommonCrawl](http://commoncrawl.org/) data, and so neither does this .uk extraction.

### Crawl Policies ###

This range of sources means that comprehensive documentation of the crawl configuration for all crawls is not available. Each of these archiving initiatives has its own crawling policies with regard to revisits, de-duplication, maximum resource or crawl size, etc. For example, the IA Web Group generally imposes a file size limit of 100 MB on records for some partner crawls, and so large objects may be under-represented in the dataset. Indeed, in some cases, [this resource size limit may be as low as 10MB](https://archive.org/about/faqs.php#18).

A significant portion of the data, particularly from the earliest years, comes from [Alexa](http://www.alexa.com/). IA have no visibility into how this data is crawled, except to say that since 2008 this dataset is text only (no images, videos etc.). Note that the Alexa data is embargoed for a period of 6 months, after which IA are able to ingest it into their repositories and make it available via the Wayback Machine.

Before 2008, IA only used the ARC format, although some crawls may have used early forms of de-duplication even before the WARC format provided a standard way to supporting revisit events.

In 2008, IA started to write data into WARC files, while continuing to write ARC files for some more time as well. Again, this was just the Web Group’s policy and the Web Wide crawls run by IA. Other donating institutions may have still been writing ARC files and donating them.

Since 2008, de-duplication was turned on in some select cases. Also, it would be turned off depending on the partner’s needs, or the start of a new calendar year etc. De-duplication was not imposed on a Web Wide scale, but was limited to smaller collections that were being crawled on a regular basis.
 
### Extraction ###

The extracted data contains all captures of .uk in the Internet Archive Web collection (for the given time range). A capture stored in an ARC file was extracted into an ARC file, while a capture that was stored in a WARC file was extracted into a WARC file. No limits on resource sizes were placed in the extraction. 
 
Also, after extracting all these (W)ARCs, IA generated WAT files to find embedded resources (as identified by the original crawl process) not belonging to .uk to be included for extraction as well. A second round of extraction added these embedded resources to this dataset.

In partnership with
-------------------

[<img src="{{ site.baseurl }}/images/jisc-logo-sml.png"/>](http://www.jisc.ac.uk/)
[<img src="{{ site.baseurl }}/images/ia-logo-sml.png"/>](http://www.archive.org/)

