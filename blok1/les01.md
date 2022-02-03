# Les 1: triples in een graaf

Verbindingen in een netwerk van data (het wiskundige woord voor netwerk is 'graaf') leg je vast door aan te geven welke knoop met welke knoop is verbonden met welk relatie. In Linked Data worden deze combinaties van ```<knoop1> <relatie> <knoop2> ```  _triples_ genoemd. In Linked Data zijn alle knopen en relaties webadressen of beter Uniform Resource Identifiers (URI's). Je kunt je Linked Data dus opsommen door deze triples in URI's uit te drukken:


```
<https://id.archief.amsterdam/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://www.ica.org/standards/RiC/ontology#RecordSet> .
<https://id.archief.amsterdam/1> <https://www.ica.org/standards/RiC/ontology#hasRecordSetType> <https://www.ica.org/standards/RiC/vocabularies/recordSetTypes#Fonds> .
```

Het heeft dus altijd de structuur: ```<knoop1> <relatie> <knoop2> .``` Deze drie dingen van de triple heten respectievelijk: _subject_, _predicate_ (of _property_) en _object_.

Laad dit voorbeeld in GraphDB. Kies "Import" -> "RDF" -> "Import RDF Text Snippet" . Knip en plak bovenstaande voorbeeld daar in.
