# LadderEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**var_date** | **str** |  | [optional] [readonly] 
**rank** | **int** |  | [optional] [readonly] 
**ladder_rank** | **int** |  | [optional] [readonly] 
**player** | **str** |  | 
**data** | **object** |  | 
**combatlog** | **int** |  | 
**ladder** | **int** |  | 

## Example

```python
from OSCR_django_client.models.ladder_entry import LadderEntry

# TODO update the JSON string below
json = "{}"
# create an instance of LadderEntry from a JSON string
ladder_entry_instance = LadderEntry.from_json(json)
# print the JSON string representation of the object
print(LadderEntry.to_json())

# convert the object into a dict
ladder_entry_dict = ladder_entry_instance.to_dict()
# create an instance of LadderEntry from a dict
ladder_entry_from_dict = LadderEntry.from_dict(ladder_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


