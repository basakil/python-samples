#!/usr/bin/env python

from flask import Flask, request, json
import logging

tasks = [{"id": 1, "name": "Task 1"}, {"id": 2, "name": "Task 2"}]

api = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


def print_request(_request, _logger):
    if request.values:
        _logger.info('request.values=' + _request.values.__repr__())
    if request.json:
        _logger.info('request.json=' + _request.json.__repr__())
    if request.files:
        _logger.info('request.files=' + _request.files.__repr__())
    if request.data:
        _logger.info('request.data=' + _request.data.__repr__())

@api.route('/tasks',  methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_tasks():
    # api.logger.info('Processing /tasks..')
    print_request(request, api.logger)
    return json.dumps(tasks)


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=5000)
