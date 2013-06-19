docker-localshop
================

Recipe for building a [Localshop pypi registry](https://github.com/mvantellingen/localshop) docker container.


Building
========

**NOTA** Locashop is built upon the [Django](https://www.djangoproject.com/) framework, and requires to set up a ``superuser``. As a default this recipe
will create a ``localshop`` superuser with ``localshop`` password. However, if you'd wanna tune it a little bit
to set up your own in the ``/docker-localshop/localshop/context/localshop.conf`` file.

```bash
$ git clone git@github.com:oleiade/docker-localshop
$ cd docker-localshop
$ docker build -t localshop localshop/
```

And you should be done.


Running
=======

Docker-localshop exposes the localshop service through port 8080. You're free to modify the recipe to expose your own. Anyway,
you can route any port on your docker host machine to the localshop container using the ``-p`` option like the following.

```bash
$ docker run -d -p LOCAL_PORT:CONTAINER_PORT localshop
```
