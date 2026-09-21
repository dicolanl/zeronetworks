# Copyright (c) 2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Splunk SOAR app for Zero Networks.

Connects to the Zero Networks portal API.
"""

from soar_sdk.app import App
from soar_sdk.asset import AssetField, BaseAsset
from soar_sdk.logging import getLogger

from .client import build_client, request_json
from .consts import CONNECTIVITY_ENDPOINT, DEFAULT_BASE_URL

logger = getLogger()

APP_ID = "85010388-bc3f-48a9-af39-0af675dcd405"


class Asset(BaseAsset):
    """Connection details for a Zero Networks tenant."""

    base_url: str = AssetField(
        default=DEFAULT_BASE_URL,
        description="Zero Networks portal API base URL",
    )
    api_token: str = AssetField(
        sensitive=True,
        description="Zero Networks API token, sent in the Authorization header",
    )
    verify_server_cert: bool = AssetField(
        default=True,
        description="Verify the TLS certificate presented by the Zero Networks portal",
    )


app = App(
    name="zeronetworks",
    app_type="network security",
    logo="logo.svg",
    logo_dark="logo_dark.svg",
    product_vendor="Zero Networks",
    product_name="Zero Networks Segment",
    publisher="Splunk Inc.",
    appid=APP_ID,
    fips_compliant=True,
    encrypt_cache_state=True,
    encrypt_ingest_state=True,
    asset_cls=Asset,
)


@app.test_connectivity()
def test_connectivity(asset: Asset) -> None:
    """Verify that the configured token can reach and authenticate to Zero Networks."""
    logger.progress(f"Connecting to {asset.base_url}")

    with build_client(
        asset.base_url, asset.api_token, asset.verify_server_cert
    ) as client:
        request_json(client, "GET", CONNECTIVITY_ENDPOINT, context="Connectivity test")

    logger.progress("Connectivity test passed")


if __name__ == "__main__":
    app.cli()
