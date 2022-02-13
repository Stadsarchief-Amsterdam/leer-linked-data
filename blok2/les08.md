# Les 8: Controleren op datatype en rdf:Class
De _inference_ die we hebben leren kennen in de les over ontologieen werkt natuurlijk pas goed als de data correct is. En een foutje is zo gemaakt. Daarom is het handig om bij zoveel mogelijk data aan te geven welke rdfs:Class de entiteit heeft. SHACL kan voor je controleren of je daarin geen fouten gemaakt hebt. Als er geen sprake is van een entiteit die is gekoppeld, kun je ook het datatype vastleggen.

```
@prefix rdf:           <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:          <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:           <http://www.w3.org/2001/XMLSchema#> .
@prefix sh:            <http://www.w3.org/ns/shacl#> .
@prefix rico:          <https://www.ica.org/standards/RiC/ontology#> .
@prefix saa:           <https://id.archief.amsterdam/recordtypes/> .

saa:Fonds a sh:NodeShape ;
    sh:targetClass rico:RecordSet ;
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
    ] .
```

Importeer deze nieuwe NodeShape. Dus: "Import" -> "RDF" -> "Import RDF Text Snippet" . Kies bij het importeren als naam voor de graaf: http://rdf4j.org/schema/rdf4j#SHACLShapeGraph. Merk op dat na het importeren de oude data wordt gevalideerd. Dus deze nieuwe SHACL file toevoegen werkt niet.

Importeer vervolgens onderstaande data:
("Import" -> "RDF" -> "Import RDF Text Snippet")


```
@prefix rdf:           <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:          <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:           <http://www.w3.org/2001/XMLSchema#> .
@prefix rico:          <https://www.ica.org/standards/RiC/ontology#> .
@prefix ric-rst:       <https://www.ica.org/standards/RiC/vocabularies/recordSetTypes#> .

<https://id.archief.amsterdam/8>
    rdf:type rico:RecordSet ;
    rdfs:label "Het Archief van het Weeshuis" ;
    rico:hasAccumulator [
        rdf:type rico:CorporateBody ;
        rdfs:label "Het Weeshuis" ;
        ] ;
    rico:beginningDate "1673-02-28"^^xsd:date ;
    rico:hasRecordSetType ric-rst:Fonds .
```

Opvallend: we hebben in de SHACL file gezegd, dat een archiefvormer een 'rico:Agent' moet zijn. Maar in deze data staat dat de archiefvormer een rico:CorporateBody is. Dit komt door de inference die we hebben aangezet op basis van de RiC-Ontology. GraphDB rekent eerst uit dat het Weeshuis een rico:Agent is omdat ```rico:CorporateBody owl:subClassOf rico:Group . rico:Group owl:subClassOf rico:Agent .```. 

Ga naar [Les 09: Specifieke properties voor het SAA](les09.md)
