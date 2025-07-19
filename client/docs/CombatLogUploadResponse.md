# CombatLogUploadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**updated** | **bool** |  | 
**detail** | **str** |  | 
**value** | **float** |  | 

## Example

```python
from OSCR_django_client.models.combat_log_upload_response import CombatLogUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CombatLogUploadResponse from a JSON string
combat_log_upload_response_instance = CombatLogUploadResponse.from_json(json)
# print the JSON string representation of the object
print(CombatLogUploadResponse.to_json())

# convert the object into a dict
combat_log_upload_response_dict = combat_log_upload_response_instance.to_dict()
# create an instance of CombatLogUploadResponse from a dict
combat_log_upload_response_from_dict = CombatLogUploadResponse.from_dict(combat_log_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


