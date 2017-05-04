#!/bin/bash
export FLASK_ENV="TESTING"
coverage run `which nosetests` hascore tests
coverage report
