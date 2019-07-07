#!/usr/bin/env bash

# pytest : export is required otherwise pytest can't find imports
export PYTHONPATH=../:../app
cd tests
pytest
