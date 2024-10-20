# Publications

{% for pub in publications %}

## {{ pub.title }}

<div class="grid cards" markdown>

<div class="publications"><ol class="bibliography"><li>
    <div class="col-sm-3 abbr">
        {% if pub.image %}
            <img src="{{ pub.image }}" class="teaser" >
        {% endif %}
        {% if pub.journal_short %}
            <abbr class="badge">{{ pub.journal_short }}</abbr>
        {% endif %}
    </div>
</li></ol></div>

<div class="col-sm-9" style="position: relative;padding-right: 15px;padding-left: 20px;">
    <div class="title"><a href="{{ pub.link }}">{{ pub.title }}</a></div>
    <div class="author">{{ pub.authors }}</div>
    <div class="periodical"><em>{{ pub.journal }}</em>{% if pub.year %}, {{ pub.year }}{% endif %}{% if pub.volume %}, {{ pub.volume }}{% endif %}{% if pub.issue %}({{ pub.issue }}){% endif %}{% if pub.pages %}, pp. {{ pub.pages }}{% endif %}</div>
    <div class="links">
        {% if pub.code %}
            <a href="{{ pub.code }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">Code</a>
        {% endif %}
        {% if pub.page %}
            <a href="{{ pub.page }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">Project Page</a>
        {% endif %}
        {% if pub.bibtex %}
            <a href="{{ pub.bibtex }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">BibTex</a>
        {% endif %}
        {% if pub.notes %}
            <strong> <i style="color:#e74d3c">{{ pub.notes }}</i></strong>
        {% endif %}
        {% if pub.others %}
            {{ pub.others }}
        {% endif %}
    </div>
</div>

</div>

{% endfor %}
