# OSCR_django_client.LadderEntriesApi

All URIs are relative to *https://oscr.stobuilds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ladder_entries_list**](LadderEntriesApi.md#ladder_entries_list) | **GET** /ladder-entries/ | 
[**ladder_entries_read**](LadderEntriesApi.md#ladder_entries_read) | **GET** /ladder-entries/{id}/ | 


# **ladder_entries_list**
> LadderEntriesList200Response ladder_entries_list(player=player, player__iexact=player__iexact, player__contains=player__contains, player__icontains=player__icontains, player__istartswith=player__istartswith, player__startswith=player__startswith, player__endswith=player__endswith, player__iendswith=player__iendswith, player__iregex=player__iregex, player__regex=player__regex, ladder=ladder, ladder__name=ladder__name, ladder__name__iexact=ladder__name__iexact, ladder__name__contains=ladder__name__contains, ladder__name__icontains=ladder__name__icontains, ladder__name__istartswith=ladder__name__istartswith, ladder__name__startswith=ladder__name__startswith, ladder__name__endswith=ladder__name__endswith, ladder__name__iendswith=ladder__name__iendswith, ladder__name__iregex=ladder__name__iregex, ladder__name__regex=ladder__name__regex, ladder__difficulty=ladder__difficulty, ladder__difficulty__iexact=ladder__difficulty__iexact, ladder__difficulty__contains=ladder__difficulty__contains, ladder__difficulty__icontains=ladder__difficulty__icontains, ladder__difficulty__istartswith=ladder__difficulty__istartswith, ladder__difficulty__startswith=ladder__difficulty__startswith, ladder__difficulty__endswith=ladder__difficulty__endswith, ladder__difficulty__iendswith=ladder__difficulty__iendswith, ladder__difficulty__iregex=ladder__difficulty__iregex, ladder__difficulty__regex=ladder__difficulty__regex, ladder__variant__name=ladder__variant__name, ladder__variant__name__iexact=ladder__variant__name__iexact, ladder__variant__name__contains=ladder__variant__name__contains, ladder__variant__name__icontains=ladder__variant__name__icontains, ladder__variant__name__istartswith=ladder__variant__name__istartswith, ladder__variant__name__startswith=ladder__variant__name__startswith, ladder__variant__name__endswith=ladder__variant__name__endswith, ladder__variant__name__iendswith=ladder__variant__name__iendswith, ladder__variant__name__iregex=ladder__variant__name__iregex, ladder__variant__name__regex=ladder__variant__name__regex, ladder__is_solo=ladder__is_solo, ordering=ordering, page=page, page_size=page_size)

LadderEntry API

### Example

* Basic Authentication (Basic):

```python
import OSCR_django_client
from OSCR_django_client.models.ladder_entries_list200_response import LadderEntriesList200Response
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
    api_instance = OSCR_django_client.LadderEntriesApi(api_client)
    player = 'player_example' # str | player (optional)
    player__iexact = 'player__iexact_example' # str | player__iexact (optional)
    player__contains = 'player__contains_example' # str | player__contains (optional)
    player__icontains = 'player__icontains_example' # str | player__icontains (optional)
    player__istartswith = 'player__istartswith_example' # str | player__istartswith (optional)
    player__startswith = 'player__startswith_example' # str | player__startswith (optional)
    player__endswith = 'player__endswith_example' # str | player__endswith (optional)
    player__iendswith = 'player__iendswith_example' # str | player__iendswith (optional)
    player__iregex = 'player__iregex_example' # str | player__iregex (optional)
    player__regex = 'player__regex_example' # str | player__regex (optional)
    ladder = 'ladder_example' # str | ladder (optional)
    ladder__name = 'ladder__name_example' # str | ladder__name (optional)
    ladder__name__iexact = 'ladder__name__iexact_example' # str | ladder__name__iexact (optional)
    ladder__name__contains = 'ladder__name__contains_example' # str | ladder__name__contains (optional)
    ladder__name__icontains = 'ladder__name__icontains_example' # str | ladder__name__icontains (optional)
    ladder__name__istartswith = 'ladder__name__istartswith_example' # str | ladder__name__istartswith (optional)
    ladder__name__startswith = 'ladder__name__startswith_example' # str | ladder__name__startswith (optional)
    ladder__name__endswith = 'ladder__name__endswith_example' # str | ladder__name__endswith (optional)
    ladder__name__iendswith = 'ladder__name__iendswith_example' # str | ladder__name__iendswith (optional)
    ladder__name__iregex = 'ladder__name__iregex_example' # str | ladder__name__iregex (optional)
    ladder__name__regex = 'ladder__name__regex_example' # str | ladder__name__regex (optional)
    ladder__difficulty = 'ladder__difficulty_example' # str | ladder__difficulty (optional)
    ladder__difficulty__iexact = 'ladder__difficulty__iexact_example' # str | ladder__difficulty__iexact (optional)
    ladder__difficulty__contains = 'ladder__difficulty__contains_example' # str | ladder__difficulty__contains (optional)
    ladder__difficulty__icontains = 'ladder__difficulty__icontains_example' # str | ladder__difficulty__icontains (optional)
    ladder__difficulty__istartswith = 'ladder__difficulty__istartswith_example' # str | ladder__difficulty__istartswith (optional)
    ladder__difficulty__startswith = 'ladder__difficulty__startswith_example' # str | ladder__difficulty__startswith (optional)
    ladder__difficulty__endswith = 'ladder__difficulty__endswith_example' # str | ladder__difficulty__endswith (optional)
    ladder__difficulty__iendswith = 'ladder__difficulty__iendswith_example' # str | ladder__difficulty__iendswith (optional)
    ladder__difficulty__iregex = 'ladder__difficulty__iregex_example' # str | ladder__difficulty__iregex (optional)
    ladder__difficulty__regex = 'ladder__difficulty__regex_example' # str | ladder__difficulty__regex (optional)
    ladder__variant__name = 'ladder__variant__name_example' # str | ladder__variant__name (optional)
    ladder__variant__name__iexact = 'ladder__variant__name__iexact_example' # str | ladder__variant__name__iexact (optional)
    ladder__variant__name__contains = 'ladder__variant__name__contains_example' # str | ladder__variant__name__contains (optional)
    ladder__variant__name__icontains = 'ladder__variant__name__icontains_example' # str | ladder__variant__name__icontains (optional)
    ladder__variant__name__istartswith = 'ladder__variant__name__istartswith_example' # str | ladder__variant__name__istartswith (optional)
    ladder__variant__name__startswith = 'ladder__variant__name__startswith_example' # str | ladder__variant__name__startswith (optional)
    ladder__variant__name__endswith = 'ladder__variant__name__endswith_example' # str | ladder__variant__name__endswith (optional)
    ladder__variant__name__iendswith = 'ladder__variant__name__iendswith_example' # str | ladder__variant__name__iendswith (optional)
    ladder__variant__name__iregex = 'ladder__variant__name__iregex_example' # str | ladder__variant__name__iregex (optional)
    ladder__variant__name__regex = 'ladder__variant__name__regex_example' # str | ladder__variant__name__regex (optional)
    ladder__is_solo = 'ladder__is_solo_example' # str | ladder__is_solo (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.ladder_entries_list(player=player, player__iexact=player__iexact, player__contains=player__contains, player__icontains=player__icontains, player__istartswith=player__istartswith, player__startswith=player__startswith, player__endswith=player__endswith, player__iendswith=player__iendswith, player__iregex=player__iregex, player__regex=player__regex, ladder=ladder, ladder__name=ladder__name, ladder__name__iexact=ladder__name__iexact, ladder__name__contains=ladder__name__contains, ladder__name__icontains=ladder__name__icontains, ladder__name__istartswith=ladder__name__istartswith, ladder__name__startswith=ladder__name__startswith, ladder__name__endswith=ladder__name__endswith, ladder__name__iendswith=ladder__name__iendswith, ladder__name__iregex=ladder__name__iregex, ladder__name__regex=ladder__name__regex, ladder__difficulty=ladder__difficulty, ladder__difficulty__iexact=ladder__difficulty__iexact, ladder__difficulty__contains=ladder__difficulty__contains, ladder__difficulty__icontains=ladder__difficulty__icontains, ladder__difficulty__istartswith=ladder__difficulty__istartswith, ladder__difficulty__startswith=ladder__difficulty__startswith, ladder__difficulty__endswith=ladder__difficulty__endswith, ladder__difficulty__iendswith=ladder__difficulty__iendswith, ladder__difficulty__iregex=ladder__difficulty__iregex, ladder__difficulty__regex=ladder__difficulty__regex, ladder__variant__name=ladder__variant__name, ladder__variant__name__iexact=ladder__variant__name__iexact, ladder__variant__name__contains=ladder__variant__name__contains, ladder__variant__name__icontains=ladder__variant__name__icontains, ladder__variant__name__istartswith=ladder__variant__name__istartswith, ladder__variant__name__startswith=ladder__variant__name__startswith, ladder__variant__name__endswith=ladder__variant__name__endswith, ladder__variant__name__iendswith=ladder__variant__name__iendswith, ladder__variant__name__iregex=ladder__variant__name__iregex, ladder__variant__name__regex=ladder__variant__name__regex, ladder__is_solo=ladder__is_solo, ordering=ordering, page=page, page_size=page_size)
        print("The response of LadderEntriesApi->ladder_entries_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LadderEntriesApi->ladder_entries_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player** | **str**| player | [optional] 
 **player__iexact** | **str**| player__iexact | [optional] 
 **player__contains** | **str**| player__contains | [optional] 
 **player__icontains** | **str**| player__icontains | [optional] 
 **player__istartswith** | **str**| player__istartswith | [optional] 
 **player__startswith** | **str**| player__startswith | [optional] 
 **player__endswith** | **str**| player__endswith | [optional] 
 **player__iendswith** | **str**| player__iendswith | [optional] 
 **player__iregex** | **str**| player__iregex | [optional] 
 **player__regex** | **str**| player__regex | [optional] 
 **ladder** | **str**| ladder | [optional] 
 **ladder__name** | **str**| ladder__name | [optional] 
 **ladder__name__iexact** | **str**| ladder__name__iexact | [optional] 
 **ladder__name__contains** | **str**| ladder__name__contains | [optional] 
 **ladder__name__icontains** | **str**| ladder__name__icontains | [optional] 
 **ladder__name__istartswith** | **str**| ladder__name__istartswith | [optional] 
 **ladder__name__startswith** | **str**| ladder__name__startswith | [optional] 
 **ladder__name__endswith** | **str**| ladder__name__endswith | [optional] 
 **ladder__name__iendswith** | **str**| ladder__name__iendswith | [optional] 
 **ladder__name__iregex** | **str**| ladder__name__iregex | [optional] 
 **ladder__name__regex** | **str**| ladder__name__regex | [optional] 
 **ladder__difficulty** | **str**| ladder__difficulty | [optional] 
 **ladder__difficulty__iexact** | **str**| ladder__difficulty__iexact | [optional] 
 **ladder__difficulty__contains** | **str**| ladder__difficulty__contains | [optional] 
 **ladder__difficulty__icontains** | **str**| ladder__difficulty__icontains | [optional] 
 **ladder__difficulty__istartswith** | **str**| ladder__difficulty__istartswith | [optional] 
 **ladder__difficulty__startswith** | **str**| ladder__difficulty__startswith | [optional] 
 **ladder__difficulty__endswith** | **str**| ladder__difficulty__endswith | [optional] 
 **ladder__difficulty__iendswith** | **str**| ladder__difficulty__iendswith | [optional] 
 **ladder__difficulty__iregex** | **str**| ladder__difficulty__iregex | [optional] 
 **ladder__difficulty__regex** | **str**| ladder__difficulty__regex | [optional] 
 **ladder__variant__name** | **str**| ladder__variant__name | [optional] 
 **ladder__variant__name__iexact** | **str**| ladder__variant__name__iexact | [optional] 
 **ladder__variant__name__contains** | **str**| ladder__variant__name__contains | [optional] 
 **ladder__variant__name__icontains** | **str**| ladder__variant__name__icontains | [optional] 
 **ladder__variant__name__istartswith** | **str**| ladder__variant__name__istartswith | [optional] 
 **ladder__variant__name__startswith** | **str**| ladder__variant__name__startswith | [optional] 
 **ladder__variant__name__endswith** | **str**| ladder__variant__name__endswith | [optional] 
 **ladder__variant__name__iendswith** | **str**| ladder__variant__name__iendswith | [optional] 
 **ladder__variant__name__iregex** | **str**| ladder__variant__name__iregex | [optional] 
 **ladder__variant__name__regex** | **str**| ladder__variant__name__regex | [optional] 
 **ladder__is_solo** | **str**| ladder__is_solo | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**LadderEntriesList200Response**](LadderEntriesList200Response.md)

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

# **ladder_entries_read**
> LadderEntry ladder_entries_read(id)

LadderEntry API

### Example

* Basic Authentication (Basic):

```python
import OSCR_django_client
from OSCR_django_client.models.ladder_entry import LadderEntry
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
    api_instance = OSCR_django_client.LadderEntriesApi(api_client)
    id = 56 # int | A unique integer value identifying this ladder entry.

    try:
        api_response = api_instance.ladder_entries_read(id)
        print("The response of LadderEntriesApi->ladder_entries_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LadderEntriesApi->ladder_entries_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this ladder entry. | 

### Return type

[**LadderEntry**](LadderEntry.md)

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

