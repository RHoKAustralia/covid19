# covid19

Temporary home for covid19 hackathon

## Development Setup

There is a `pyproject.toml` file within the `covid19` directory. This is a standard Python project description file
that can be used to describe configuration and build data. The standard is described in [PEP-0518](https://www.python.org/dev/peps/pep-0518/)

One of the benefits for developers is that it installs the development environment and requirements into a virtual environment so that packages and requirements do not conflict with other system installed packages.

To get started install `poetry` on your system by following the instructions here:

https://python-poetry.org/docs/

And then

```sh
$ cd covid19
$ poetry install
```

This will fetch and install all requirements. To develop in the environment run:

```sh
$ poetry shell
```

Which will activate the virtual environment
