# docker-localshop

Recipe for building a [Localshop pypi registry](https://github.com/mvantellingen/localshop) docker container.


## Configuration

As a convention, here at [botify-labs](https://github.com/botify-labs), we set up the Docker building filesystem context
in a ``context`` subfolder mirroring the actual final container fs state, just like you would do in a [puppet]() module ``files``
folder. If you don't get it yet, take a look at the ``context`` folder of the repository ;)

However, locashop is built upon the [Django](https://www.djangoproject.com/) framework, and requires to set up a ``superuser``. As a default this recipe
will create a ``localshop`` superuser with ``localshop`` password. However, if you'd wanna tune it a little bit
to set up your own in the ``/docker-localshop/localshop/context/localshop.conf`` file.

## Building

```bash
$ git clone git@github.com:oleiade/docker-localshop
$ cd docker-localshop
$ docker build -t localshop localshop/
```

And you should be done.


## Running

Docker-localshop exposes the localshop service through port 8080. You're free to modify the recipe to expose your own. Anyway,
you can route any port on your docker host machine to the localshop container using the ``-p`` option like the following.

```bash
$ docker run -d -p LOCAL_PORT:CONTAINER_PORT localshop
```


## License

Copyright (c) 2013, Theo Crevon. All rights reserved.


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


## Contribute

Localshop container builder is far from perfect, and could be easily enhanced or fixed, don't restrain yourself
just follow the path:

1. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
2. Fork the repository on Github to start making your changes to the master branch.
3. Send a pull request and bug the maintainer until it gets merged and published.
4. Make sure to add yourself to AUTHORS.


*Please note that these instructions were lazily copied from [Kenneth reitz requests](https://github.com/kennethreitz/requests)*


