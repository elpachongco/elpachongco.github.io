<h3>Shorts</h3>
<p>Welcome to shorts! </p>
<ul class="post-list">
  {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
  {%- for short in site.shorts -%}
  <li>
    <span class="post-meta">{{ short.date | date: date_format }}</span>
    <h3>
      <a class="post-link" href="{{ short.url | relative_url }}">
        {{ short.title | escape }}
      </a>
    </h3>
    <p>{{ short.content | markdownify }}</p>
  </li>
  {%- endfor -%}
</ul>
