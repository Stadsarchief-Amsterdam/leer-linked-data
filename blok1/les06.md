# Les 6: Mijn eerste SPARQL-query
SPARQL is een query-taal die op zoek gaat naar patronen in de graaf. Een SPARQL-query geeft dus altijd antwoord op de vraag: geeft mij alle waardes die voldoen aan het opgegeven patroon. In SPARQL zul je allerlei dingen herkennen uit turtle en -als je dat kent- SQL.

```
SELECT ?archief WHERE {
     ?archief   rdf:type rico:RecordSet ;
                rico:hasRecordSetType ric-rst:Fonds .
}

```

Deze query zoekt naar dingen '?archief' die voldoen aan het patroon dat er een relaties is met rdf:type naar rico:RecordSet *en* met rico:hasRecordSetType naar ric-rst:Fonds. De uitkomst geeft een lijst terug van URI's waarvan in de graaf is aangegeven dat het een rico:RecordSet is en dat het met de property rico:hasRecordSetType aan ric-rst:Fonds is gekoppeld.

Knip en plak deze query in GraphDB -> SPARQL .

Ga naar [Les 07: Een query met twee variabelen](les07.md)
