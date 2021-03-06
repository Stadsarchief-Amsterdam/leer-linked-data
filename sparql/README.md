# Oefeningen in SPARQL
Dit overzicht bevat oefeningen in het maken van SPARQL-queries voor verschillende endpoints in het erfgoeddomein. Je leert daardoor hoe SPARQL werkt, maar ook op welke manier Linked Open Data voor erfgoed in de praktijk wordt gemodeleerd.

## DuCharme's Learning SPARQL
Volgt de opbouw van dit boek:
[Bob DuCharme, Learning SPARQL, O'Reilly 2013](https://www.oreilly.com/library/view/learning-sparql-2nd/9781449371449/)

## Gebruik GraphDB
Als je de voorbeelden van DuCharme wilt gebruiken om te oefenen, kun je ook GraphDB gebruiken in plaats van de ```arq``` omgeving die DuCharme in het boek gebruikt. De voorbeelden van DuCharme kun je daarvoor als [zip-file](http://learningsparql.com/2ndeditionexamples/LearningSPARQLExamples.zip) downloaden. De ttl-bestandjes kun je als RDF snippets inlezen in GraphDB (zoals geleerd tijdens de basiscursus) en daar dan de SPARQL queries (in rq-bestandjes) in GraphDB uitvoeren.

## Gebruik YASGUI
Je kunt op yasgui.org een SPARQL-query maken, aangeven naar welk endpoint je het wilt sturen en deze vervolgens uitvoeren.

Bijvoorbeeld:
https://api.triplydb.com/s/yLqXmahhD

## Inhoud Blok 1
Bestudeer: hoofdstuk 1
Opdrachten bij DuCharme hoofdstuk 1.
Bij deze opdrachten maken we gebruik van SPARQL endpoints van
- [Koninklijke Bibliotheek](http://data.bibliotheken.nl/sparql) (Den Haag)
- [Bibliotheque National de France](https://data.bnf.fr/sparql) (Parijs)

Onderwerpen: basisprincipe, FILTER/REGEX, Schema.org, Dublin Core.

## Inhoud Blok 2
Bestudeer: pp. 47-69
Opdrachten bij DuCharme hoofdstuk 3, pp. 47-69
Bij deze opdrachten maken we gebruik van SPARQL endpoints van
- [Koninklijke Bibliotheek](http://data.bibliotheken.nl/sparql) (Den Haag)
- [DBPedia](https://dbpedia.org/sparql) 
- [Kungliga Biblioteket](https://libris.kb.se/sparql) (Stockholm)
- [Getty Institute](http://vocab.getty.edu/sparql) (Los Angeles, CA (USA))

Onderwerpen: turtle-syntax/labels, OPTIONAL, pad door gebruik van variabelen/gebruik van + in pad, SKOS

## Inhoud blok 3
Bestudeer: pp 69-89
Opdrachten bij DuCharme hoofdstuk 3, pp. 69-89
- [ALEGORIA project](http://data.alegoria-project.fr/sparql/) (Frankrijk)

Onderwerpen: DISTINCT, FILTER, RiC-O

## Inhoud blok 4
Bestudeer: pp 89-108
Opdrachten bij DuCharme hoofdstuk 3, pp. 89-108

- [Japans endpoint](https://mediag.bunka.go.jp/sparql) (Japan)

Onderwerpen: COUNT, AS, ORDER BY

