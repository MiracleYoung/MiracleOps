### Salt & Salt-Api

1. Install salt-master on your master server

**PS**: Recommend Python 2.7 on master server, although SaltStack have been compatibile to Python 3, actually not very well in my side.
```bash
curl -L https://bootstrap.saltstack.com -o install_salt.sh
sudo sh install_salt.sh -M
```

2. If you want to install salt-minion, do below script on your minion server

**PS**: After v1.1, MO supply SSH module to installed minion on web
```bash
curl -L https://bootstrap.saltstack.com -o install_salt.sh
sudo sh install_salt.sh
```

3. Install salt-api, salt python packages.
```bash
pip install salt salt-api
```

4. Write the following content to your master config, ex: `/etc/salt/master.d/salt-api.conf`
```yaml
interface: 0.0.0.0

external_auth:
  pam:
    saltapi:
      - .*
      - '@wheel'
      - '@runner'
      - '@jobs'

rest_cherrypy:
  port: 9000
  disable_ssl: True # disable ssl for simple
```

5. In order to make sure your salt-api work, create a *saltapi* user on your master server for *salt rest api* auth.
```bash
pip install rest_cherrypy # supply rest api
useradd saltapi -s /sbin/nologin
```

6. Test your salt-api
```bash
[root@miracle salt]# salt-api exec

# open another terminal
[root@miracle salt]# curl http://localhost:9000/login \
>     -H 'Accept: application/x-yaml' \
>     -d username=saltapi \
>     -d password=saltapi \
>     -d eauth=pam
return:
- eauth: pam
  expire: 1516793480.405034
  perms:
  - .*
  - '@wheel'
  - '@runner'
  - '@jobs'
  start: 1516750280.405032
  token: 3bfe295499a6702d2de00b4f93bde66509de8d31
  user: saltapi
```
This means you already installed successfully!

### Web

1. Please use Python 3.x.(3.6 is recommendation.)
2. Install packages: `pip install -r requirements.txt`
3. Modify MySQL config in MiracleOps.settings.py: 
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MiracleOps', # Your Database Name
        # 'HOST': '127.0.0.1',
        'HOST': '127.0.0.1', # Your MySQL instance host or IP
        'PORT': 3306, # Your MySQL instance port
        'USER': 'root', # Your MySQL instance user
        'PASSWORD': '', # Your MySQL instance password
        'CHARSET': 'utf8', # Your MySQL client character
    }
}

SALT_API_URL = 'http://127.0.0.1:9000' # change it to your salt-api host:port
SALT_API_USERNAME = 'saltapi' # your saltapi user 
SALT_API_PASSWORD = 'saltapi'
``` 
4. Migrate python data model to MySQL:
```python
python manager.py makemigrations
python manager.py migrate
```
5. Run app in DEBUG schema. `python manager.py runserver 0.0.0.0:8080`

6. Starting development server at `http://0.0.0.0:8080/`