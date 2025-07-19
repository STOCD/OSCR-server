# OSCR_django_client.LadderApi

All URIs are relative to *https://oscr.stobuilds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ladder_list**](LadderApi.md#ladder_list) | **GET** /ladder/ | 
[**ladder_read**](LadderApi.md#ladder_read) | **GET** /ladder/{id}/ | 


# **ladder_list**
> LadderList200Response ladder_list(name=name, difficulty=difficulty, variant=variant, is_solo=is_solo, is_space=is_space, metric=metric, manual_review_threshold=manual_review_threshold, ordering=ordering, search=search, page=page, page_size=page_size)

Ladder API

### Example

* Basic Authentication (Basic):

```python
import OSCR_django_client
from OSCR_django_client.models.ladder_list200_response import LadderList200Response
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
    api_instance = OSCR_django_client.LadderApi(api_client)
    name = 'name_example' # str | name (optional)
    difficulty = 'difficulty_example' # str | difficulty (optional)
    variant = 'variant_example' # str | variant (optional)
    is_solo = 'is_solo_example' # str | is_solo (optional)
    is_space = 'is_space_example' # str | is_space (optional)
    metric = 'metric_example' # str | metric (optional)
    manual_review_threshold = 'manual_review_threshold_example' # str | manual_review_threshold (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    search = 'search_example' # str | A search term. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.ladder_list(name=name, difficulty=difficulty, variant=variant, is_solo=is_solo, is_space=is_space, metric=metric, manual_review_threshold=manual_review_threshold, ordering=ordering, search=search, page=page, page_size=page_size)
        print("The response of LadderApi->ladder_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LadderApi->ladder_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | [optional] 
 **difficulty** | **str**| difficulty | [optional] 
 **variant** | **str**| variant | [optional] 
 **is_solo** | **str**| is_solo | [optional] 
 **is_space** | **str**| is_space | [optional] 
 **metric** | **str**| metric | [optional] 
 **manual_review_threshold** | **str**| manual_review_threshold | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**LadderList200Response**](LadderList200Response.md)

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

# **ladder_read**
> Ladder ladder_read(id)

Ladder API

### Example

* Basic Authentication (Basic):

```python
import OSCR_django_client
from OSCR_django_client.models.ladder import Ladder
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
    api_instance = OSCR_django_client.LadderApi(api_client)
    id = 56 # int | A unique integer value identifying this ladder.

    try:
        api_response = api_instance.ladder_read(id)
        print("The response of LadderApi->ladder_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LadderApi->ladder_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this ladder. | 

### Return type

[**Ladder**](Ladder.md)

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

