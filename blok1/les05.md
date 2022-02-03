# Les 5: Blanknodes - nodes in het netwerk zonder naam
Hieronder is een complete beschrijving van een archief.

```
@prefix rdf:           <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:          <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rico:          <https://www.ica.org/standards/RiC/ontology#> .
@prefix ric-rst:       <https://www.ica.org/standards/RiC/vocabularies/recordSetTypes#> .
@prefix xsd:        <http://www.w3.org/2001/XMLSchema#> .

<https://id.archief.amsterdam/4> 
	rdf:type rico:RecordSet ;
	rdfs:label "Archief van Een Of Ander Instituut" ;
	rico:hasRecordSetType ric-rst:Fonds ;
    rico:hasAccumulator <https://id.archief.amsterdam/5> ;
    rico:hasOrHadIdentifier [
        a rico:Identifier ;
        rico:hasIdentifierType <https://id.archief.amsterdam/6> ; 
        rico:textualValue "395"
    ] ;
    rico:hasOrHadTitle [
        a rico:Title ;
        rico:textualValue "Archief van Een Of Ander Instituut"
    ] ;
    rico:isAssociatedWithDate [
        a rico:DateRange ;
        rico:expressedDate "1823 - 1972" ;
        rico:hasBeginningDate [
            a rico:SingleDate ;
            rico:normalizedDateValue "1823"^^xsd:gYear
        ] ;
        rico:hasEndDate [
            a rico:SingleDate ;
            rico:normalizedDateValue "1972"^^xsd:gYear
        ]
    ] ;
    rico:isOrWasDescribedBy [
        a rico:Record ;
        rico:hasDocumentaryFormType <https://www.ica.org/standards/RiC/vocabularies/documentaryFormTypes#FindingAid> ;
        rico:hasOrHadTitle [
            a rico:Title ;
            rico:textualValue "Inventaris van het Archief van Een Of Ander Instituut"
        ] ;
        rico:hasPublisher <https://id.archief.amsterdam/7> ;
    ] ;
    rico:scopeAndContent "blabla" .

<https://id.archief.amsterdam/5>
	a rico:Organization ;
	rdfs:label "Een Of Ander Instituut" .

<https://id.archief.amsterdam/6>
	a rico:IdentifierType ;
	rdfs:label "Toegangsnummer" .

<https://id.archief.amsterdam/7>
	a rico:Organization ;
	rdfs:label "Stadsarchief Amsterdam" .


```

Je ziet hier een heleboel _blanknodes_. Omdat deze geen naam hebben kan GraphDB ze niet visualiseren, en kun je ook niet rechtstreeks aan ze refereren. Maar ze zijn er wel. Er is nu dus een pad in de graaf van <https://id.archief.amsterdam/2> naar de begindatum van de vorming. Dit pad volgt deze relaties: rico:isAssociatedWith/rico:hasBeginningDate/rico:normalizedDateValue. 

Ga naar [Les 06: Mijn eerste SPARQL-query](les06.md)
