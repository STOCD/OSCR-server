# OSCR_django_client.VariantApi

All URIs are relative to *https://oscr.stobuilds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**variant_list**](VariantApi.md#variant_list) | **GET** /variant/ | 
[**variant_read**](VariantApi.md#variant_read) | **GET** /variant/{name}/ | 


# **variant_list**
> VariantList200Response variant_list(name=name, start_date=start_date, end_date=end_date, is_ground_variant=is_ground_variant, is_space_variant=is_space_variant, exclude_space=exclude_space, exclude_ground=exclude_ground, combat_time_source=combat_time_source, combat_time_threshold=combat_time_threshold, ordering=ordering, search=search, page=page, page_size=page_size)

Variant API

### Example

* Basic Authentication (Basic):

```python
import OSCR_django_client
from OSCR_django_client.models.variant_list200_response import VariantList200Response
from OSCR_django_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://oscr.stobuilds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = OSCR_django_client.Configuration(
    host = "https://oscr.stobuilds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = OSCR_django_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with OSCR_django_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = OSCR_django_client.VariantApi(api_client)
    name = 'name_example' # str | name (optional)
    start_date = 'start_date_example' # str | start_date (optional)
    end_date = 'end_date_example' # str | end_date (optional)
    is_ground_variant = 'is_ground_variant_example' # str | is_ground_variant (optional)
    is_space_variant = 'is_space_variant_example' # str | is_space_variant (optional)
    exclude_space = 'exclude_space_example' # str | exclude_space (optional)
    exclude_ground = 'exclude_ground_example' # str | exclude_ground (optional)
    combat_time_source = 'combat_time_source_example' # str | combat_time_source (optional)
    combat_time_threshold = 'combat_time_threshold_example' # str | combat_time_threshold (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    search = 'search_example' # str | A search term. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.variant_list(name=name, start_date=start_date, end_date=end_date, is_ground_variant=is_ground_variant, is_space_variant=is_space_variant, exclude_space=exclude_space, exclude_ground=exclude_ground, combat_time_source=combat_time_source, combat_time_threshold=combat_time_threshold, ordering=ordering, search=search, page=page, page_size=page_size)
        print("The response of VariantApi->variant_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariantApi->variant_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | [optional] 
 **start_date** | **str**| start_date | [optional] 
 **end_date** | **str**| end_date | [optional] 
 **is_ground_variant** | **str**| is_ground_variant | [optional] 
 **is_space_variant** | **str**| is_space_variant | [optional] 
 **exclude_space** | **str**| exclude_space | [optional] 
 **exclude_ground** | **str**| exclude_ground | [optional] 
 **combat_time_source** | **str**| combat_time_source | [optional] 
 **combat_time_threshold** | **str**| combat_time_threshold | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**VariantList200Response**](VariantList200Response.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variant_read**
> Variant variant_read(name)

Variant API

### Example

* Basic Authentication (Basic):

```python
import OSCR_django_client
from OSCR_django_client.models.variant import Variant
from OSCR_django_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://oscr.stobuilds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = OSCR_django_client.Configuration(
    host = "https://oscr.stobuilds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = OSCR_django_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with OSCR_django_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = OSCR_django_client.VariantApi(api_client)
    name = 'name_example' # str | A unique value identifying this variant.

    try:
        api_response = api_instance.variant_read(name)
        print("The response of VariantApi->variant_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariantApi->variant_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A unique value identifying this variant. | 

### Return type

[**Variant**](Variant.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

