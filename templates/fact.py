#!/usr/bin/python

import json
import functions

print json.dumps({
    "version": functions.version_from_textfile("{{ easy_modules_installation_base_path }}/{{ easy_module_name }}/version")
})
