# Les 9: Een query met een FILTER

In de volgende query kun je filteren op een datum. Wat zou deze query moeten opleveren?

```
SELECT * WHERE {
     ?rs 	rico:hasRecordSetType ?rst ;
     		rico:isAssociatedWithDate/rico:hasBeginningDate/rico:normalizedDateValue ?begindate .
     FILTER (?begindate < '1600'^^xsd:gYear)
}

```

Knip en plak deze query in GraphDB -> SPARQL. Als het goed is geeft de query nu geen enkel resultaat.

Einde blok 1

