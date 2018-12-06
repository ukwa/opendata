---
title: Geoindex
subtitle: JISC UK Web Domain Dataset (1996-2010)
doi: 10.5259/ukwa.ds.2/geo/1
outputs:
- html
- dcxml
- dcresolve
---

The approximately 2.5 billion 200 OK responses in the 1996-2010 tranche of the [JISC UK Web Domain Dataset]({{ site.baseurl }}/ukwa.ds.2/) dataset have been scanned for geographic references - specifically postcodes. This set of postcode citations, found at particular URLs, crawled at particular times, forms an historical geoindex of the UK web. For more details about how the data was created, its format, and how to use it, see [here](https://github.com/ukwa/opendata/tree/gh-pages/ukwa.ds.2/geo).

The geoindex is composed of some 700,641,549 lines of TSV data, each asserting that a given web page, crawled at a given date, contained one or more references to a given postcode. Uncompressed, this is a total of 61 GB of text, and so care should be taken before downloading or attempting to use this data set.

Download
--------

The data is not hosted on GitHub, as it is far too large. It can be downloaded from [here](http://www.webarchive.org.uk/datasets/ukwa.ds.2/geo/) in a compressed format (total download size, about 8GB).


The structure of the data
-------------------------

Each individual line of data captures the appearence of a given postcode on a given archived web page, as it was seen by a web crawler, visited at a particular time. Note that each combination of postcode, URL and timestamp only appears once, no matter how many times that particular postcode appears in the given page.

The layout of the data is as follows:

> {crawl-timestamp}/{url} {postcode}

i.e. timestamp and the URL are separated by a `/`, and then a _tab character_ separates that from the postcode itself.

<pre>
20080509162138/http://uk.eurogate.co.uk/contact_us	IG8 8HD
20080509162231/http://www.toolfastdirect.co.uk/acatalog/cable_Reels_and_Extensions_240_Volt.html	ML2 7UR
20080509162233/http://www.tgdiecasting.co.uk/supply_chain.htm	DD3 9DL
20080509162252/http://triton-technology.co.uk/php/	NG12 5AW
</pre>

This format is not ideal, but can be parsed fairly easily. For example, by extracting the first column and adding a prefix 
of `http://wayback.archive.org/web/` (i.e. use the form `http://wayback.archive.org/web/{crawl-timestamp}/{url}`) you'll get to the Internet Archive's copy of that page (unless it's blocked by `robots.txt`). Similarly, you can extract the postcode and change to the OS linked-data form, like this: <http://data.ordnancesurvey.co.uk/doc/postcodeunit/LS237BQ>


Unfortunately, at the current time, we've only been able to extract this data for the 1996-2010 chunk of the underlying dataset. We intend to extend this analysis to the remaining years, but are not able to dedicate resources to doing so at the current time.

How the data is packaged
------------------------

The dataset 'homepage' is [here](http://data.webarchive.org.uk/opendata/ukwa.ds.2/geo/), and the data itself can be downloaded from: <https://www.webarchive.org.uk/datasets/ukwa.ds.2/geo/>

To attempt to make the dataset more manageable, we've broken it down into separate files which can be downloaded individually, e.g. `postcode-aa.tsv.bz2`. Note that the `aa` does not mean anything - it's just a way of breaking the full dataset up into chunks. There's also a summary file (`summary-count-year-postcode.tsv.gz`) that contains overall statistics, and a `manifest.sha1` that can be used to validate that the data has been downloaded correctly.

How the data was created
------------------------

This was powered by the regular-expression-based [WARCRegexIndexer](https://github.com/ukwa/webarchive-discovery/blob/master/warc-hadoop-recordreaders/src/main/java/uk/bl/wa/hadoop/regex/WARCRegexIndexer.java). It was run like this:

<pre>
hadoop jar EntityIndexer-0.0.1-SNAPSHOT-job.jar uk.bl.wap.hadoop.regex.WARCRegexIndexer ia.archives.job.1 postcodes "[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}"
</pre>
  
This job goes through the arc.gz or warc.gz files listed in ia.archive.job.1, extract all references to postcodes (using that generic RegEx), and list them to text files under the postcodes directory. 

The lists from separate runs were then combined into a set of separate files based on postcode prefix.

