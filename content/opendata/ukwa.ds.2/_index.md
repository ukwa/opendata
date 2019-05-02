---
title: JISC UK Web Domain Dataset
doi: 10.5259/ukwa.ds.2/1
weight: 2
description: "UK web resources from the Internet Archive's collections, held on behalf of JISC. Covers the pre-Legal Deposit period from 1996 ro April 2013."
date: 1996-01-01
layout: dataset
contributors:
- title: The UK Web Archive
  email: web-archivist@bl.uk
  path: https://www.webarchive.org.uk/
  role: publisher
licenses:
- title: UK Non-Print Legal Deposit Regulations
  path: https://www.legislation.gov.uk/ukdsi/2013/9780111533703/contents
outputs:
- html
- dcxml
- dcresolve
---

In partnership with the [Internet Archive](http://www.archive.org/) and [JISC](http://www.jisc.ac.uk/), we have obtained access to the subset of the Internet Archive's web collection that relates to the UK. The JISC UK Web Domain Dataset (1996-2013) contains all of the resources from the Internet Archive that were hosted on domains ending in '.uk', or that are required in order to render those UK pages.

The collection was deposited with us in two separate tranches. The 1996-2010 tranche is composed of 470,466 files (mostly arc.gz) and the total size is 32TB. The 2011-2013 tranche runs up to April of 2013 (i.e. until the enaction of the UK's Non-Print Legal Deposit legislation), is composed of 203,502 files with a total size of 30TB. The first version of this dataset corresponded to the first tranche, whereas the current version of the dataset includes both tranches.

This dataset cannot be made generally available here, but can be used to generate secondary datasets, and these can be made available under open license terms.

Before interpreting results from this dataset, or any secondary-datasets based upon it, please refer to the [known issues with this dataset](#issues).

Secondary datasets
------------------

* [JISC UK Web Domain Dataset (1996-2010) Format Profile](./fmt)
* [JISC UK Web Domain Dataset (1996-2010) Geoindex](./geo)
* [JISC UK Web Domain Dataset (1996-2010) Host Link Graph](./host-linkage)
* [JISC UK Web Domain Dataset (1996-2013) Crawled URL Index](./cdx)


Issues
------

This corpus has been assembled from a few different sources, each exploiting different crawl configurations, and this should be borne in mind when attempting to interpret the data.

### Sources ###
 
The Internet Archive (IA) web collection comes from crawls run by the IA Web Group for different archiving partners, the whole-web crawls and other miscellaneous crawls run by IA, as well as data donations from Alexa and other companies or institutions. IA is not able to share the names of these companies, but can state that they include a few vertical search engines, and some other Google-like companies. The IA web collection does not include any [CommonCrawl](http://commoncrawl.org/) data, and so neither does this extraction of UK domains.

### Crawl Policies ###

This range of sources means that comprehensive documentation of the crawl configuration for all crawls is not available. Each of these archiving initiatives has its own crawling policies with regard to revisits, de-duplication, maximum resource or crawl size, etc. For example, the IA Web Group generally imposes a file size limit of 100 MB on records for some partner crawls, and so large objects may be under-represented in the dataset. Indeed, in some cases, [this resource size limit may be as low as 10MB](http://webarchive.loc.gov/all/20110813043651/http://www.archive.org/about/faqs.php#18). In general, these crawls obeyed robots.txt, and so many sites may be missing or patchy for that reason. Also, as robots.txt files are usually written with search crawlers in mind, they often block non-textual resources like embedded images or stylesheets, biasing the collection towards textual and HTML resources.

A significant portion of the data, particularly from the earliest years, comes from [Alexa](http://www.alexa.com/). IA have no visibility into how this data is crawled, except to say that since 2008 this dataset is text only (no images, videos etc.). Note that [the Alexa data](https://archive.org/details/alexacrawls) is embargoed for a period of 6 months, after which IA are able to ingest it into their repositories and make it available via the Wayback Machine.

Before 2008, IA only used the [ARC format](https://archive.org/web/researcher/ArcFileFormat.php), although some crawls may have used early forms of de-duplication even before the [WARC format](https://www.loc.gov/preservation/digital/formats/fdd/fdd000236.shtml) provided a standard way to supporting revisit events.

In 2008, IA started to write data into WARC files, while continuing to write ARC files for some more time as well. Other donating institutions may have still been writing ARC files and donating them.

Since 2008, de-duplication was turned on in some select cases. Also, it would be turned off depending on the partner’s needs, or the start of a new calendar year etc. De-duplication was not imposed on a web-wide scale, but was limited to smaller collections that were being crawled on a regular basis.

Like most web archives, the limitations of the crawling process mean that highly dynamic or form-driven sites will not be archived completely. Embedded objects like Flash, Java Applets, video and audio files and so on will generally not be archived correctly. Also, most web crawlers follow long chains of links from their initial starting points, and so the regularity with which sites are visited is driven largely by how many links refer to them, rather than being an explicit curatorial request.
 
### Extraction ###

The extracted data contains all captures of .uk resources in the Internet Archive Web collection (for the given time range). A capture stored in an ARC file was extracted into an ARC file, while a capture that was stored in a WARC file was extracted into a WARC file. No limits on resource sizes were placed in the extraction. 
 
After extracting all these (W)ARCs for the period 1996 to 2010, IA generated [WAT](https://webarchive.jira.com/wiki/spaces/Iresearch/pages/14484029/Web+Archive+Transformation+WAT+Specification+Utilities+and+Usage+Overview) files to find embedded resources (as identified by the original crawl process) not belonging to .uk to be included for extraction as well. A second round of extraction added these embedded resources to this dataset.

Later the process was repeated for the 2011 to April 2013 tranche of data. In this case the whole of the extraction was performed at once, so this data is not split by phase.

### Summary Statistics ###

Tranche 2011-201304 contains 203,502 blobs, 30,036,052,322,986 bytes  (24,060 warc.gz files)

Tranche 1996-2010 contains 4,494 warc.gz files


### Data Quality Problems ###

Tranche 2011-201304 appears to contain an accidentally truncated WARC.GZ file:

    2011-201304/part-04/warcs/DOTUK-HISTORICAL-2011-201304-WARCS-PART-00072-801000-000000.warc.gz
    
If you attempt to use this file, you'll get a *Unexpected end of ZLIB input stream* error. Based on the MD5 hashes inventory on the original drives, this file appears to be exactly as it was supplied to us.


In partnership with
-------------------

[JISC] (http://www.jisc.ac.uk/)

[Internet Archive] (http://www.archive.org/)



