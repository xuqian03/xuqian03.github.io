---
permalink: /
title: "Welcome!"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---



I am Qian Xu, currently a Master's student in Information and Communication Engineering at the [College of Electronics and Information Engineering](https://ceie.szu.edu.cn/), [Shenzhen University (SZU)](https://en.szu.edu.cn/), advised by [Prof. Shishun Tian](https://shishuntian.github.io/).

My research focuses on light-field computer vision, with an emphasis on referring image segmentation, epipolar geometry, and multimodal reasoning with large language models. I am interested in building structure-aware frameworks that fuse natural language instructions with high-dimensional light-field cues for robust perception in complex, occluded scenes.

I am currently seeking a position as a doctor.

## 📢 News

{% if site.data.news %}
{::nomarkdown}
<div class="news-scroller" id="news" role="region" aria-label="News">
<ul>
{% for item in site.data.news %}<li>{{ item.text }}</li>{% endfor %}
</ul>
{% assign news_count = site.data.news | size %}{% if news_count > 6 %}<div class="news-hint" aria-hidden="true">scroll for more ↓</div>{% endif %}
</div>
{:/nomarkdown}
{% endif %}

## Publications

{% assign pubs = site.data.publications %}
{% if pubs %}
{::nomarkdown}
<div class="pub-gallery">
{% for pub in pubs %}{% assign has_image = pub.image | default: '' | strip %}
<article class="pub-card{% if has_image == '' %} pub-card--text{% endif %}">{% if has_image != '' %}<a class="pub-card__figure" href="{{ pub.image | relative_url }}" target="_blank" rel="noopener" aria-label="Open the full-size figure for {{ pub.title | escape }}"><img src="{{ pub.image | relative_url }}" alt="{{ pub.title | escape }}" loading="lazy"></a>{% endif %}<div class="pub-card__body"><h3 class="pub-card__title">{% if pub.paper and pub.paper != '' %}<a href="{{ pub.paper }}" target="_blank" rel="noopener">{{ pub.title }}</a>{% else %}{{ pub.title }}{% endif %}</h3><p class="pub-card__authors">{{ pub.authors }}</p><p class="pub-card__venue">{{ pub.venue }}</p>{% if pub.note and pub.note != '' %}<p class="pub-card__note">{{ pub.note }}</p>{% endif %}{% if pub.paper or pub.code or pub.project %}<p class="pub-card__links">{% if pub.paper and pub.paper != '' %}<a class="pub-link" href="{{ pub.paper }}" target="_blank" rel="noopener">Paper</a>{% endif %}{% if pub.code and pub.code != '' %}<a class="pub-link" href="{{ pub.code }}" target="_blank" rel="noopener">Code</a>{% endif %}{% if pub.project and pub.project != '' %}<a class="pub-link" href="{{ pub.project }}" target="_blank" rel="noopener">Project</a>{% endif %}</p>{% endif %}</div></article>
{% endfor %}</div>
{:/nomarkdown}
{% endif %}


## Honors & Awards

{: #honors-awards }

* University Special Scholarship, Shenzhen University
* University First-Class Scholarship, Shenzhen University
* University First-Class Scholarship, Dalian Polytechnic University
