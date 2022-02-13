# Les 5: Domain (domein) en range (bereik)
We kunnen ook nog afleidregels toevoegen voor properties.

Voeg toe:
("Import" -> "RDF" -> "Import RDF Text Snippet")

```
@prefix ex: <http://example.com/example#> .

@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

# ontology
ex:playsIn a rdfs:Property ;
    rdfs:domain ex:Player ;
    rdfs:range ex:SportsTeam .

```

Dankzij de inferentie levert deze SPARQL-query meer op dan je zou verwachten op basis van de data alleen:
```
PREFIX ex: <http://example.com/example#> 

SELECT ?s WHERE {
    ?s a ex:Player .
}
```

Kijk ook: [Extra les ontologie: bekijk Records in Contexts](extra-les-ontologie.md)
Ga naar: [Les 06: Onze eerste Shapes](les06.md)

### Compleet voorbeeld

```
@prefix ex: <http://example.com/example#> .

@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

# ontology
ex:SportsTeam a rdfs:Class .

ex:FootballTeam a rdfs:Class ;
    rdfs:subClassOf ex:SportsTeam .

ex:HockeyTeam a rdfs:Class ;
    rdfs:subClassOf ex:SportsTeam .

ex:Player a rdfs:Class .

ex:playsIn a rdfs:Property ;
    rdfs:domain ex:Player ;
    rdfs:range ex:SportsTeam .

# data
ex:Tadic ex:playsIn ex:Ajax .
ex:Mitton ex:playsIn ex:AHBC .

ex:Ajax a ex:FootballTeam .
ex:AHBC a ex:HockeyTeam .
```
