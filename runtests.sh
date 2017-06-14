#!/bin/bash
set -e
export FLASK_ENV="TESTING"
coverage run `which nosetests` hascore tests
coverage report
