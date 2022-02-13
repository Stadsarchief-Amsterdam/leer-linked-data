# Les 10: SHACL als formulierdefinitie
En nu maken we een denksprong. Als we dit soort randvoorwaarden vastleggen in SHACL, kunnen we die randvoorwaarden gebruiken om te valideren, maar legt het ook eenduidig vast hoe het scherm van de gebruikersinterface eruit ziet. Bij de bovenstaande NodeShape zal er dus voor een Archiefblok drie velden op het scherm moeten zijn, en het systeem kan aangeven dat ze niet wil opslaan, als er niet een verplichte archiefvormer en datum zijn ingevuld. We hebben wat aanvullende informatie nodig: we willen de volgorde vastleggen en misschien willen we de velden groeperen in blokken op het scherm. Memorix maakt gebruik van dit idee om drie vliegen in een klap te slaan: met zo'n SHACL-nodeshape-met aanvullingen leggen we de datadefinitie vast, kunnen we de data correct houden en de gebruikersinterface definieren. Volgende keer gaan we daar naar kijken.

Er zijn een aantal aanvullingen noodzakelijk om van een graaf met shapes in SHACL een formulier in een gebruikersinterface te kunnen genereren. De volgende zaken zijn daarbij van belang:
* een label om bij het veld op het formulier te laten zien
* de volgorde waarin de velden in het formulier moeten worden opgenomen
* eventueel een groepering van de velden

Al deze zaken zijn gedefinieerd in SHACL zelf, rdfs:label, sh:order, sh:group.

Dus, bijvoorbeeld:
```
@prefix rdf:           <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:          <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:           <http://www.w3.org/2002/07/owl#> .
@prefix xsd:           <http://www.w3.org/2001/XMLSchema#> .
@prefix sh:            <http://www.w3.org/ns/shacl#> .
@prefix rico:          <https://www.ica.org/standards/RiC/ontology#> .

blauwdruk:VeldenGroep a sh:PropertyGroup ;                              # <======
    rdfs:label "Groepering van de velden"@nl ;                          # <======
    sh:order 1.0 .                                                      # <======

blauwdruk:FondsTest a sh:NodeShape , owl:Class ;
    sh:targetClass blauwdruk:FondsTest ;
    rdfs:subClassOf rico:RecordSet ;
    rdfs:label "Archiefblok" ;
    sh:property [
        rdfs:label "Archiefnummer"@nl , "Number of the Fonds"@en ;
        sh:path rico:identifier ;
        sh:datatype xsd:integer ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:group blauwdruk:VeldenGroep ;                                # <======
        sh:order 1.0                                                    # <======
    ] ;
    sh:property [
        rdfs:label "Beschrijving"@nl , "Title"@en ;
        sh:path rico:title ;
        sh:datatype xsd:string ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:group blauwdruk:VeldenGroep ;                                # <======
        sh:order 2.0                                                    # <======
    ] ;
    sh:property [
        rdfs:label "Begindatum archiefvorming"@nl , "Beginning date Accumulation"@en ;
        sh:path rico:beginningDate ;
        sh:datatype xsd:date ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:group blauwdruk:VeldenGroep ;                                # <======
        sh:order 3.0                                                    # <======           
    ] .
```

Ga naar [Les 11: SHACL en Memorix](les11.md)
