#!/usr/bin/env python3
import click
import json
import requests
import logging
from lib_thema import (
    display_item,
    display_docs
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.getLevelName('INFO'))
logger.addHandler(logging.StreamHandler())

ROOT_URL = "https://codex.opendata.api.vlaanderen.be"


@click.group()
def main():
    pass


@main.group()
def thema():
    pass


@thema.command()
def list():
    resp = requests.get(f"{ROOT_URL}/api/thema")
    if resp.status_code == 200:
        raw_output = resp.json()
        themas = raw_output['Items']
        for item in themas:
            display_item(item)


@thema.command()
@click.argument('thema_id')
def show(thema_id):
    resp = requests.get(f"{ROOT_URL}/api/thema/{thema_id}")
    if resp.status_code == 200:
        item = resp.json()
        print(json.dumps(item, indent=2))


@thema.command()
@click.argument('thema_id')
def docs(thema_id):
    resp = requests.get(f"{ROOT_URL}/api/thema/{thema_id}/WetgevingDocumenten")
    if resp.status_code == 200:
        response = resp.json()
        display_docs(response)


if __name__ == "__main__":
    main()
