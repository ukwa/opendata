UK Web Domain Dataset (1996-2010) Geoindex
==========================================

The structure of the data
-------------------------

Each individual line of data captures the appearence of a given postcode on a given archived web page, as it was seen by a web crawler that visited at a particular time. Note that each combination of postcode, URL and timestamp only appears once, no matter how many times that particular postcode appears in the given page.

The layout of the data is as follows:

> {crawl-timestamp}/{url} _tab_ {postcode}

i.e. timestamp and the URL are separated by a `/`, and then a tab character separates that from the postcode itself.

<pre>
20080509162138/http://uk.eurogate.co.uk/contact_us	IG8 8HD
20080509162231/http://www.toolfastdirect.co.uk/acatalog/cable_Reels_and_Extensions_240_Volt.html	ML2 7UR
20080509162233/http://www.tgdiecasting.co.uk/supply_chain.htm	DD3 9DL
20080509162252/http://triton-technology.co.uk/php/	NG12 5AW
</pre>

This format is not ideal but can be post-processed to link to elsewhere, e.g. prefix the first column 
with http://wayback.archive.org/web/ and you'll get to IAs version. Or change the postcode into the OS
linked data form, like http://data.ordnancesurvey.co.uk/doc/postcodeunit/SO164GU


How the data was created
------------------------

This was powered by the regular-expression-based [WARCRegexIndexer](https://github.com/ukwa/webarchive-discovery/blob/master/warc-hadoop-indexer/src/main/java/uk/bl/wa/hadoop/regex/WARCRegexIndexer.java). It was run like this:

<pre>
hadoop jar EntityIndexer-0.0.1-SNAPSHOT-job.jar uk.bl.wap.hadoop.regex.WARCRegexIndexer ia.archives.job.1 postcodes "[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}"
</pre>
  
This job goes through the arc.gz or warc.gz files listed in ia.archive.job.1, extract all references to postcodes (using that generic RegEx), and list them to text files under the postcodes directory. 

The lists from separate runs were then combined into a set of separate files based on postcode prefix.


License
-------
<p xmlns:dct="http://purl.org/dc/terms/">
  <a rel="license"
     href="http://creativecommons.org/publicdomain/zero/1.0/">
    <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
  </a>
  <br />
  To the extent possible under law,
  <a rel="dct:publisher"
     href="http://data.webarchive.org.uk/opendata/ukwa.ds.2/">
    <span property="dct:title">The Project Partners</span></a>
  have waived all copyright and related or neighboring rights to
  <span property="dct:title">The UK Web Domain Dataset (1996-2010) Geoindex</span>.
</p>


Citing this dataset
-------------------
If you do wish to cite this dataset, please this DOI: [**10.5259/ukwa.ds.2/geo/1**](http://dx.doi.org/10.5259/ukwa.ds.2/geo/1).
