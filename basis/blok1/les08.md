# Les 8: Een query met een pad

Het patroon dat we zoeken wordt steeds verder uitgebreid. Nu krijgen we er een ?begindate bij. Let op: als er geen begindate in de graaf is, bestaat het patroon niet en komt er dus ook niet een archief of archiefonderdeel uit de query.

```
SELECT * WHERE {
     ?rs 	rico:hasRecordSetType ?rst ;
     		rico:isAssociatedWithDate/rico:hasBeginningDate/rico:normalizedDateValue ?begindate .
}

```

Knip en plak deze query in GraphDB -> SPARQL. Als het goed is krijg je nu nog maar een archief. Bij dat andere archief is immers geen datum in de graaf opgenomen, dus dat voldoet niet aan het patroon waarom je in deze SPARQL query vraagt.

Ga naar [Les 09: Een query met een patroon dat OPTIONAL is](les09.md)
