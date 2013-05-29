---
layout: bootstrap
title: Host Linkage Graph
subtitle: JISC UK Web Domain Dataset (1996-2010)
doi: 10.5259/ukwa.ds.2/host.linkage/1
---

The ~2.5 billion 200 OK responses in the [JISC UK Web Domain Dataset (1996-2010)]({{ site.baseurl }}/ukwa.ds.2/) dataset have been scanned for hyperlinks. For each link, we extract the host that the link targets, and use this to build up a picture of which hosts have linked to which other hosts, over time.

This host-level linkage index summarises the number of links between hosts, in each year. The data format is a slightly unusual, as you can see from this snippet:

<pre>
1996|appserver.ed.ac.uk|portico.bl.uk   1
1996|art-www.acorn.co.uk|portico.bl.uk  1
1996|astra.ich.ucl.ac.uk|portico.bl.uk  1
1996|back.niss.ac.uk|portico.bl.uk  1
1996|beta.bids.ac.uk|portico.bl.uk  2
1996|blaiseweb.bl.uk|blaiseweb.bl.uk    4
1996|bonsai.iielr.dmu.ac.uk|portico.bl.uk   4
</pre>

There are two tab-separated columns. The first contains three bar-separated fields: the crawl year, the source host, and the target host. The second contains the number of linking URLs. Therefore, the first line:

<pre>
1996|appserver.ed.ac.uk|portico.bl.uk   1
</pre>

represents an assertion that, from the data crawled in 1996, we found one URL on the 'appserver.ed.ac.uk' host that contained a hyperlink to a resource held on 'portico.bl.uk'.

Download
--------

This large dataset cannot be hosted on GitHub. It can be downloaded from [here](http://www.webarchive.org.uk/datasets/ukwa.ds.2/linkage/) instead, in a compressed format (total download size, about 19GB).

Usage
-----

Perhaps the simplest way to exploit this dataset is via the zgrep command. This can be used to extract a subset of the data, pertaining to a particular host or domain. As an example, we have extracted all of the links relating to the British Library website, like this:

    % zgrep "bl.uk" host-linkage.tsv.gz | sort > bl-uk-linkage.tsv

This subset of the data has also been [made available for download](http://www.webarchive.org.uk/datasets/ukwa.ds.2/linkage/).


{% include cite_doi.md %}

{% include jia_cc0.md %}
