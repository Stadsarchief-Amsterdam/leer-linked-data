### Les 6: Onze eerste Shapes
Een ontologie verschilt van een datamodel in dat er in een ontologie (en daarmee volgens de principes van Linked Data) geen verplichtingen zijn over welke properties er wel of niet zijn. Deze vrijheid die Linked Data biedt is niet altijd handig. Soms moet je gewoon zeker weten dat er een plaats in het depot is vastgelegd bijvoorbeeld. En ook kunnen controleren dat dit verplichte veld is ingevuld. Daarvoor gebruiken we SHACL (Shapes Constraint Language). Bij het Stadsarchief Amsterdam stellen we bijvoorbeeld als randvoorwaarde (_constraint_) dat bij een Archiefblok precies 1 archiefvormer moet worden vastgelegd. In SHACL leggen we dat als volgt vast:

```
@prefix rdf:           <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:          <http://www.w3.org/2000/01/rdf-schema#> .
@prefix saa:           <https://id.archief.amsterdam/recordtypes/> .
@prefix sh:            <http://www.w3.org/ns/shacl#> .
@prefix rico:          <https://www.ica.org/standards/RiC/ontology#> .

saa:Fonds a sh:NodeShape;
    sh:targetClass rico:RecordSet ;
    rdfs:label "Archiefblok" ;
    sh:property [
        sh:path rico:hasAccumulator ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
    ] .
```

Lees deze graaf in. 
("Import" -> "RDF" -> "Import RDF Text Snippet")  

Kies bij het importeren als naam voor de graaf: http://rdf4j.org/schema/rdf4j#SHACLShapeGraph. Door het deze naam te geven weet GraphDB dat ze de shapes in deze graaf moet gebruiken om te valideren bij het importeren.

Ga naar [Les 07: Data valideren](les07.md)


