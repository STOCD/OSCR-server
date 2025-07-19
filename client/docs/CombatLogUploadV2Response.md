# CombatLogUploadV2Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[CombatLogUploadResponse]**](CombatLogUploadResponse.md) |  | [optional] 
**combatlog** | **int** |  | [optional] 
**detail** | **str** |  | 

## Example

```python
from OSCR_django_client.models.combat_log_upload_v2_response import CombatLogUploadV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of CombatLogUploadV2Response from a JSON string
combat_log_upload_v2_response_instance = CombatLogUploadV2Response.from_json(json)
# print the JSON string representation of the object
print(CombatLogUploadV2Response.to_json())

# convert the object into a dict
combat_log_upload_v2_response_dict = combat_log_upload_v2_response_instance.to_dict()
# create an instance of CombatLogUploadV2Response from a dict
combat_log_upload_v2_response_from_dict = CombatLogUploadV2Response.from_dict(combat_log_upload_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


