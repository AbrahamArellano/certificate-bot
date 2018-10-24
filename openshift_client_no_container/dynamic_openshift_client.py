import os
import yaml
from kubernetes import client, config
from openshift.dynamic import DynamicClient

k8s_client = config.new_client_from_config()
dyn_client = DynamicClient(k8s_client)

v1_routes = dyn_client.resources.get(api_version='route.openshift.io/v1', kind='Route')

project_namespace = input("Provide Openshift namespace: ")
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
