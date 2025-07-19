# CombatLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**metadata** | [**Metadata**](Metadata.md) |  | 
**youtube** | **str** |  | [optional] 

## Example

```python
from OSCR_django_client.models.combat_log import CombatLog

# TODO update the JSON string below
json = "{}"
# create an instance of CombatLog from a JSON string
combat_log_instance = CombatLog.from_json(json)
# print the JSON string representation of the object
print(CombatLog.to_json())

# convert the object into a dict
combat_log_dict = combat_log_instance.to_dict()
# create an instance of CombatLog from a dict
combat_log_from_dict = CombatLog.from_dict(combat_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


