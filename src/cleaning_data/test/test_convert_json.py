"""
@name: test_convert_json
@author: Vuong Quoc Viet
@version: 1.0
@since: Mar 03, 2018
"""
from cleaning_data.models.information_post import InformationPost
from cleaning_data.service.covert_json_service import ConvertJsonService

model = InformationPost()
json_data = ConvertJsonService().get_json(model)
print json_data


