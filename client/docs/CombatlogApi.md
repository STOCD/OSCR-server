# OSCR_django_client.CombatlogApi

All URIs are relative to *https://oscr.stobuilds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**combatlog_download**](CombatlogApi.md#combatlog_download) | **GET** /combatlog/{id}/download/ | Combat Log Download
[**combatlog_download_raw**](CombatlogApi.md#combatlog_download_raw) | **GET** /combatlog/{id}/download_raw/ | Combat Log Download
[**combatlog_list**](CombatlogApi.md#combatlog_list) | **GET** /combatlog/ | 
[**combatlog_read**](CombatlogApi.md#combatlog_read) | **GET** /combatlog/{id}/ | 
[**combatlog_upload**](CombatlogApi.md#combatlog_upload) | **POST** /combatlog/upload/ | Combat Log Upload
[**combatlog_uploadv2**](CombatlogApi.md#combatlog_uploadv2) | **POST** /combatlog/uploadv2/ | Combat Log Upload


# **combatlog_download**
> bytearray combatlog_download(id)

Combat Log Download

Download the saved Combat Log

### Example

* Basic Authentication (Basic):

```python
import OSCR_django_client
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
    api_instance = OSCR_django_client.CombatlogApi(api_client)
    id = 56 # int | A unique integer value identifying this combat log.

    try:
        # Combat Log Download
        api_response = api_instance.combatlog_download(id)
        print("The response of CombatlogApi->combatlog_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CombatlogApi->combatlog_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this combat log. | 

### Return type

**bytearray**

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File Attachment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **combatlog_download_raw**
> bytearray combatlog_download_raw(id)

Combat Log Download

Download the saved Combat Log

### Example

* Basic Authentication (Basic):

```python
import OSCR_django_client
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
    api_instance = OSCR_django_client.CombatlogApi(api_client)
    id = 56 # int | A unique integer value identifying this combat log.

    try:
        # Combat Log Download
        api_response = api_instance.combatlog_download_raw(id)
        print("The response of CombatlogApi->combatlog_download_raw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CombatlogApi->combatlog_download_raw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this combat log. | 

### Return type

**bytearray**

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File Attachment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **combatlog_list**
> CombatlogList200Response combatlog_list(page=page, page_size=page_size)

Combat Log API

### Example

* Basic Authentication (Basic):

```python
import OSCR_django_client
from OSCR_django_client.models.combatlog_list200_response import CombatlogList200Response
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
    api_instance = OSCR_django_client.CombatlogApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.combatlog_list(page=page, page_size=page_size)
        print("The response of CombatlogApi->combatlog_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CombatlogApi->combatlog_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**CombatlogList200Response**](CombatlogList200Response.md)

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

# **combatlog_read**
> CombatLog combatlog_read(id)

Combat Log API

### Example

* Basic Authentication (Basic):

```python
import OSCR_django_client
from OSCR_django_client.models.combat_log import CombatLog
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
    api_instance = OSCR_django_client.CombatlogApi(api_client)
    id = 56 # int | A unique integer value identifying this combat log.

    try:
        api_response = api_instance.combatlog_read(id)
        print("The response of CombatlogApi->combatlog_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CombatlogApi->combatlog_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this combat log. | 

### Return type

[**CombatLog**](CombatLog.md)

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

# **combatlog_upload**
> List[CombatLogUploadResponse] combatlog_upload(file)

Combat Log Upload

Uploads a Combat Log for analysis.

### Example

* Basic Authentication (Basic):

```python
import OSCR_django_client
from OSCR_django_client.models.combat_log_upload_response import CombatLogUploadResponse
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
    api_instance = OSCR_django_client.CombatlogApi(api_client)
    file = None # bytearray | 

    try:
        # Combat Log Upload
        api_response = api_instance.combatlog_upload(file)
        print("The response of CombatlogApi->combatlog_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CombatlogApi->combatlog_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 

### Return type

[**List[CombatLogUploadResponse]**](CombatLogUploadResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **combatlog_uploadv2**
> CombatLogUploadV2Response combatlog_uploadv2(file)

Combat Log Upload

Uploads a Combat Log for analysis.

### Example

* Basic Authentication (Basic):

```python
import OSCR_django_client
from OSCR_django_client.models.combat_log_upload_v2_response import CombatLogUploadV2Response
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
    api_instance = OSCR_django_client.CombatlogApi(api_client)
    file = None # bytearray | 

    try:
        # Combat Log Upload
        api_response = api_instance.combatlog_uploadv2(file)
        print("The response of CombatlogApi->combatlog_uploadv2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CombatlogApi->combatlog_uploadv2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 

### Return type

[**CombatLogUploadV2Response**](CombatLogUploadV2Response.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

