"""
lanpartydb_website.blueprints.party.views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Copyright: 2024 Jochen Kupperschmidt
:License: MIT
"""

from flask import abort, current_app, request
from flask_paginate import Pagination
from lanpartydb.models import Party
from pycountry import countries
from pycountry.db import Country

from ...util.blueprint import create_blueprint
from ...util.templating import templated


blueprint = create_blueprint('party', __name__, url_prefix='/parties')


@blueprint.get('/', defaults={'page': 1})
@blueprint.get('/pages/<int:page>/')
@templated
def index(page: int):
    per_page = request.args.get('per_page', type=int, default=50)
    offset = (page - 1) * per_page

    parties = list(current_app.parties_by_slug.values())
    parties.sort(key=lambda party: party.start_on, reverse=True)

    pagination = Pagination(page=page, per_page=per_page, total=len(parties))

    parties_slice = parties[offset : offset + per_page]

    return {
        'parties': parties_slice,
        'pagination': pagination,
    }


@blueprint.get('/<slug>/')
@templated
def view(slug: str):
    party = current_app.parties_by_slug.get(slug)
    if not party:
        abort(404)

    series = current_app.series_by_slug.get(party.series_slug)

    country = _get_country(party)

    return {
        'party': party,
        'series': series,
        'country': country,
    }


def _get_country(party: Party) -> Country | None:
    if not party.location:
        return None

    return countries.get(alpha_2=party.location.country_code)
