# Variant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**is_ground_variant** | **bool** |  | [optional] 
**is_space_variant** | **bool** |  | [optional] 
**combat_time_source** | **str** |  | [optional] 
**combat_time_threshold** | **float** |  | [optional] 
**exclude_space** | **List[str]** |  | [optional] 
**exclude_ground** | **List[str]** |  | [optional] 

## Example

```python
from OSCR_django_client.models.variant import Variant

# TODO update the JSON string below
json = "{}"
# create an instance of Variant from a JSON string
variant_instance = Variant.from_json(json)
# print the JSON string representation of the object
print(Variant.to_json())

# convert the object into a dict
variant_dict = variant_instance.to_dict()
# create an instance of Variant from a dict
variant_from_dict = Variant.from_dict(variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


