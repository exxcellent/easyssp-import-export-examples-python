from easyssp_auth import AuthError
from easyssp_import_export.client.import_export_client import ImportExportClient
from easyssp_utils.client import ApiException
from pydantic import ValidationError
from demo_config import USER_AGENT, EASYSSP_USERNAME, EASYSSP_PASSWORD

with (open("../output/ssp_output.ssp", "wb") as ssp_output_file):
    try:
        import_export_client = ImportExportClient(username=EASYSSP_USERNAME, password=EASYSSP_PASSWORD,
                                                  user_agent=USER_AGENT)
        # get the SSP model id from the console
        ssp_id = input("Enter SSP model id: ")

        # export it to .ssp file
        ssp_export_result = import_export_client.export_ssp(ssp_id=ssp_id)
        ssp_output_file.write(ssp_export_result.data)  # write the exported file to the file system
        print("The SSP model has been successfully exported.")
    # catch ValidationError for incorrect request parameters
    # catch ApiException for errors from the API client or the server
    except (AuthError, ApiException, ValidationError) as ex:
        print(ex)
