# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import StorageImportExportConfiguration
from .operations_async import LocationOperations
from .operations_async import JobOperations
from .operations_async import BitLockerKeyOperations
from .operations_async import OperationOperations
from .. import models


class StorageImportExport(object):
    """The Storage Import/Export Resource Provider API.

    :ivar location: LocationOperations operations
    :vartype location: storage_import_export.aio.operations_async.LocationOperations
    :ivar job: JobOperations operations
    :vartype job: storage_import_export.aio.operations_async.JobOperations
    :ivar bit_locker_key: BitLockerKeyOperations operations
    :vartype bit_locker_key: storage_import_export.aio.operations_async.BitLockerKeyOperations
    :ivar operation: OperationOperations operations
    :vartype operation: storage_import_export.aio.operations_async.OperationOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param subscription_id: The subscription ID for the Azure user.
    :type subscription_id: str
    :param acceptlanguage: Specifies the preferred language for the response.
    :type acceptlanguage: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        acceptlanguage: Optional[str] = None,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = StorageImportExportConfiguration(credential, subscription_id, acceptlanguage, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.location = LocationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.job = JobOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.bit_locker_key = BitLockerKeyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "StorageImportExport":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
