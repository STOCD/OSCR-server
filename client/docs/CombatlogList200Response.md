# CombatlogList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[CombatLog]**](CombatLog.md) |  | 

## Example

```python
from OSCR_django_client.models.combatlog_list200_response import CombatlogList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CombatlogList200Response from a JSON string
combatlog_list200_response_instance = CombatlogList200Response.from_json(json)
# print the JSON string representation of the object
print(CombatlogList200Response.to_json())

# convert the object into a dict
combatlog_list200_response_dict = combatlog_list200_response_instance.to_dict()
# create an instance of CombatlogList200Response from a dict
combatlog_list200_response_from_dict = CombatlogList200Response.from_dict(combatlog_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


