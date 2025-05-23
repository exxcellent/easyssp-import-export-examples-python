from easyssp_auth import AuthError
from easyssp_import_export.client.import_export_client import ImportExportClient
from easyssp_utils.client import ApiException
from pydantic import ValidationError
from demo_config import USER_AGENT, EASYSSP_USERNAME, EASYSSP_PASSWORD

with (open("../input/ssd_example.ssd", "rb") as ssd_input_file):
    try:
        import_export_client = ImportExportClient(username=EASYSSP_USERNAME, password=EASYSSP_PASSWORD,
                                                  user_agent=USER_AGENT)
        # import a .ssd file
        ssd_import_result = import_export_client.import_ssd(filename="ssd_import_example.ssd",
                                                            body=ssd_input_file.read())
        print(ssd_import_result.data)
    # catch ValidationError for incorrect request parameters
    # catch ApiException for errors from the API client or the server
    except (AuthError, ApiException, ValidationError) as ex:
        print(ex)
