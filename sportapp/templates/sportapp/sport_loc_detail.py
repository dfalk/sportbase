{% extends base.html' %}

{% block extra_head %}
<style>
.form-list { padding: 2px; border: 1px solid gray; margin-bottom: 10px; }
.form-list td { padding: 4px; padding-bottom: 6px; border: 1px solid #bbbbbb; }
</style>
{% endblock %}

{% block content %}


<h1> {{ location }} </h1>
<p><b>Список соревнований: </b></p>
<table class="form-list">
{% for tourney in tourney_loc  %}
<tr>
    <td style="width: 130px"><b>{{ tourney.date_start }}</b>
    {% if tourney.date_end and tourney.date_start != tourney.date_end %}<br/>- {{ tourney.date_end}}{% endif %}</td>
    <td><a href="/sport/detail/{{ tourney.id }}">{{ tourney }}</a></td>
</tr>
{% endfor %}
</table>

{% endblock %}
