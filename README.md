easy.init
=========
Ansible role to prepare an EASY deployment. 

SYNOPSIS
--------

    ansible-galaxy install git+https://github.com/DANS-KNAW/easy.init


DESCRIPTION
-----------
This role installs:

* some shared dependencies;
* some libraries that are needed by Ansible during the build;
* some programs that come in handy for the application manager (e.g., `tmux`).

