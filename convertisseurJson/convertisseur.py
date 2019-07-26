#!/usr/bin/env python

import simplejson
import sys
import yaml
import json


class ConvertisseurJson:

    def __init__(self, filename):
        self.filename = filename

    def convert(self):
        with open(self.filename) as json_file:
            resYaml = open('test.yml', 'w')
            resYaml.write(yaml.dump(simplejson.load(json_file)))
            resYaml.close()

if __name__ == "__main__":
    __init__()
