from easyssp_auth import AuthError
from easyssp_import_export.client.import_export_client import ImportExportClient
from easyssp_utils.client import ApiException
from pydantic import ValidationError

USER_AGENT = "easyssp-import-export-examples-python"

with (
    open("../input/ssp_example.ssp", "rb") as ssp_input_file,
    open("../output/ssp_output.ssp", "wb") as ssp_output_file,
    open("../input/ssd_example.ssd", "rb") as ssd_input_file,
    open("../output/ssd_output.ssp", "wb") as ssd_output_file,
):
    try:
        import_export_client = ImportExportClient(username="your_easyssp_username", password="your_easyssp_password",
                                                  user_agent=USER_AGENT)

        # .ssp file import and export
        # import a .ssp file
        ssp_import_result = import_export_client.import_ssp(filename="ssp_import_example.ssp",
                                                            body=ssp_input_file.read())
        # export it to .ssp file
        ssp_export_result = import_export_client.export_ssp(ssp_id=ssp_import_result.data.id)
        ssp_output_file.write(ssp_export_result.data)  # write the exported file to the file system

        # .ssd file import and export
        # import a .ssd file
        ssd_import_result = import_export_client.import_ssd(filename="ssd_import_example.ssd",
                                                            body=ssd_input_file.read())
        # export it to .ssp file
        ssd_export_result = import_export_client.export_ssp(ssp_id=ssd_import_result.data.id)
        ssd_output_file.write(ssd_export_result.data)  # write the exported file to the file system
    # catch ValidationError for incorrect request parameters
    # catch ApiException for errors from the API client or the server
    except (AuthError, ApiException, ValidationError) as ex:
        print(ex)
