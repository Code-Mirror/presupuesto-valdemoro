# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, url

MAIN_ENTITY_LEVEL = 'municipio'
MAIN_ENTITY_NAME = 'Valdemoro'

BUDGET_LOADER = 'ValdemoroBudgetLoader'
PAYMENTS_LOADER = 'ValdemoroPaymentsLoader'

FEATURED_PROGRAMMES = ['9240', '4910', '4930']

OVERVIEW_INCOME_NODES = []
OVERVIEW_EXPENSE_NODES = []
OVERVIEW_INCOME_NODES = [
                          {
                            'nodes': [['11', '113']],
                            'label': 'IMPUESTO SOBRE BIENES INMUEBLES DE NATURALEZA URBANA'
                          },
                          '13', 
                          {
                            'nodes': [['30', '302']],
                            'label': 'TASA DE REOCGIDA DE BASURAS'
                          },
			{
				'nodes': ['30', '31', '32'],
				'label': 'OTRAS TASAS Y PRECIOS PÚBLICOS'
			},
			'33', '34', '42', '45',
                          {
                            'nodes': [['29', '290']],
                            'label': 'IMPUESTO SOBRE CONSTRUCCIONES, INSTALACIONES Y OBRAS'
                          },
                          {
                            'nodes': [['11', '115']],
                            'label': 'IMPUESTOS SOBRE VEHÍCULOS DE TRACCIÓN MECÁNICA'
                          },
                          {
                            'nodes': [['11', '116']],
                            'label': 'IMPUESTO SOBRE INCREMENTO DEL VALOR DE LOS TERRENOS DE NATURALEZA URBANA'
                          },
                          '91'
                        ]
OVERVIEW_EXPENSE_NODES = ['13', '15', '16', '92', '93', '91', '32', '23', '24', '34', '33', '44', '17', '01']
#OVERVIEW_EXPENSE_NODES = ['45', '13', '92', '32', '23', '34', '33', '17', '01']

# How aggresive should the Sankey diagram reorder the nodes. Default: 0.79 (Optional)
# Note: 0.5 usually leaves nodes ordered as defined. 0.95 sorts by size (decreasing).
OVERVIEW_RELAX_FACTOR = 0.5

# Show Payments section in menu & home options. Default: False.
SHOW_PAYMENTS           = True

# Show Tax Receipt section in menu & home options. Default: False.
SHOW_TAX_RECEIPT        = True

# Show Counties & Towns links in Policies section in menu & home options. Default: False.
SHOW_COUNTIES_AND_TOWNS = False

# Show an extra tab with institutional breakdown. Default: True.
SHOW_INSTITUTIONAL_TAB  = False

# Show an extra tab with funding breakdown (only applicable to some budgets). Default: False.
# SHOW_FUNDING_TAB = False

# Adjust inflation in amounts in Overview page. Default: True
ADJUST_INFLATION_IN_OVERVIEW = False

# Show an extra column with actual revenues/expenses. Default: True.
# Warning: the execution data still gets shown in the summary chart and in downloads.
#SHOW_ACTUAL = True

# Include financial income/expenditures in overview and global policy breakdowns. Default: False.
INCLUDE_FINANCIAL_CHAPTERS_IN_BREAKDOWNS = True

# Search in entity names. Default: True.
SEARCH_ENTITIES = False

# Supported languages. Default: ('es', 'Castellano')
LANGUAGES = (
  ('es', 'Castellano'),
)

# Setup Data Source Budget link
DATA_SOURCE_BUDGET      = 'http://www.valdemoro.es/presupuestos1'

# Setup Data Source Population link
DATA_SOURCE_POPULATION  = 'http://www.ine.es/jaxiT3/Tabla.htm?t=2861'

# Setup Data Source Inflation link
DATA_SOURCE_INFLATION   = 'http://www.ine.es/jaxiT3/Tabla.htm?t=10019&L=0'

# Setup Main Entity Web Url
MAIN_ENTITY_WEB_URL     = 'http://www.valdemoro.es/'

# Setup Main Entity Legal Url (if empty we hide the link)
MAIN_ENTITY_LEGAL_URL   = 'http://www.valdemoro.es/aviso-legal'

# External URL for Cookies Policy (if empty we use out template page/cookies.html)
COOKIES_URL             = 'http://www.valdemoro.es/politica-de-cookies'

# Allow overriding of default treemap color scheme
COLOR_SCALE = [ '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#e7969c', '#bcbd22', '#17becf' ]

ANALYTICS_CODE = 'UA-77087919-1'
