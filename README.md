[![Build Status](https://github.com/c4dt/showcase/actions/workflows/main.yml/badge.svg)](https://github.com/c4dt/showcase/actions/workflows/main.yml)

# Showcase

Code that helps organize the labs' projects and present them nicely

## Purpose

The showcase is the first box of C4DT's Factory. Its purpose is to help labs at the IC faculty
to present their most interesting projects to potential industrial customers.

## Structure

The information regarding the IC labs and their projects is organized in YAML files as follows:

```
data
├── labs.yaml
├── LAB1
│   └── projects.yaml
├── LAB2
│   └── projects.yaml
├── ...
...
```

- `labs.yaml` contains the information on all the labs, each one indexed by an ID.
- Each `projects.yaml`, located in a subdirectory named after a lab ID, contains the information on that lab's projects.

The information is presented to the user via a small [bottle](https://bottlepy.org/) application.

## Yaml structure

A summary of the different entries found in the yaml structure. All text to be changed is written
in `(brackets)`.

### Needed

```yaml
url_path:
  name: (short name)
  description: >
    (Short description, will be shown under the name)
  type: ( "Application" | "Library" | "Framework" | "Toolset" | "Simulation" | "Experiments" )
  categories: ( "Privacy" | "Blockchain" | "Verification" | "Security" |
    "Learning" | "Other" )
  applications: ( "Finance" | "Health" | "Gov" | "Infra" | "Info" | "Other" )
  tags:
    - (Add tags, if possible out of the existing ones)
  date_added: (YYYY-MM-DD)
```

### Optional

```yaml
    layman_desc: >
      (A 2-3 sentence description for somebody with general knowledge)
    tech_desc: >
      (A more detailed description in 2-3 sentences for somebody knowledgeable in the subject)
    notes: (Additional description)
    url: (URL for a home page)
    contacts:
      - name: (Full Name)
        email: (name@institution.org)
    code:
      type: (Lab Github, Personal Gihub, zip files, ...)
      url:  (https://...)
      date_last_commit: (YYYY-MM-DD)
    doc: (url to documentation)
    lines_of_code: (# of codelines)
    c4dt_contact: (Email of a special contact, defaults to c4dt-dev@listes.epfl.ch)
    language: (What the majority of the code is written in)
    license: (BSD, GPL 3+, MPL 2+, Apache, ...)
    information: (zero or more of:)
      - type: (Paper | Video | Article | Blog Post | Demo | Web Page | Documentation)
        title: (Short title)
        url: (https:.. - for papers, don't use arxiv, but the conference link)
        notes: (this is optional)
          - label: (what will be shown in front of the note)
            text: (the text of the note)
            url: (the URL for the <a> tag)
    maturity: (1|2|3)
    incubator:
      work: (What C4DT did for the project)
      products:
        type: ( Demo | Hands-on | Pilot | App | OSS-participation)
        url: (https://...)
        title: (Description of this product)
        code: (https:// of the code)
    date_updated: (YYYY-MM-DD)
```

## Run the application locally

Ensure you have the required tools to create Python virtual environments.
You can either install the dependencies in a virtual environment, or use [devbox](https://www.jetpack.io/devbox).

### Install dependencies in a virtual environment

You might need to install a specific package depending on your distribution,
e.g. on Debian `python3-venv`:

```
$ sudo apt install python3-venv
```

### Use devbox

Install devbox from https://www.jetpack.io/devbox, then run:

```bash
devbox shell --pure
```

### Create the virtual environment

Simply run `make`:

```
$ make
```

This will create a Python virtual environment, activate it,
install the dependencies and run the showcase application.

The application listens by default on port 8080 in the path `showcase`;
point your browser to http://localhost:8080/showcase.

## Run the tests

```
$ make test
```

## Run the application on a server

Assuming `$APP_PATH` is the directory containing the application,
the following must be setup on the server (see also the [mod_wsgi docs](https://modwsgi.readthedocs.io/en/develop/user-guides/virtual-environments.html#daemon-mode-single-application):

Clone the repository:

```
$ cd $APP_PATH && git clone git@github.com:c4dt/showcase.git
```

Create the Python virtual environment and install the dependencies:

```
$ cd showcase
$ make env
```

Configure an Apache virtual host for the app, containing in particular:

```
	WSGIDaemonProcess showcase user=showcase group=showcase processes=1 threads=5 python-home=$APP_PATH/showcase/venv
	WSGIScriptAlias / $APP_PATH/showcase/app.wsgi

	<Directory $APP_PATH/showcase>
		WSGIProcessGroup showcase
		WSGIApplicationGroup %{GLOBAL}
		Require all granted
	</Directory>
```

Restart Apache:

```
$ sudo /etc/init.d/apache2 restart
```

# Tools

## Linkchecker

When checking the links, you can use [LinkChecker](https://github.com/linkchecker/linkchecker) to
scan all links from the showcase.
The configuration file [./linkcheckerrc](./linkcheckerrc) helps to clean up
the result page of a linkchecker run.
You can get the links to the project of a lab with the `data.py` file:

```bash
make env
. ./venv/bin/activate
./data.py
```

This will print out a list of all available labs.
Launch the showcase:

```bash
make showcase &
```

Now you can launch linkchecker on all pages from a given lab:

For a list of available labs:

```bash
./check_lab_links.sh
```

Checking a given lab:

```bash
./check_lab_links.sh LAB_NAME
```

This will also check the links of the external websites.

# Contributing

To contribute to this repository, please install the pre-commit hooks:

```
pre-commit install
```

This will run the linter before committing.
If you already committed, you can run it like this:

```
pre-commit run --all
```
