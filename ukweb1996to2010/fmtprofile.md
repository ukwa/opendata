---
layout: default
title: UK Domain Dark Archive (1996-2010) Format Profile
---

This data set captures information about the data formats used by the resources in the UK Domain Dark Archive.  As well as collecting the MIME type delivered by the server, we have also run two format identification tools over the content of each HTTP 200 OK response. These tools were Apache Tika and DROID. All three MIME types are collected, along with the year the resource was crawled. These four pieces of information are treated as a 'key' for the resource, and the number of resources with that key are counted up, over the entire dataset. The result is output as tab separated data. For full details see, the Nanite codebase, tag v.0.1.1 was used to create this dataset.

For example, this line:
<pre>
application/x-csv	text/plain	application/octet-stream	2009	1
</pre>
means that, of all the resources crawled in 2009, there was one item that the server declared to be CSV, but which Tika determined to be plain text, and which DROID could not identify at all.

### Citing this dataset ###
If you do wish cite this dataset, please use:

DOI: 10.5259/ukwa.ds.2.fmt/1

### License ###

<p xmlns:dct="http://purl.org/dc/terms/">
  <a rel="license"
     href="http://creativecommons.org/publicdomain/zero/1.0/">
    <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
  </a>
  <br />
  To the extent possible under law,
  <a rel="dct:publisher"
     href="http://www.webarchive.org.uk/">
    <span property="dct:title">The UK Web Archive</span></a>
  has waived all copyright and related or neighboring rights to
  <span property="dct:title">The UK Web Domain Dataset (1996-2010) Format Profile</span>.
</p>


