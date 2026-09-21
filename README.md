# zeronetworks

Publisher: Splunk Inc. <br>
Connector Version: 1.1.0 <br>
Product Vendor: Zero Networks <br>
Product Name: Zero Networks Segment <br>
Minimum Product Version: 7.0.0

Segment, quarantine and release assets managed by Zero Networks

### Configuration variables

This table lists the configuration variables required to operate zeronetworks. These variables are specified when configuring a Zero Networks Segment asset in Splunk SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base_url** | required | string | Zero Networks portal API base URL |
**api_token** | required | password | Zero Networks API token, sent in the Authorization header |
**verify_server_cert** | required | boolean | Verify the TLS certificate presented by the Zero Networks portal |

### Supported Actions

[test connectivity](#action-test-connectivity) - Verify that the configured token can reach and authenticate to Zero Networks.

## action: 'test connectivity'

Verify that the configured token can reach and authenticate to Zero Networks.

Type: **test** <br>
Read only: **True**

Basic test for app.

#### Action Parameters

No parameters are required for this action

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failure |
action_result.message | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

______________________________________________________________________

Auto-generated Splunk SOAR Connector documentation.

Copyright 2026 Splunk Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
