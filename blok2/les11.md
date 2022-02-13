# Les 11: SHACL en Memorix
Ook Picturae heeft als basis voor het definieren van een recordtype SHACL gekozen als standaard. Memorix stelt een paar extra eisen aan de recordtype definitie.
* sh:order, sh:group en rdfs:label (zie hierboven) zijn verplicht bij een property
* een sh:NodeShape moet *ook* gedefinieerd worden als een memorix:Recordtype.
* Een memorix:Recordtype *moet* bevatten: dc:identifier, sh:ignoredProperties en sh:closed (en deze laatste moet *true* zijn).
* er moet een dynamisch pad zijn in de prefix
* er zijn properties memorix:inTitleAt en memorix:inSummaryAt

Dus:
```
@prefix rdf:           <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:          <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:           <http://www.w3.org/2002/07/owl#> .
@prefix xsd:           <http://www.w3.org/2001/XMLSchema#> .
@prefix dc:            <http://purl.org/dc/elements/1.1/> .                   # <======
@prefix sh:            <http://www.w3.org/ns/shacl#> .
@prefix dash:          <http://datashapes.org/dash#> .                        # <======
@prefix memorix:       <http://memorix.io/ontology#> .                        # <======
@prefix rico:          <https://www.ica.org/standards/RiC/ontology#> .
@prefix fonds:         </resources/recordtypes/> .                            # <======

blauwdruk:VeldenGroep a sh:PropertyGroup ;
    rdfs:label "Groepering van de velden"@nl ;
    sh:order 1.0 .

blauwdruk:Blablabla a sh:NodeShape , memorix:Recordtype;                      # <======
    sh:targetClass saa:Fonds ;
    rdfs:label "Archiefblok" ;
    dc:identifier "Fonds" ;                                                   # <======
    sh:ignoredProperties ( rdf:type ) ;                                       # <======
    sh:closed true ;                                                          # <======
    sh:property [
        rdfs:label "Archiefnummer"@nl , "Number of the Fonds"@en ;
        sh:path rico:identifier ;
        sh:datatype xsd:integer ;
        memorix:inTitleAt 1.0 ;                                               # <======
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:group blauwdruk:VeldenGroep ;
        sh:order 1.0
    ] ;
    sh:property [
        rdfs:label "Beschrijving"@nl , "Title"@en ;
        sh:path rico:title ;
        sh:datatype xsd:string ;
        memorix:inTitleAt 2.0 ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:group blauwdruk:VeldenGroep ;
        sh:order 2.0
    ] ;
    sh:property [
        rdfs:label "Begindatum archiefvorming"@nl , "Beginning date Accumulation"@en ;
        sh:path rico:beginningDate ;
        sh:datatype xsd:date ;
        memorix:inSummaryAt 1.0 ;                                             # <======
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:group blauwdruk:VeldenGroep ;
        sh:order 3.0
    ] .
```

Het leuke is: om de RecordType SHACL file te controleren heeft Picturae zelf een SHACL-file ingebouwd ...

Op basis van dit memorix:Recordtype genereert Memorix dit record:

```
@prefix blauwdruk: <https://example.memorix-test.nl/resources/recordtypes/> .
@prefix dash:      <http://datashapes.org/dash#> .
@prefix dc:        <http://purl.org/dc/elements/1.1/> .
@prefix dcterms:   <http://purl.org/dc/terms/> .
@prefix fondsTest: <https://example.memorix-test.nl/resources/recordtypes/FondsTest#> .
@prefix memorix:   <http://memorix.io/ontology#> .
@prefix owl:       <http://www.w3.org/2002/07/owl#> .
@prefix rdf:       <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:      <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rico:      <https://www.ica.org/standards/RiC/ontology#> .
@prefix schema:    <http://schema.org/> .
@prefix sh:        <http://www.w3.org/ns/shacl#> .
@prefix skos:      <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd:       <http://www.w3.org/2001/XMLSchema#> .

<https://example.memorix-test.nl/resources/records/cb9bb7f0-694b-4689-8e8c-2a42d607996f>
        rdf:type            saa:Fonds , memorix:Record ;
        rico:beginningDate  "2021-12-08"^^xsd:date ;
        rico:identifier     4 ;
        rico:title          "Archief van Ivo" .
```

Voor een compleet voorbeeld van een Memorix recordtype klik [hier](../memorix-recordtype-example.ttl).

Einde blok 2