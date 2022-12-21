"""
config.py: Configuration values. Secrets to be handled with Secrets Manager
"""

import logging
import socket

SKID_NAME = 'DABS'

AGOL_ORG = 'https://utah.maps.arcgis.com'
SENDGRID_SETTINGS = {  #: Settings for SendGridHandler
    'from_address': 'noreply@utah.gov',
    'to_addresses': 'eneemann@utah.gov',
    'prefix': f'{SKID_NAME} on {socket.gethostname()}: ',
}
LOG_LEVEL = logging.DEBUG
LOG_FILE_NAME = 'log'

# FEATURE_LAYER_ITEMID = 'bb9518380e0f42ec9a7bd29104762c32' # TESTING
# FEATURE_LAYER_ITEMID = 'b120a5ee1f85468c9367e9a98a2ccf22' # TESTING_4
# FEATURE_LAYER_ITEMID = '96fbd8c210a24ed7be12611502be6c1e' # TESTING_3
# FEATURE_LAYER_ITEMID = '132af29731ca4ae5b505d46a720c9a60' # TESTING_1027
FEATURE_LAYER_ITEMID = '17a454e0c81547d1b13040da97d17506' # TESTING_20221220
# FEATURE_LAYER_ITEMID = '5708ae24486a4dae810e37fe613a63b6' # The Live Layer!
# FEATURE_LAYER_ITEMID = '0909ac49fa404f1793862499e914caef' # The New Live Layer!
JOIN_COLUMN = 'Lic_Number'
ATTACHMENT_LINK_COLUMN = ''
ATTACHMENT_PATH_COLUMN = ''
FIELDS = {
    'Lic_Number': str,
    'Name': str,
    'Address': str,
    'City': str,
    'Zip': str,
}
