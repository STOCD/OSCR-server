# LadderEntriesList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[LadderEntry]**](LadderEntry.md) |  | 

## Example

```python
from OSCR_django_client.models.ladder_entries_list200_response import LadderEntriesList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LadderEntriesList200Response from a JSON string
ladder_entries_list200_response_instance = LadderEntriesList200Response.from_json(json)
# print the JSON string representation of the object
print(LadderEntriesList200Response.to_json())

# convert the object into a dict
ladder_entries_list200_response_dict = ladder_entries_list200_response_instance.to_dict()
# create an instance of LadderEntriesList200Response from a dict
ladder_entries_list200_response_from_dict = LadderEntriesList200Response.from_dict(ladder_entries_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


