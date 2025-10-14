# Maintainers Guide

This procedure is not automated and run regularly in github. If the source OpenAPI file has changed, a PR is created. 
You only need to create a new release in GitHub to publish the new version to PyPi.

See the [Makefile](./Makefile) if you need to install and test locally. Just type `make` to get the help.

Or just follow these steps:

## For new API version

1. Copy and rename the source openapi file the `openapi_specification/nadag-innmelding.yaml`
2. Run the following command to generate the client code:
   ```bash
    uvx openapi-python-client generate --path openapi_specification/nadag-innmelding.yaml --overwrite --custom-template-path=templates --config config.yaml --meta=uv
    ```
3. Check in the changes to the repository (files updated, added, or removed).
4. In the GitHub project, create a new release and the package should be published to PyPi.