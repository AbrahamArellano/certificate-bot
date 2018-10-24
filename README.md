# Openshift quickstart: CertBot

This is a [CertBot](http://www.CertBotproject.com) project that you can use as the starting point to develop your own and deploy it on an [OpenShift](https://github.com/openshift/origin) cluster.

The steps in this document assume that you have access to an OpenShift deployment that you can deploy applications on.

## What has been done for you

A Cron Job that check the certificates in the existing Routes in the Openshift namespace using a Python Dynamic client.

## Special files in this repository


```
openshift/         - OpenShift-specific files
├── scripts        - helper scripts
└── templates      - application templates


```

## Warnings

Please be sure to read the following warnings and considerations before running this code on your local workstation, shared systems, or production environments.

### Automatic test execution

The Cron Job will be triggered every 3 minutes and will print all available certificates from Routes.

## Local development

Use the script:

```
openshift_client_no_container/         - Python scripts
└── dynamic_openshift_client.py        - Dynamic python client


```


## Deploying to OpenShift

Use the following command to deploy/execute the Certificate Bot in Openshift:

oc new-app https://raw.githubusercontent.com/AbrahamArellano/django-ex/master/openshift/templates/certificate_watchdog_cronjob.json -p SOURCE_REPOSITORY_URL=https://github.com/AbrahamArellano/django-ex -p NAME=[APPLICATION_NAME] -p NAMESPACE=[OPENSHIFT_NAMESPACE] -p DOCKER_REGISTRY_SERVER_PORT=[REGISTRY_SERVER_IP]:[REGISTRY_SERVER_PORT]

## Special environment variables

###NAMESPACE:
Define the Openshift namespace name where the installation is done

###DOCKER_REGISTRY_SERVER_PORT: 
Define the docker registry server and port using the following syntax [SERVER]:[PORT]. Is relevant to mention that those values should be provided by the cluster administrator or checking the description of the image after it is deployed in the namespace.


## Looking for help

If you get stuck at some point, or think that this document needs further details or clarification, you can give feedback and look for help using the channels mentioned in [the OKD repo](https://github.com/openshift/origin), or by filing an issue.


## License

This code is dedicated to the public domain to the maximum extent permitted by applicable law, pursuant to [CC0](http://creativecommons.org/publicdomain/zero/1.0/).
