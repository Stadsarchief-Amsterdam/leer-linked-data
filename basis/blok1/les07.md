# Les 7: Een query met twee variabelen

Je kunt in een query ook een patroon opvragen met twee onbekenden. Deze query geeft alle soorten RecordSet's met hun type.

```
SELECT * WHERE {
     ?rs 	rico:hasRecordSetType ?rst ;
}

```

Knip en plak deze query in GraphDB -> SPARQL. In het antwoord zie je nu twee kolommen: voor elke onbekende variabele (?rs en ?rst) een. 

Ga naar [Les 08: Een query met een pad](les08.md)
