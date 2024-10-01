---
date: 2023-03-17
authors:
  - haiiliin
categories:
  - Academic
tags:
  - Python
  - Pip
---

# Freezing Installed Python Packages

Use the `pip freeze` command to generate a list of installed packages and their versions and save it to the
`requirements.txt` file.

```sh
pip freeze > requirements.txt
```

The `requirements.txt` file can be used to install the same packages and versions on another machine.

```sh
pip install -r requirements.txt
```
