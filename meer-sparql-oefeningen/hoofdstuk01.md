# Opdrachten bij DuCharme hoofdstuk 1.
TODO: alleen volledige triples in de resultaten. Geen punt-komma gebruiken.

## Opdracht 1: 
Bij de de Koninklijke Bibliotheek beheren ze de Nederlandse Bibliografische Catalogus. Deze dataset is met SPARQL te bevragen op dit endpoint: http://data.bibliotheken.nl/sparql. In de dataset zijn publicaties met behulp van properties uit Schema.org gemodelleerd. Zo kan bij een boek, indien beschikbaar, een ISBN nummer zijn opgeslagen met de property http://schema.org/isbn en de titel van het boek met de property http://schema.org/name .

1.1. Wat is de URI van het boek met het ISBN-nummer "9789023476825"?
1.2. Wat is de titel van dit boek?

Antwoord: [yasgui-link]
```
PREFIX schema: <http://schema.org/>

SELECT * WHERE {
  ?boek schema:isbn "9789023476825" ;
      schema:name ?titel .
}
```
1.3. Welke informatie is nog meer over dit boek vastgelegd?

```
PREFIX schema: <http://schema.org/>

SELECT * WHERE {
  ?boek schema:isbn "9789023476825" ;
      ?property ?object .
}
```

## Opdracht 2: FILTER/regex
Ook de Bibliotheque National de France heeft een SPARQL-endpoint voor het beschikbaar stellen van de catalogusinformatie (https://data.bnf.fr/sparql). Zou daar ook een exemplaar van Mulisch' Stenen Bruidsbed zijn te vinden? Ze gebruiken in Frankrijk Dublin Core Terms in plaats van Schema.org. De titel van het boek is daarom gekoppeld met de property <http://purl.org/dc/terms/title>. Voor de plaats van uitgave hebben ze een property uit een andere ontologie gekozen: <http://rdaregistry.info/Elements/m/P30088>.

2.1 Schrijf een query waarmee de boeken die zijn uitgegeven in Amsterdam in de catalogus worden gevonden. Geef in het resultaat de URI van het boek en de titel.

2.2 Bereid de query uit zodat alleen boeken worden weergegeven met het woord "bruidsbed" in de titel.


```
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX rdam: <http://rdaregistry.info/Elements/m/>

SELECT * WHERE {
  ?livre rdam:P30088 "Amsterdam" ;
     dct:title ?titre .
  FILTER (regex(?titre, "bruidsbed", "i"))
} 
```

## Opdracht 3: OPTIONAL
Bij de British Library bevat het SPARQL-endpoint de metadata over een boek met properties volgens Dublin Core Terms *en* Schema.org (https://bnb.data.bl.uk/sparql). Voor deze opdracht kiezen we Dublin Core Terms. Laten we de boeken zoeken die door Mulisch zijn geschreven (dct:creator) in deze catalogus. Bij de BL identificeren ze Mulisch met deze URI: <http://bnb.data.bl.uk/id/person/MulischHarry1927-2010>

3.1 
Geef een overzicht van de boeken in de collectie van de BL geschreven door Mulisch. Neem op: de URI van het boek en de titel (je weet intussen welke property dat zou moeten zijn volgens Dublin Core).

3.2
Bij sommige boeken hebben ze in de catalogus een alternatieve titel opgenomen, namelijk de titel in de oorspronkelijke taal. Dit gebeurt met de property dct:alternative. Maar deze alternatieve titel is niet altijd opgenomen. Maak een query waarbij ook de alternatieve titel is opgenomen, indien aanwezig.

```
PREFIX dct: <http://purl.org/dc/terms/>

SELECT * WHERE {
  ?book dct:creator <http://bnb.data.bl.uk/id/person/MulischHarry1927-2010> ;
        dct:title ?title .
  OPTIONAL {
    ?book dct:alternative ?altTitle .
  }
}
```

3.3. 
Altijd instructief: kijk even wat er allemaal vastligt over Mulisch in de catalogus. Met welke externe terminologiebronnen is Mulisch verbonden?

SELECT * WHERE {
  <http://bnb.data.bl.uk/id/person/MulischHarry1927-2010> ?property ?object .
}


