"""Diretório de validações para get_countries"""
from cerberus import Validator
from src.data.database.get_countries import GetCountry
from src.infra.database.repo import CountryRepo

countries_repo = CountryRepo()
get_countries = GetCountry(countries_repo)

get_countries_response = get_countries.all_countries()
all_countries = []

for data in get_countries_response["data"]:
    all_countries.append(data.name)


def get_from_country_validator(request: any) -> None:
    """Validor de parâmtros da url"""
    querry_param_validator = Validator(
        {"name": {"type": "string", "allowed": all_countries}}
    )

    response = querry_param_validator.validate(request.query_params)

    if response is False:
        raise Exception(querry_param_validator.errors)