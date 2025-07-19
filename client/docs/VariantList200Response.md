# VariantList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Variant]**](Variant.md) |  | 

## Example

```python
from OSCR_django_client.models.variant_list200_response import VariantList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VariantList200Response from a JSON string
variant_list200_response_instance = VariantList200Response.from_json(json)
# print the JSON string representation of the object
print(VariantList200Response.to_json())

# convert the object into a dict
variant_list200_response_dict = variant_list200_response_instance.to_dict()
# create an instance of VariantList200Response from a dict
variant_list200_response_from_dict = VariantList200Response.from_dict(variant_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


