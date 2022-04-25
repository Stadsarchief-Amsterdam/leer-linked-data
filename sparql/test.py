#! /usr/bin/env python3
# We moeten regelmatig controleren of de antwoorden op de opdrachten het nog doen. Dit script automatiseert deze test. 
# Dit script zoekt de antwoorden op uit de markdown-bestanden (TODO), vuurt de query af en controleert of er een adequate response terugkomt.

import urllib
import SPARQLWrapper

# voorbereiden: volledige queries in de request-url opnemen bij de opdrachten, ipv de short-versie.

# parsen *.md files op zoek naar antwoorden bij opdrachten
# nu, om te testen deze standaard requestUrl:
requestUrl = 'http://yasgui.triply.cc/#query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT%20*%20WHERE%20%7B%0A%20%20%3Chttp%3A%2F%2Fdbpedia.org%2Fresource%2FHarry_Mulisch%3E%20rdfs%3Alabel%20%3Flabel%20.%0A%7D%20&endpoint=https%3A%2F%2Fdbpedia.org%2Fsparql&requestMethod=POST&tabTitle=Query&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table'

# request opknippen en decoden
requestString = requestUrl.replace('http://yasgui.triply.cc/#','')
requestDict = urllib.parse.parse_qs(requestString)

sparqlQuery = requestDict['query'][0]
endpointUrl = requestDict['endpoint'][0]

# sparql-query afvuren op endpoint
sparqlEndpoint = SPARQLWrapper.SPARQLWrapper(endpointUrl)
sparqlEndpoint.setQuery(sparqlQuery)
sparqlEndpoint.setReturnFormat(SPARQLWrapper.JSON)

# controleren of (http reply == 200) AND (len(data_reply) > 0) 

try:
    queryResults = sparqlEndpoint.queryAndConvert()

    for r in queryResults["results"]["bindings"]:
        print(r)

except Exception as e:
    print(e)
