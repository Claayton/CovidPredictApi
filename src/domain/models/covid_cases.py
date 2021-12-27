"""Interface para a tupla nomeada CovidCases"""
from collections import namedtuple

CovidCases = namedtuple("CovidCases", "id date new_cases country_id")
