# Les 10: Een query met een patroon dat OPTIONAL is
Stel je wilt wel alle archieven en alleen de begindatum van vorming als deze ook in de graaf is opgenomen. Als hij niet in de graaf is opgenomen, mag de waarde in kolom wegblijven.

Daarvoor gebruik je het woord OPTIONAL.

```
SELECT * WHERE {
     ?rs    rico:hasRecordSetType ?rst .
     OPTIONAL {
        ?rs	rico:isAssociatedWithDate/rico:hasBeginningDate/rico:normalizedDateValue ?begindate .
     }
}

```

Knip en plak deze query in GraphDB -> SPARQL. Deze query geeft drie kolommen, waarvan de ?begindate op twee plaatsen leeg is.

Einde blok 1
