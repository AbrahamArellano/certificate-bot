import os
import openshift.client
import openshift.config

openshift.config.load_incluster_config()

api_client = openshift.client.ApiClient()
oapi_client = openshift.client.OapiApi(api_client)

project_namespace = input("Provide Openshift namespace: ")

route_list = oapi_client.list_namespaced_route(project_namespace)
print(route_list)