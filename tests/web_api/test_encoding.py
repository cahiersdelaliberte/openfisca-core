# -*- coding: utf-8 -*-

from httplib import BAD_REQUEST, OK, NOT_FOUND
import json
import dpath
from nose.tools import assert_equal, assert_in
from . import subject
import logging


log = logging.getLogger(__name__)


def post_json(data = None, file = None):
    if file:
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', file)
        with open(file_path, 'r') as file:
            data = file.read()
    return subject.post('/calculate', data = data, content_type = 'application/json')


def check_response(data, expected_error_code, path_to_check, content_to_check):
    response = post_json(data)
    assert_equal(response.status_code, expected_error_code)
    json_response = json.loads(response.data, encoding='utf-8')
    if path_to_check:
        content = dpath.util.get(json_response, path_to_check)
        assert_in(content_to_check, content)


def test_encoding():
    simulation_json = json.dumps({
        "persons": {
            "O‘Ryan": {},
            "Renée": {}
        },
        "households": {
            "_": {
                "housing_occupancy_status": {
                    "2017-07": "Locataire ou sous-locataire d‘un logement loué vide non-HLM"
    
                },
                "parent": [
                    "O‘Ryan",
                    "Renée"
                ],
                "children": [ ]
            }
        }
    })

    expected_response = "'Locataire ou sous-locataire d‘un logement loué vide non-HLM' is not a valid value for 'housing_occupancy_status'. Possible values are ['Tenant', 'Owner', 'Free logder', 'Homeless']."
    check_response(simulation_json, BAD_REQUEST, 'households/_/housing_occupancy_status/2017-07', expected_response)
    response = post_json(simulation_json)
    assertresponse.data.decode('utf-8')
    assert_equal(response.status_code, OK, response.data)
