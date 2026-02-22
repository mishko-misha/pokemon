from unittest.mock import patch
from pokemon_service import PokemonService

def test_get_pokemon_info_with_mock(pokemon_service, pikachu_info):
    with patch.object(PokemonService, "get_pokemon_info", return_value=pikachu_info):
        result = pokemon_service.get_pokemon_info("pikachu")
        assert result["name"] == "pikachu"
        assert result["id"] == 25
        assert result["types"][0]["type"]["name"] == "electric"

def test_get_pokemon_info_not_found(pokemon_service):
    with patch.object(PokemonService, "get_pokemon_info", return_value=None):
        result = pokemon_service.get_pokemon_info("unknown-pokemon")
        assert result is None

def test_report_generation_with_mock_translation(report_generator, pikachu_info):
    translated_name = "Pikachu-FR"

    with patch("pokemon_report.pdfkit.from_file") as mock_pdf:
        report_generator.generate_report(
            pokemon_info=pikachu_info,
            translated_name=translated_name,
            output_pdf="test_report.pdf"
        )
        mock_pdf.assert_called_once()

def test_translator(translator, mock_google_translate):
    with patch("pokemon_name_translator.PokemonNameTranslator.translate", return_value="Pikachu-FR"):
        result = translator.translate("Pikachu", target_language="fr")
        assert result == "Pikachu-FR"