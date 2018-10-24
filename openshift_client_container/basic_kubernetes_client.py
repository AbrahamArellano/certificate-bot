import sys
import os
from kubernetes import client
from kubernetes.client.rest import ApiException

def main():
    SERVICE_TOKEN_FILENAME = "/var/run/secrets/kubernetes.io/serviceaccount/token"
    SERVICE_CERT_FILENAME = "/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"
    KUBERNETES_HOST = "https://%s:%s" % (os.getenv("KUBERNETES_SERVICE_HOST"), os.getenv("KUBERNETES_SERVICE_PORT"))

    ## configure 
    configuration = client.Configuration()
    configuration.host = KUBERNETES_HOST
    if not os.path.isfile(SERVICE_TOKEN_FILENAME):
        raise ApiException("Service token file does not exists.")
    with open(SERVICE_TOKEN_FILENAME) as f:
        token = f.read()
        if not token:
            raise ApiException("Token file exists but empty.")
        configuration.api_key['authorization'] = "bearer " + token.strip('\n')
    if not os.path.isfile(SERVICE_CERT_FILENAME):
        raise ApiException("Service certification file does not exists.")
    with open(SERVICE_CERT_FILENAME) as f:
        if not f.read():
            raise ApiException("Cert file exists but empty.")
        configuration.ssl_ca_cert = SERVICE_CERT_FILENAME
    client.Configuration.set_default(configuration)

    try:
        ret = client.CoreV1Api().list_namespaced_config_map("rest-project")
        print ret
    except ApiException as e:
        print("Exception when calling CoreV1Api->list_namespaced_config_map: %s\n" % e)

if __name__ == '__main__':
    main()