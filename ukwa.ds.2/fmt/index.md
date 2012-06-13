---
layout: bootstrap
title: Format Profile
subtitle: UK Web Domain Dataset (1996-2010)
doi: 10.5259/ukwa.ds.2/fmt/1
---

This dataset is a format profile, summarising the data formats (MIME types) contained within all of the HTTP 200 OK responses in the [UK Web Domain Dataset (1996-2010)]({{ site.baseurl }}/ukwa.ds.2/) dataset.

This dataset is hosted in this GitHub repository. You can download it from [here](https://github.com/ukwa/opendata/tree/master/datasets/ukwa.ds.2/fmt), where you'll also find [a full description of the data](https://github.com/ukwa/opendata/tree/master/datasets/ukwa.ds.2/fmt#uk-web-domain-dataset-1996-2010-format-profile).


{% include cite_doi.md %}

{% include jia_cc0.md %}

Example Results
---------------
Here are a few examples of the kinds of trends we have been able to expose by digging into this dataset.

### Popular Image Formats ###
Here we show overall usage trends for a range of popular image formats, illustrating how this dataset can be used to explore how format usage can vary over time.

<center>
<a href="{{ site.baseurl }}/ukwa.ds.2/fmt/images/fmt-image-trends.png"><img src="{{ site.baseurl }}/ukwa.ds.2/fmt/images/fmt-image-trends.png" width="500"/></a>
</center>

This shows that JPEG and GIF usage has remained stable over the years, but that TIFF and particularly XBM images have become increasingly rare. The graph also shows significant gains over the same period for the PNG format, and for the ICO format commonly used to create favicons.

### HTML Version Usage Over Time ###
The following graph shows how the number of resources that used a given version of the HTML format, as a fraction of all HTML resources, by year.

<center>
<a href="{{ site.baseurl }}/ukwa.ds.2/fmt/images/fmt-html-versionspng"><img src="{{ site.baseurl }}/ukwa.ds.2/fmt/images/fmt-html-versions.png" width="500"/></a>
</center>

Each new version comes to dominate the picture, then slowly fade away. Over time, more versions are present in each crawl, with HTML 2.0-4.01 and XHTML 1.0-1.1 all present in the 2010 crawl data.
