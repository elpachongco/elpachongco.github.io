---
layout: page
title: Shorts
permalink: /shorts/
---
<p>
Place for shorter content. Subscribe at your own risk.
</p>
<p class="feed-subscribe">
  <a href="{{ site.feed.collections.shorts.path | default: 'feed/shorts.xml' | absolute_url }}">
    <svg class="svg-icon orange">
      <use xlink:href="{{ 'assets/minima-social-icons.svg#rss' | relative_url }}"></use>
    </svg><span>Subscribe to Shorts</span>
  </a>
</p>


<ul class="post-list">
  {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y %I:%M%p" -%}
  {%- for short in site.shorts reversed -%}
  <div class="short-item">
    <li>
      <span class="post-meta">{{ short.date | date: date_format }}</span>
      <h3>
        <a class="post-link" href="{{ short.url | relative_url }}">
          {{ short.title | escape }}
        </a>
      </h3>
      <p>{{ short.content | markdownify }}</p>
    </li>
  </div>
  {%- endfor -%}
</ul>
