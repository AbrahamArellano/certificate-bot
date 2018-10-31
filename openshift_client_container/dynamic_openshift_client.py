import os
import yaml
import openshift.config
import openshift.client
from openshift.dynamic import DynamicClient

openshift.config.load_incluster_config()

api_client = openshift.client.ApiClient()
dyn_client = DynamicClient(api_client)

v1_routes = dyn_client.resources.get(api_version='route.openshift.io/v1', kind='Route')

project_namespace = os.getenv("OPENSHIFT_BUILD_NAMESPACE")
route_list = v1_routes.get(namespace=project_namespace)

print("+++++++++++++++")
print(route_list)
print("+++++++++++++++")

for route in route_list.items:
	print("Route:")
	print("Name: " + route.metadata.name)
	if route.spec.tls is not None:
		if route.spec.tls.certificate != None:
			print("Certificate: " + route.spec.tls.certificate)
		if route.spec.tls.key != None:
			print("Key: " + route.spec.tls.key)
		if route.spec.tls.caCertificate != None:
			print("CA Certificate: " + route.spec.tls.caCertificate)
		if route.spec.tls.destinationCACert != None:
			print("Destination CA Certificate: " + route.spec.tls.destinationCACert)
	print("+++++++++++++++")
	
	
	
## Patching route

# Sample variables
route_to_be_patched="mytestapp"
newCaCertificate="MyPatchedCert"
newKey="MyPatchedKey"

# General structure of the route to be patched
body = {

    'kind': 'Route',

    'apiVersion': 'v1',

    'metadata': {'name': route_to_be_patched},

    'spec': {

        'tls': {'caCertificate': newCaCertificate, 'key': newKey},

    }

}

# Single patch
v1_routes.patch(body=body, namespace=project_namespace)

print("Route patched")


## Multiple patches

v1_lists = dyn_client.resources.get(api_version='route.openshift.io/v1', kind='List')

# In case you want to use a list of routes
body_list = {
    "kind": "List",
    "apiVersion": "v1",
    "items": [
        {
            "kind": "Route",
            "apiVersion": "v1",
            "metadata": {
                "name": "mytestapp"
            },
            "spec": {
                "tls": {
                    "termination": "edge",
                    "certificate": "MyCertificate",
                    "key": "MyPatchedKey",
                    "caCertificate": "MyPatchedCert"
                },
                "wildcardPolicy": "None"
            }
        },
        {
            "kind": "Route",
            "apiVersion": "v1",
            "metadata": {
                "name": "mytestapp2"
            },
            "spec": {
                "tls": {
                    "termination": "edge",
                    "certificate": "MyCertificate",
                    "key": "MyPatchedKey",
                    "caCertificate": "MyPatchedCert"
                },
                "wildcardPolicy": "None"
            }
        }
    ]
}

# Multiple patches
v1_lists.patch(body=body_list, namespace=project_namespace)

