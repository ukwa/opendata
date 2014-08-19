---
layout: bootstrap
title: Geoindex
subtitle: JISC UK Web Domain Dataset (1996-2010)
doi: 10.5259/ukwa.ds.2/geo/1
---

The ~2.5 billion 200 OK responses in the (1996-2010) tranch of the [JISC UK Web Domain Dataset]({{ site.baseurl }}/ukwa.ds.2/) dataset have been scanned for geographic references - specifically postcodes. This set of postcode citations, found at particular URLs, crawled at particular times, forms an historical geoindex of the UK web. For more details about how the data was created, its format, and how to use it, see [here](https://github.com/ukwa/opendata/tree/master/datasets/ukwa.ds.2/geo).

The geoindex is composed of some 700,641,549 lines of TSV data, each asserting that a given web page, crawled at a given data, contained one or more references to a given postcode. Uncompressed, this is a total of 61 GB of text, and so care should be taken before downloading or attempting to use this data set.

Download
--------

The data is not hosted on GitHub, as it is far too large. It can be downloaded from [here](http://www.webarchive.org.uk/datasets/ukwa.ds.2/geo/) in a compressed format (total download size, about 8GB).


{% include cite_doi.md %}

{% include jia_cc0.md %}
