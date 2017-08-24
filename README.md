# mg-rest-auth-test

This is the basic info to get the test server up and running

Installation
============

```
pyenv virtualenv 2.7.10 mg-rest-auth
pyenv activate mg-rest-auth

pip install git+https://github.com/markmcdowall/mg-rest-auth-test.git
```


Config file
===========

Add the file rest/auth_meta.json:

```
{"auth_server" : {"name" : "auth", "url" : "https://<url_auth_server>/userinfo"}}
```

Starting the server
===================

```
${HOME}/.pyenv/versions/2.7.10/envs/mg-rest-auth/bin/waitress-serve --listen=127.0.0.1:5000 rest.app:APP
```


Example Query
=============

```
curl -v -H "Content-Type: application/json" -H "Authorization: Bearer <valid token>" --url "http://localhost:5000/mug/api/check"
```