"""Diretório de validações para get_data_covid_from_country"""
from cerberus import Validator
from .countries_list import ALL_COUNTRIES

def get_from_country_validator(request: any) -> None:
    """Validor de parâmtros da url"""
    querry_param_validator = Validator({
        'country': {
            'type': 'string',
            'allowed': ALL_COUNTRIES,
            'required': True
        }
    })

    response = querry_param_validator.validate(request.query_params)

    if response is False:
        raise Exception(querry_param_validator.errors)
