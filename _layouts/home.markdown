---
layout: default
---

{{content}}

<h2>Episodes</h2>

<ul>
{% for post in site.posts %}
<li><a href="{{post.url | prepend: site.baseurl}}">Season {{post.itunesSeason}} Episode {{post.itunesEpisode}} - {{post.title}}</a></li>
{% endfor %}
</ul>
