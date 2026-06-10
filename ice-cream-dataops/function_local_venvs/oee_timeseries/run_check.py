import os
import sys

from pathlib import Path
from pprint import pprint

from cognite.client import CogniteClient, ClientConfig
from cognite.client.credentials import OAuthClientCredentials

# This is necessary to import adjacent modules in the function code.
sys.path.insert(0, str(Path(__file__).parent / "local_code"))

from local_code.handler import handle # noqa: E402

try:
    from dotenv import load_dotenv

    for parent in Path(__file__).resolve().parents:
        if (parent / ".env").exists():
            load_dotenv(parent / '.env')
except ImportError:
    ...


def main() -> None:
    credentials = OAuthClientCredentials(
        token_url="https://login.microsoftonline.com/afd5c01e-f493-4cd1-b9f9-2a801c00d3c9/oauth2/v2.0/token",
        client_id="12e78bfe-608a-4fd6-9982-bb878a0c184c",
        client_secret=os.environ["DATA_PIPELINE_OEE_CLIENT_SECRET"],
        scopes=['https://bluefield.cognitedata.com/.default'],
    )

    client = CogniteClient(
        config=ClientConfig(
            client_name="CDF-Toolkit:0.6.53",
            project="test-cdf-project",
            base_url="https://bluefield.cognitedata.com",
            credentials=credentials,
        )
    )

    print("oee_timeseries LOGS:")
    response = handle(
        client=client,
        data={},
    )

    print("oee_timeseries RESPONSE:")
    pprint(response)


if __name__ == "__main__":
    main()
