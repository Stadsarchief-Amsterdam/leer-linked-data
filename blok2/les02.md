# Les 2: Onze eerste ontologie
Zo'n ontologie helpt om allerlei queries te kunnen stellen die eerst niet mogelijk waren. De triple store (in ons geval GraphDB) maakt daarbij gebruik van _reasoning_. Bij dit _redeneren_ leidt de triple store extra relaties af die je niet expliciet hebt opgegeven in je data. Dit afleiden heet _inference_. Daarbij maakt het systeem gebruik van de onderlinge relaties tussen concepten en properties die in de ontologie zijn vastgelegd. Dit klinkt heel abstact, daarom gaan we daarmee oefenen.

```
@prefix ex: <http://example.com/example#> .

@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

# ontology
ex:SportsTeam a rdfs:Class .
ex:Player a rdfs:Class .
ex:playsIn a rdfs:Property .

# data
ex:Tadic ex:playsIn ex:Ajax .
ex:Mitton ex:playsIn ex:AHBC .
```

Lees de data in, in GraphDB.
("Import" -> "RDF" -> "Import RDF Text Snippet")

Opdracht: leg uit wat we hier hebben vastgelegd. Kun je nog meer semantiek bedenken die we niet gecodeerd hebben? Wat is ex:AHBC voor club?

Ga naar: [Les 03: De eerste _inference_](les03.md)
