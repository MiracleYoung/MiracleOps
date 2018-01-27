{% load static %}

### Roster List

- You can click the roster file name to open the detail modal.
- You can delete the row roster, pay attention, this is a update status action, so you can not choose it in *Install Minion* unit and *Server List* unit.

<img src="{% static 'images/doc/mo/ssh_roster_list_detail.png' %}" class="img-responsive">

### Roster Upload

In this unit, you can drag your file to the box.

**PS**: The file postfix must be *.roster*.

For example:

**centos.roster:**
```yaml
web-pro.centos1.com:
  host: web-pro.centos1.com
  user: root
  password: 123
  sudo: True

db-dev.centos2.com:
  host: db-dev.centos2.com
  user: root
  password: 123
  sudo: True

web-stg.centos3.com:
  host: web-stg.centos3.com
  user: root
  password: 123
  sudo: True
```

<img src="{% static 'images/doc/mo/ssh_roster_upload.png' %}" class="img-responsive">

### Install Minion

This unit is used installing salt-minion for some host not installed.

**PS**: You should upload your roster file first, then to choose the file in the select frame.

<img src="{% static 'images/doc/mo/ssh_install_minion.png' %}" class="img-responsive">

### Server List

You can execute some simple command in this unit.

My original intention is for some simple test for newbies.

**PS**: It is not suggested you to use this unit for working. Just install salt-minion, and Use Salt Minion module.

<img src="{% static 'images/doc/mo/ssh_cmd.png' %}" class="img-responsive">