"""Diretório de validações para get_covid_cases"""
from cerberus import Validator


def get_covid_cases_validator(request: any) -> None:
    """Validor de parâmtros da url"""
    querry_param_validator = Validator(
        {"country": {"type": "string"}, "date": {"type": "string"}}
    )

    response = querry_param_validator.validate(request.query_params)

    if response is False:
        raise Exception(querry_param_validator.errors)
