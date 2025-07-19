# Ladder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**variant_name** | **str** |  | [optional] [readonly] 
**name** | **str** |  | 
**difficulty** | **str** |  | [optional] 
**is_solo** | **bool** |  | [optional] 
**is_space** | **bool** |  | [optional] 
**metric** | **str** |  | 
**variant** | **str** |  | 

## Example

```python
from OSCR_django_client.models.ladder import Ladder

# TODO update the JSON string below
json = "{}"
# create an instance of Ladder from a JSON string
ladder_instance = Ladder.from_json(json)
# print the JSON string representation of the object
print(Ladder.to_json())

# convert the object into a dict
ladder_dict = ladder_instance.to_dict()
# create an instance of Ladder from a dict
ladder_from_dict = Ladder.from_dict(ladder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


