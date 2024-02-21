"""
lanpartydb_website.loader
~~~~~~~~~~~~~~~~~~~~~~~~~

Data loading

:Copyright: 2024 Jochen Kupperschmidt
:License: MIT
"""

from pathlib import Path

from lanpartydb.models import Party, Series
from lanpartydb.reading import (
    read_party_from_toml_file,
    read_series_list_from_toml_file,
)


def load_series(data_path: Path) -> list[Series]:
    filename = data_path / 'series.toml'
    return read_series_list_from_toml_file(filename)


def load_parties(data_path: Path) -> list[Party]:
    parties_path = data_path / 'parties'
    party_filenames = parties_path.glob('**/*.toml')
    return list(map(read_party_from_toml_file, party_filenames))
