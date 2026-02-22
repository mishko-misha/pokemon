import sys
from unittest.mock import MagicMock

mock_translate = MagicMock()
sys.modules["google.cloud.translate"] = mock_translate
mock_translate.Client.return_value.translate.return_value = {"translatedText": "Pikachu-FR"}

from pokemon_name_translator import PokemonNameTranslator
from pokemon_report import PokemonReport
from pokemon_service import PokemonService

import pytest

@pytest.fixture
def pokemon_service():
    return PokemonService()

@pytest.fixture
def pikachu_info():
    return {
        "name": "pikachu",
        "id": 25,
        "height": 4,
        "weight": 60,
        "types": [
            {
                "slot": 1,
                "type": {
                    "name": "electric",
                    "url": "https://pokeapi.co/api/v2/type/13/"
                }
            }
        ],
        "abilities": [
            {"ability": {"name": "static"}},
            {"ability": {"name": "lightning-rod"}}
        ]
    }

@pytest.fixture
def translator():
    return PokemonNameTranslator()

@pytest.fixture
def report_generator():
    return PokemonReport()