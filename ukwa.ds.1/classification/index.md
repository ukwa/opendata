---
layout: bootstrap
title: Website Classification Dataset
subtitle: UK Selective Web Archive
doi: 10.5259/ukwa.ds.1/classification/1
---

The entire [selective archive]({{ site.baseurl }}/ukwa.ds.1/) is manually curated, including classification of sites into a two-tiered subject hierarchy. We have made this manually-generated classification information available as an [open dataset, in tab-separated column format]({{ site.baseurl }}/ukwa.ds.1/classification/classification.tsv). The structure of the data is as follows:

<pre>
Primary Category        Secondary Category      Title   URL
Arts &amp; Humanities       Architecture    68 Dean Street  http://www.sixty8.com/
Arts &amp; Humanities       Architecture    Abandoned Communities   http://www.abandonedcommunities.co.uk/
...
</pre>

Use Cases
---------
We are particularly interested in understanding whether high-level metadata like this can be used to train an appropriate automatic classification system so that we might use this manually generated dataset to partially automate the categorisation of our larger archives.

{% include cite_doi.md %}

{% include ukwa_cc0.md %}

