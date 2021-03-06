# Les 5: Blanknodes - nodes in het netwerk zonder naam
Hieronder is een nog completere beschrijving van een archief. Loop het even rustig langs om te kijken of je begrijpt wat er is vastgelegd.

```
@prefix rdf:           <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:          <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rico:          <https://www.ica.org/standards/RiC/ontology#> .
@prefix ric-rst:       <https://www.ica.org/standards/RiC/vocabularies/recordSetTypes#> .
@prefix xsd:           <http://www.w3.org/2001/XMLSchema#> .

<https://id.archief.amsterdam/4> 
	rdf:type rico:RecordSet ;
	rdfs:label "Archief van Een Of Ander Instituut" ;
	rico:hasRecordSetType ric-rst:Fonds ;
    rico:hasAccumulator <https://id.archief.amsterdam/5> ;
    rico:hasOrHadIdentifier [
        rdf:type rico:Identifier ;
        rico:hasIdentifierType <https://id.archief.amsterdam/6> ; 
        rico:textualValue "395"
    ] ;
    rico:hasOrHadTitle [
        rdf:type rico:Title ;
        rico:textualValue "Archief van Een Of Ander Instituut"
    ] ;
    rico:isAssociatedWithDate [
        rdf:type rico:DateRange ;
        rico:expressedDate "1823 - 1972" ;
        rico:hasBeginningDate [
            rdf:type rico:SingleDate ;
            rico:normalizedDateValue "1823"^^xsd:gYear
        ] ;
        rico:hasEndDate [
            rdf:type rico:SingleDate ;
            rico:normalizedDateValue "1972"^^xsd:gYear
        ]
    ] ;
    rico:isOrWasDescribedBy [
        rdf:type rico:Record ;
        rico:hasDocumentaryFormType <https://www.ica.org/standards/RiC/vocabularies/documentaryFormTypes#FindingAid> ;
        rico:hasOrHadTitle [
            rdf:type rico:Title ;
            rico:textualValue "Inventaris van het Archief van Een Of Ander Instituut"
        ] ;
        rico:hasPublisher <https://id.archief.amsterdam/7> ;
    ] ;
    rico:scopeAndContent "blabla" .

<https://id.archief.amsterdam/5>
	rdf:type rico:CorporateBody ;
	rdfs:label "Een Of Ander Instituut" .

<https://id.archief.amsterdam/6>
	rdf:type rico:IdentifierType ;
	rdfs:label "Toegangsnummer" .

<https://id.archief.amsterdam/7>
	rdf:type rico:CorporateBody ;
	rdfs:label "Stadsarchief Amsterdam" .


```

Je ziet hier een heleboel _blanknodes_. Omdat deze geen naam hebben kan GraphDB ze niet visualiseren, en kun je ook niet rechtstreeks aan ze refereren. Maar ze zijn er wel. Er is nu dus een pad in de graaf van <https://id.archief.amsterdam/4> naar de begindatum van de vorming. Dit pad volgt deze relaties: rico:isAssociatedWith/rico:hasBeginningDate/rico:normalizedDateValue. 

Voeg deze triples toe aan de repository in GraphDB ("Import" -> "RDF" -> "Import RDF Text Snippet")

Wat is de begindatum van de archiefvorming?

Ga naar [Les 06: Mijn eerste SPARQL-query](les06.md)
