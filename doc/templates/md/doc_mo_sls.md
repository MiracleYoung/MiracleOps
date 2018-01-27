### SLS List

- You can click the sls file name to open the detail modal.
- Detail modal will demostate you a recursive strucure, if you upload a zip include directory.
- You can delete the row sls, pay attention, this is a update status action, so you can not choose it in *SLS Execution* unit.

<img src="https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/sls_list.png" class="img-responsive">

### SLS Upload

In this unit, you can drag your file to the box.

**PS**: The file postfix must be *.zip*. For a directory, you should use a zip package as the following example.

**PPS**: Now, your package agenda must be like as below:

For example:

- `top.sls`
- `sls/`
    - `custom.sls`

**top.sls**
```yaml
base:
  '*':
    - sls.custom
```

**sls/custom.sls**
```yaml
apache:
  pkg.installed:
    - name: httpd
  service.running:
    - require:
      - pkg: apache
```

Then `zip -r [biz_name].zip top.sls sls/` to zip a package, and upload it.

More information about *Salt State*, go [https://docs.saltstack.com/en/latest/topics/tutorials/starting_states.html](https://docs.saltstack.com/en/latest/topics/tutorials/starting_states.html).

<img src="https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/sls_upload.png" class="img-responsive">

<img src="https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/sls_upload_structure.png" class="img-responsive">

### SLS Execution

This unit is used executing specific state to execute for glob expression servers.

**PS**: You should upload your state files first, then to choose the file in the select frame.

<img src="https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/sls_execution.png" class="img-responsive">