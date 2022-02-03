# Les 10: Een query met een patroon dat OPTIONAL is
Voeg toe aan de graaf ("Import" -> "RDF" -> "Import RDF Text Snippet"):

```
<https://id.archief.amsterdam/8> 
	rdf:type rico:RecordSet ;
    rico:isAssociatedWithDate [
        a rico:DateRange ;
        rico:expressedDate "1572 - 1798" ;
        rico:hasBeginningDate [
            a rico:SingleDate ;
            rico:normalizedDateValue "1572"^^xsd:gYear
        ] ;
        rico:hasEndDate [
            a rico:SingleDate ;
            rico:normalizedDateValue "1798"^^xsd:gYear
        ]
    ] .

```

en voer dezelfde query opnieuw uit:

```
SELECT * WHERE {
     ?rs 	rico:hasRecordSetType ?rst ;
     		rico:isAssociatedWithDate/rico:hasBeginningDate/rico:normalizedDateValue ?begindate .
     FILTER (?begindate < '1600'^^xsd:gYear)
}

```

Waarom komt de nieuwe archiefbeschrijving nu niet als resultaat uit de query? Hint: heeft deze beschrijving een rico:hasRecordSetType property?

Deze query doet het beter:

```
SELECT * WHERE {
     ?rs	rico:isAssociatedWithDate/rico:hasBeginningDate/rico:normalizedDateValue ?begindate .
     OPTIONAL { ?rs 	rico:hasRecordSetType ?rst ; }
     FILTER (?begindate < '1600'^^xsd:gYear)
}

```


