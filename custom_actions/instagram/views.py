import logging

import requests

from flask import Blueprint, current_app, jsonify
from marshmallow import ValidationError
from webargs.flaskparser import use_args

from . import schema

blueprint = Blueprint("instagram", __name__)

logger = logging.getLogger(__name__)


@blueprint.post('/create_media')
@use_args(schema.CreateMediaSchema, location='json')
def create_media(data: dict):
    try:

        url = f"{current_app.config['INSTAGRAM_APP_BASE_URL']}/{data['ig_user_id']}/media"
        payload = {
            'caption': data['caption'],
            'image_url': data['image_url'],
            'access_token': current_app.config['INSTAGRAM_ACCESS_TOKEN']
        }
        response = requests.post(url, data=payload)
        return jsonify(response.json()), response.status_code

    except ValidationError as err:
        return jsonify(err.messages), 400


@blueprint.get('/read_media')
@use_args(schema.ReadMediaSchema, location='querystring')
def read_media(params: dict):
    ig_user_id = params.get('ig_user_id')

    url = (f"{current_app.config['INSTAGRAM_APP_BASE_URL']}/{ig_user_id}/media"
           f"?access_token={current_app.config['INSTAGRAM_ACCESS_TOKEN']}")
    response = requests.get(url)
    return jsonify(response.json()), response.status_code


@blueprint.get('/read_media')
@use_args(schema.UpdateMediaSchema, location='json')
def update_media(data: dict):
    try:

        url = f"{current_app.config['INSTAGRAM_APP_BASE_URL']}/{data['media_id']}"
        payload = {
            'caption': data['caption'],
            'access_token': current_app.config['INSTAGRAM_ACCESS_TOKEN']
        }
        response = requests.post(url, data=payload)
        return jsonify(response.json()), response.status_code

    except ValidationError as err:
        return jsonify(err.messages), 400


@blueprint.post('/delete_media')
@use_args(schema.DeleteMediaSchema, location='json')
def delete_media(data: dict):
    try:

        url = (f"{current_app.config['INSTAGRAM_APP_BASE_URL']}/{data['media_id']}"
               f"?access_token={current_app.config['INSTAGRAM_ACCESS_TOKEN']}")
        response = requests.delete(url)
        return jsonify(response.json()), response.status_code

    except ValidationError as err:
        return jsonify(err.messages), 400
