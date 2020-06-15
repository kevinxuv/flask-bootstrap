![Build Status](https://travis-ci.com/kevinxuv/flask-bootstrap.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/kevinxuv/flask-bootstrap/badge.svg)](https://coveralls.io/github/kevinxuv/flask-bootstrap)

# flask-bootstrap

A cli tool to bootstrap your [flask](https://github.com/pallets/flask) draft project in a few seconds.

## Install

You can install this tool by pip:

```commandline
$ pip3 install git+https://github.com/kevinxuv/flask-bootstrap
``` 

## Usage

After install, run `flask-boot` in your terminal or console:

```commandline
$ cd /tmp  # cd to your project's workspace
$ flask-boot # run this cmd
$ -> Give your flask project a name [unknown]: test
$ -> Give a description for your flask project [none]: test
$ -> Init git or not? [False]: yes
$ Start to bootstrap project...
$ Finish bootstrap project test at /private/tmp/test
```

Then you will see your created flask draft project in your folder:

```commandline
test
├── README.md
└── test
    ├── __init__.py
    ├── settings.py
    └── wsgi.py

1 directory, 4 files
```

And you can run this flask project by `flask` cli:

```commandline
$ cd /tmp/test # cd to your project dir
$ export FLASK_APP=test.wsgi:app && flask run
$ * Serving Flask app "test.wsgi:app"
$ * Environment: production
$   WARNING: This is a development server. Do not use it in a production deployment.
$   Use a production WSGI server instead.
$ * Debug mode: off
$ * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now, get ready to add more features to it, have fun.
