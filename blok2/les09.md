# Les 9: Specifieke properties voor het SAA
Bij het Stadsarchief Amsterdam stellen we andere eisen aan verschillende RecordSet (bijvoorbeeld: archiefvormer verplicht bij :Archiefblok, maar niet bij :Groep) of een Record (we willen een vervaardiger bij :Afbeelding, maar niet bij :Akte). Voor elke entiteit in de Blauwdruk hebben we daarom een eigen shape gedefinieerd.

Daarom definieren we onze eigen Classes, die we 'ophangen' in de RiC-O ontologie. We kunnen dan gebruik maken van de mogelijkheden die de ontologie ons biedt en onze eigen eisen stellen aan onze eigen data. Dat doen we in onze eigen ontologie.

```
@prefix rdf:           <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:          <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:           <http://www.w3.org/2001/XMLSchema#> .
@prefix sh:            <http://www.w3.org/ns/shacl#> .
@prefix rico:          <https://www.ica.org/standards/RiC/ontology#> .
@prefix saa:           <https://id.archief.amsterdam/recordtypes/> .

saa:Fonds a sh:NodeShape , rdf:Class ;
    sh:targetClass saa:Fonds ;
    rdfs:subClassOf rico:RecordSet ;
    rdfs:label "Archiefblok" ;
    sh:property [
        sh:path rico:hasAccumulator ;
        sh:class rico:Agent ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
    ] ;
    sh:property [
        sh:path rico:beginningDate ;
        sh:datatype xsd:date ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
    ] ;
    sh:property [
        sh:path saa:internalRemarks ;
        sh:datatype xsd:string ;
    ] .

```

We moeten dan wel ons eigen ding de rdf:type saa:Fonds meegeven:
```
@prefix rdf:           <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:          <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:           <http://www.w3.org/2001/XMLSchema#> .
@prefix rico:          <https://www.ica.org/standards/RiC/ontology#> .
@prefix saa:           <https://id.archief.amsterdam/recordtypes/> .
@prefix ric-rst:       <https://www.ica.org/standards/RiC/vocabularies/recordSetTypes#> .

<https://id.archief.amsterdam/8>
    rdf:type saa:Fonds ;
    rdfs:label "Het Archief van het Weeshuis" ;
    rico:hasAccumulator [
        rdf:type rico:Agent ;
        rdfs:label "Het Weeshuis" ;
        ] ;
    rico:beginningDate "1673-02-28"^^xsd:date ;
    rico:hasRecordSetType ric-rst:Fonds .
```

Ga naar [Les 10: SHACL als formulierdefinitie](les10.md)
