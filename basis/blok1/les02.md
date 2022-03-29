# Les 2: turtle en andere serializaties
De manier om triples uit te drukken zoals we in les 1 zagen wordt _n-triples_ genoemd. Overzichtelijker wordt het als je triples uitdrukt in _turtle_.

In de onderstaande voorbeelden zijn dezelfde triples uitgedrukt als in het voorbeeld in n-triples van les 1.
```
<https://id.archief.amsterdam/1> 
	<http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://www.ica.org/standards/RiC/ontology#RecordSet> ;
	<https://www.ica.org/standards/RiC/ontology#hasRecordSetType> <https://www.ica.org/standards/RiC/vocabularies/recordSetTypes#Fonds> .
```

Echt leesbaar voor mensen wordt het als je webadressen afkort met een _namespace_.

```
@prefix rdf:           <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rico:          <https://www.ica.org/standards/RiC/ontology#> .
@prefix ric-rst:       <https://www.ica.org/standards/RiC/vocabularies/recordSetTypes#> .

<https://id.archief.amsterdam/1> 
	rdf:type rico:RecordSet ;
	rico:hasRecordSetType ric-rst:Fonds .
```

N-triples en Turtle drukken allebei dus op een andere manier dezelfde triples uit. Het zijn, in jargon, verschillende _serializaties_ van dezelfde RDF.

Ga naar [Les 03: Een RiC-O voorbeeld in turtle](les03.md)
