# OSCR_django_client.SystemApi

All URIs are relative to *https://oscr.stobuilds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_latest**](SystemApi.md#system_latest) | **GET** /system/latest/ | 


# **system_latest**
> List[Update] system_latest()

Fetch information about the latest update

### Example

* Basic Authentication (Basic):

```python
import OSCR_django_client
from OSCR_django_client.models.update import Update
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
    api_instance = OSCR_django_client.SystemApi(api_client)

    try:
        api_response = api_instance.system_latest()
        print("The response of SystemApi->system_latest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->system_latest: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Update]**](Update.md)

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

