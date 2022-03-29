# Les 3: Een RiC-O voorbeeld in turtle

Laten we metadata van een ander archief aan de graaf toevoegen.

```
@prefix rdf:           <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:          <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rico:          <https://www.ica.org/standards/RiC/ontology#> .
@prefix ric-rst:       <https://www.ica.org/standards/RiC/vocabularies/recordSetTypes#> .

<https://id.archief.amsterdam/2> 
	rdf:type rico:RecordSet ;
	rdfs:label "Archief van de Familie Boissevain en Aanverwante Families" ;
	rico:hasRecordSetType ric-rst:Fonds ;
    rico:hasAccumulator <https://id.archief.amsterdam/3> .

<https://id.archief.amsterdam/3>
	rdf:type rico:Family ;
	rdfs:label "Familie Boissevain" . 
```

Elk ding heeft hier een rdfs:label gekregen. Dat is handig omdat alle tools die linked data 'doen' hiermee overweg kunnen.

Lees ook de data over dit archief in, in GraphDB.
("Import" -> "RDF" -> "Import RDF Text Snippet")

Ga naar [Les 04: Visualisatie in GraphDB](les04.md)
