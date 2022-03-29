# Les 7: Data valideren
Als het goed is, gaat het nu mis als je onderstaande data wilt invoeren:
("Import" -> "RDF" -> "Import RDF Text Snippet")

```
@prefix rdf:           <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:          <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rico:          <https://www.ica.org/standards/RiC/ontology#> .

<https://id.archief.amsterdam/8>
	rdf:type rico:RecordSet ;
    rdfs:label "Het Archief van het Weeshuis" .
```

Opdracht: probeer het in te voeren in je repo en kijk wat er gebeurt.
Opdracht: voeg een triple toe waardoor aan de NodeShape hierboven is voldaan.

Antwoord:
```
@prefix rdf:           <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:          <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rico:          <https://www.ica.org/standards/RiC/ontology#> .

<https://id.archief.amsterdam/8>
    rdf:type rico:RecordSet ;
    rdfs:label "Het Archief van het Weeshuis" ;
    rico:hasAccumulator "Het Weeshuis" .
```

Ga naar [Les 08: Controleren op datatype en rdf:Class](les08.md)

