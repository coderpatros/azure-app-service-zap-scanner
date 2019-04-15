Azure App Service ZAP Scanner
=============================

Requires the Azure CLI.

Usage
-----

After performing an Azure CLI login and setting the subscription running
`scan.py` will enumerate all your app services and run a ZAP scan against them.

This will create a `<HOSTNAME>.xml` JUnit test results file for each app
service.

I'm assuming that you already enforce HTTPS only on your app services.
