apache:
  pkg:
    - installed
      {% if grains['os']|lower == 'centos' %}
    - name: httpd
      {% endif %}
