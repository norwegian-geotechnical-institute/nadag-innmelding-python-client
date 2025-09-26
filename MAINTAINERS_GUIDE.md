# Maintainers Guide

See the [Makefile](./Makefile) if you need to install and test locally. Just type `make` to get the help.

Or just follow these steps:

## For new API version

1. Copy and rename the openapi.yaml the `openapi_specification/nadag-innmelding.yaml`
2. ~~Update the version number in the `config.yaml` file~~ (not needed anymore, as version number now in the openapi file)  
3. Run the following command to generate the client code:
   ```bash
    uvx openapi-python-client generate --path openapi_specification/nadag-innmelding.yaml --overwrite --custom-template-path=templates --config config.yaml
    ```
4. Check in the changes to the repository (files updated, added, or removed).
5. In the GitHub project, create a new release and the package should be published to PyPi.