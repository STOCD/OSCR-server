# coding: utf-8

"""
    OSCR API

    OSCR API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from OSCR_django_client.models.variant import Variant
from OSCR_django_client.models.variant_list200_response import VariantList200Response

from OSCR_django_client.api_client import ApiClient, RequestSerialized
from OSCR_django_client.api_response import ApiResponse
from OSCR_django_client.rest import RESTResponseType


class VariantApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def variant_list(
        self,
        name: Annotated[Optional[StrictStr], Field(description="name")] = None,
        start_date: Annotated[Optional[StrictStr], Field(description="start_date")] = None,
        end_date: Annotated[Optional[StrictStr], Field(description="end_date")] = None,
        is_ground_variant: Annotated[Optional[StrictStr], Field(description="is_ground_variant")] = None,
        is_space_variant: Annotated[Optional[StrictStr], Field(description="is_space_variant")] = None,
        exclude_space: Annotated[Optional[StrictStr], Field(description="exclude_space")] = None,
        exclude_ground: Annotated[Optional[StrictStr], Field(description="exclude_ground")] = None,
        combat_time_source: Annotated[Optional[StrictStr], Field(description="combat_time_source")] = None,
        combat_time_threshold: Annotated[Optional[StrictStr], Field(description="combat_time_threshold")] = None,
        ordering: Annotated[Optional[StrictStr], Field(description="Which field to use when ordering the results.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="A search term.")] = None,
        page: Annotated[Optional[StrictInt], Field(description="A page number within the paginated result set.")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> VariantList200Response:
        """variant_list

        Variant API

        :param name: name
        :type name: str
        :param start_date: start_date
        :type start_date: str
        :param end_date: end_date
        :type end_date: str
        :param is_ground_variant: is_ground_variant
        :type is_ground_variant: str
        :param is_space_variant: is_space_variant
        :type is_space_variant: str
        :param exclude_space: exclude_space
        :type exclude_space: str
        :param exclude_ground: exclude_ground
        :type exclude_ground: str
        :param combat_time_source: combat_time_source
        :type combat_time_source: str
        :param combat_time_threshold: combat_time_threshold
        :type combat_time_threshold: str
        :param ordering: Which field to use when ordering the results.
        :type ordering: str
        :param search: A search term.
        :type search: str
        :param page: A page number within the paginated result set.
        :type page: int
        :param page_size: Number of results to return per page.
        :type page_size: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._variant_list_serialize(
            name=name,
            start_date=start_date,
            end_date=end_date,
            is_ground_variant=is_ground_variant,
            is_space_variant=is_space_variant,
            exclude_space=exclude_space,
            exclude_ground=exclude_ground,
            combat_time_source=combat_time_source,
            combat_time_threshold=combat_time_threshold,
            ordering=ordering,
            search=search,
            page=page,
            page_size=page_size,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "VariantList200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def variant_list_with_http_info(
        self,
        name: Annotated[Optional[StrictStr], Field(description="name")] = None,
        start_date: Annotated[Optional[StrictStr], Field(description="start_date")] = None,
        end_date: Annotated[Optional[StrictStr], Field(description="end_date")] = None,
        is_ground_variant: Annotated[Optional[StrictStr], Field(description="is_ground_variant")] = None,
        is_space_variant: Annotated[Optional[StrictStr], Field(description="is_space_variant")] = None,
        exclude_space: Annotated[Optional[StrictStr], Field(description="exclude_space")] = None,
        exclude_ground: Annotated[Optional[StrictStr], Field(description="exclude_ground")] = None,
        combat_time_source: Annotated[Optional[StrictStr], Field(description="combat_time_source")] = None,
        combat_time_threshold: Annotated[Optional[StrictStr], Field(description="combat_time_threshold")] = None,
        ordering: Annotated[Optional[StrictStr], Field(description="Which field to use when ordering the results.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="A search term.")] = None,
        page: Annotated[Optional[StrictInt], Field(description="A page number within the paginated result set.")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[VariantList200Response]:
        """variant_list

        Variant API

        :param name: name
        :type name: str
        :param start_date: start_date
        :type start_date: str
        :param end_date: end_date
        :type end_date: str
        :param is_ground_variant: is_ground_variant
        :type is_ground_variant: str
        :param is_space_variant: is_space_variant
        :type is_space_variant: str
        :param exclude_space: exclude_space
        :type exclude_space: str
        :param exclude_ground: exclude_ground
        :type exclude_ground: str
        :param combat_time_source: combat_time_source
        :type combat_time_source: str
        :param combat_time_threshold: combat_time_threshold
        :type combat_time_threshold: str
        :param ordering: Which field to use when ordering the results.
        :type ordering: str
        :param search: A search term.
        :type search: str
        :param page: A page number within the paginated result set.
        :type page: int
        :param page_size: Number of results to return per page.
        :type page_size: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._variant_list_serialize(
            name=name,
            start_date=start_date,
            end_date=end_date,
            is_ground_variant=is_ground_variant,
            is_space_variant=is_space_variant,
            exclude_space=exclude_space,
            exclude_ground=exclude_ground,
            combat_time_source=combat_time_source,
            combat_time_threshold=combat_time_threshold,
            ordering=ordering,
            search=search,
            page=page,
            page_size=page_size,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "VariantList200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def variant_list_without_preload_content(
        self,
        name: Annotated[Optional[StrictStr], Field(description="name")] = None,
        start_date: Annotated[Optional[StrictStr], Field(description="start_date")] = None,
        end_date: Annotated[Optional[StrictStr], Field(description="end_date")] = None,
        is_ground_variant: Annotated[Optional[StrictStr], Field(description="is_ground_variant")] = None,
        is_space_variant: Annotated[Optional[StrictStr], Field(description="is_space_variant")] = None,
        exclude_space: Annotated[Optional[StrictStr], Field(description="exclude_space")] = None,
        exclude_ground: Annotated[Optional[StrictStr], Field(description="exclude_ground")] = None,
        combat_time_source: Annotated[Optional[StrictStr], Field(description="combat_time_source")] = None,
        combat_time_threshold: Annotated[Optional[StrictStr], Field(description="combat_time_threshold")] = None,
        ordering: Annotated[Optional[StrictStr], Field(description="Which field to use when ordering the results.")] = None,
        search: Annotated[Optional[StrictStr], Field(description="A search term.")] = None,
        page: Annotated[Optional[StrictInt], Field(description="A page number within the paginated result set.")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """variant_list

        Variant API

        :param name: name
        :type name: str
        :param start_date: start_date
        :type start_date: str
        :param end_date: end_date
        :type end_date: str
        :param is_ground_variant: is_ground_variant
        :type is_ground_variant: str
        :param is_space_variant: is_space_variant
        :type is_space_variant: str
        :param exclude_space: exclude_space
        :type exclude_space: str
        :param exclude_ground: exclude_ground
        :type exclude_ground: str
        :param combat_time_source: combat_time_source
        :type combat_time_source: str
        :param combat_time_threshold: combat_time_threshold
        :type combat_time_threshold: str
        :param ordering: Which field to use when ordering the results.
        :type ordering: str
        :param search: A search term.
        :type search: str
        :param page: A page number within the paginated result set.
        :type page: int
        :param page_size: Number of results to return per page.
        :type page_size: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._variant_list_serialize(
            name=name,
            start_date=start_date,
            end_date=end_date,
            is_ground_variant=is_ground_variant,
            is_space_variant=is_space_variant,
            exclude_space=exclude_space,
            exclude_ground=exclude_ground,
            combat_time_source=combat_time_source,
            combat_time_threshold=combat_time_threshold,
            ordering=ordering,
            search=search,
            page=page,
            page_size=page_size,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "VariantList200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _variant_list_serialize(
        self,
        name,
        start_date,
        end_date,
        is_ground_variant,
        is_space_variant,
        exclude_space,
        exclude_ground,
        combat_time_source,
        combat_time_threshold,
        ordering,
        search,
        page,
        page_size,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if name is not None:
            
            _query_params.append(('name', name))
            
        if start_date is not None:
            
            _query_params.append(('start_date', start_date))
            
        if end_date is not None:
            
            _query_params.append(('end_date', end_date))
            
        if is_ground_variant is not None:
            
            _query_params.append(('is_ground_variant', is_ground_variant))
            
        if is_space_variant is not None:
            
            _query_params.append(('is_space_variant', is_space_variant))
            
        if exclude_space is not None:
            
            _query_params.append(('exclude_space', exclude_space))
            
        if exclude_ground is not None:
            
            _query_params.append(('exclude_ground', exclude_ground))
            
        if combat_time_source is not None:
            
            _query_params.append(('combat_time_source', combat_time_source))
            
        if combat_time_threshold is not None:
            
            _query_params.append(('combat_time_threshold', combat_time_threshold))
            
        if ordering is not None:
            
            _query_params.append(('ordering', ordering))
            
        if search is not None:
            
            _query_params.append(('search', search))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if page_size is not None:
            
            _query_params.append(('page_size', page_size))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Basic'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/variant/',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def variant_read(
        self,
        name: Annotated[StrictStr, Field(description="A unique value identifying this variant.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Variant:
        """variant_read

        Variant API

        :param name: A unique value identifying this variant. (required)
        :type name: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._variant_read_serialize(
            name=name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Variant",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def variant_read_with_http_info(
        self,
        name: Annotated[StrictStr, Field(description="A unique value identifying this variant.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Variant]:
        """variant_read

        Variant API

        :param name: A unique value identifying this variant. (required)
        :type name: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._variant_read_serialize(
            name=name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Variant",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def variant_read_without_preload_content(
        self,
        name: Annotated[StrictStr, Field(description="A unique value identifying this variant.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """variant_read

        Variant API

        :param name: A unique value identifying this variant. (required)
        :type name: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._variant_read_serialize(
            name=name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Variant",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _variant_read_serialize(
        self,
        name,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if name is not None:
            _path_params['name'] = name
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Basic'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/variant/{name}/',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


