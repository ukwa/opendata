---
layout: bootstrap
title: Wayback
---

TBA

* http://inkdroid.org/journal/2012/05/03/way-way-back/




APIs and Data Services
--------------------------------

Traditionally, the online presence of most archives, archives and museums have focussed on delivering access to individual items, directly to users, one by one. This is changing. As more items are either born digital or have excellent digital facsimiles, glam are beginning to offer data access and services in addition to simple direct use. This allows the communities we serve to build great things. 

One of the most successful examples is that of the National Library of Australia's [Trove](http://trove.nla.gov.au/) database, which provides [a rich API](http://trove.nla.gov.au/general/api), that allows [independent developers](http://wraggelabs.com/emporium/2012/04/the-new-api-powered-future/) to create all sorts of [generous interfaces](http://www.dancohen.org/2012/12/05/generous-interfaces-for-scholarly-sites/). Similarly, the British Library provides various [free data services](http://www.bl.uk/bibliographic/datafree.html) and the [National Archives of the UK has started offering direct API access to its discovery systems](http://discovery.nationalarchives.gov.uk/SearchUI/api.htm).

Web archives have also tended to focus on the playback of individual web pages, via the Wayback machine, and this is the way most users are used to interacting with our archives.
However, for many years now, that same playback infrastructure has been used to develop other data and interfaces to the content. These APIs allow structured metadata about archival holdings to be retrieved programmatically, and in subsequent posts we'll explore how the Wayback queries and Memento protocols can be used to exploit web archives.

Alongside these online services, we've also been exploring the possibilities around making metadata datasets available for research and analysis. So far we're released an historical geoindex, a format profile, . We're also about to make further, even richer datasets available, based on the same 1996-2010 archive.

The Wayback API
------------------------

Wayback query API is similar, but slightly more powerful, and slightly easier to integrate. Two types, if you have a URI of interest, holdings. Also a Memento version of that. However, the starts-with query let's you list and discover.

http://wwwoh-access.archive.org/wwwoh/waybackapi.htm

http://web.archive.org/web/xmlquery?type=urlquery&url=http://www.webarchive.org.uk/

Use cases for this, knowing the uri, include wikipedia link rot prevention and find mementos. Would be interest in ways of integration with wikipedia to ensure refs are archived and linked to.

But also, beyond the URL. What was on the web in this year etc. Internal infrastructure allows any number of properties to be indexed, and this could be made into an API. What would you like to see?

The Memento API
-------------------------
Memento covers a range of technologies but in terms of the API, the basic usage is quite simple. ???
Mention prototype Chrome plugin?

The Historical UK Host Linkage Dataset
-------------------------------------------------
http://www.webarchive.org.uk/datasets/ukwa.ds.2/linkage/bl.uk.txt.srt

The Historical UK Link Graph Dataset
---------------------------------------------------
i.e. The WATs


