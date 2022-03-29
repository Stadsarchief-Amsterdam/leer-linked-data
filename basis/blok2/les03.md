# Les 3: De eerste _inference_

Voeg toe:
("Import" -> "RDF" -> "Import RDF Text Snippet")

```
@prefix ex: <http://example.com/example#> .

@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

# ontology
ex:FootballTeam a rdfs:Class ;
    rdfs:subClassOf ex:SportsTeam .

# data
ex:Ajax a ex:FootballTeam .
```

Dit maakt de volgende queries mogelijk:

SPARQL:
```
PREFIX ex: <http://example.com/example#> 

SELECT * WHERE {
    ?s ex:playsIn ?o .
    ?o a ex:FootballTeam .
}
```
en
```
PREFIX ex: <http://example.com/example#> 

SELECT * WHERE {
    ?s ex:playsIn ?o .
    ?o a ex:SportsTeam .
}
```

Opdracht: waar staat dat Ajax een Sportsteam is? Is deze kennis afgeleid (impliciet) of direct vastgelegd (expliciet)?

Ga naar: [Les 04: Nog meer _inference_](les04.md)