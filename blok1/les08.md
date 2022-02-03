# Les 8: Een query met een pad

Het patroon dat we zoeken wordt steeds verder uitgebreid. Nu krijgen we er een ?begindate bij. Let op: als er geen begindate in de graaf is, bestaat het patroon niet en komt er dus ook niet een archief of archiefonderdeel uit de query.

```
SELECT * WHERE {
     ?rs 	rico:hasRecordSetType ?rst ;
     		rico:isAssociatedWithDate/rico:hasBeginningDate/rico:normalizedDateValue ?begindate .
}

```

Knip en plak deze query in GraphDB -> SPARQL .

Ga naar [Les 09: Een query met een FILTER](les09.md)
