"""
lanpartydb_website.blueprints.base.views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Copyright: 2024 Jochen Kupperschmidt
:License: MIT
"""

from datetime import datetime, UTC
from typing import Any

from ...util.blueprint import create_blueprint


blueprint = create_blueprint('base', __name__)


@blueprint.app_context_processor
def extend_template_context() -> dict[str, Any]:
    return {
        'now': datetime.now(UTC),
    }
