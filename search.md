---
layout: default
title: '검색'
---

<html data-baseurl="{{ site.baseurl }}"></html>
<link rel="stylesheet" href="{{ site.baseurl }}/assets/style.css">
<div class="nav"><a href="{{ site.baseurl }}/">Home</a><a href="{{ site.baseurl }}/search.html">검색</a><a href="{{ site.baseurl }}/about.html">소개</a><a href="{{ site.baseurl }}/disclaimer.html">면책</a></div>

# 검색
<div class="searchbar">
  <input id="q" placeholder="용어/카테고리 검색…" autofocus>
</div>
<div id="results"></div>
<script src="{{ site.baseurl }}/assets/search.js"></script>
