# -*- coding: utf-8 -*-

import httplib, urllib
import json

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the accessKey string value with your valid access key.
accessKey = '2f95a0b225b141c290a3a1d4f2f7e87a'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your access keys.
# For example, if you obtained your access keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial access keys are generated in the westcentralus region, so if you are using
# a free trial access key, you should not need to change this region.
uri = 'northeurope.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/sentiment'

def GetMultipleSentiment (documents):
    "Gets the sentiments for a set of documents and returns the information."

    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection (uri)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse ()
    return response.read ()

documents = { 'documents': [
    { 'id': '1', 'language': 'en', 'text': 'I really enjoy the new XBox One S. It has a clean look, it has 4K/HDR resolution and it is affordable.' },
    { 'id': '2', 'language': 'es', 'text': 'Este ha sido un dia terrible, llegué tarde al trabajo debido a un accidente automobilistico.' },
    { 'id': '3', 'language': 'en', 'text': 'My day is great.'},
    { 'id': '4', 'language': 'en', 'text': 'My day is incredibly dead.'}
]}

def GetSentiment (text):
    "Gets the sentiments for a set of documents and returns the information."

    filled_in_documents = { 'documents': [{ 'id': '0', 'language': 'en', 'text': text }]}
    # print(filled_in_documents);

    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection (uri)
    body = json.dumps (filled_in_documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse ()
    return response.read ()

documents = { 'documents': [
    { 'id': '0', 'language': 'en', 'text': 'I really enjoy the new XBox One S. It has a clean look, it has 4K/HDR resolution and it is affordable.' }
]}

print 'Please wait a moment for the results to appear.\n'

# result = GetMultipleSentiment (documents)
# print (json.dumps(json.loads(result), indent=4))

print(json.dumps(json.loads(GetSentiment("This is absolutely terrible")), indent=4))