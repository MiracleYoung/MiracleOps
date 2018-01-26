{% if grains['os']|lower == 'centos' %}
  {% set apache = 'httpd' %}
{% endif %}

apache:
  pkg.installed:
    - name: {{ apache }}
  service.running:
    - name: {{ apache }}
    - require:
      - pkg: apache

/tmp/index.html:
  file.managed:
    - source: salt://index.html
    - require:
      - pkg: apache
