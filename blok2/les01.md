# Les 1: De samenhang van properties en classes in een ontologie
Je mag in Linked Data alle properties gebruiken die je wilt. We hebben tot nu toe gebruik gemaakt van property-verzamelingen rdf, rdfs en rico. Een veel toegepaste andere verzameling van properties is schema.org.

Zo'n verzameling van properties heeft een bepaalde samenhang. In rico is het bijvoorbeeld logisch dat een knoop van het type rico:RecordSet de property rico:hasRecordSetType mag hebben. Dit soort samenhang wordt vastgelegd in een _ontologie_. Van elke property is bijvoorbeeld vastgelegd wat de _domain_ is, en de _range_. De domain van de property rico:hasRecordSetType is rico:RecordSet en de object van een triple met deze property is van het type rico:RecordSetType, met andere woorden: de range van rico:hasRecordSetType is rico:RecordSetType.

Lees de rico-ontologie in in GraphDB:
"Import" -> "RDF" -> "Get RDF data from a URL"

Gebruik deze URL en kies bij het inlezen voor 'named graph'.
https://www.ica.org/standards/RiC/RiC-O_v0-2.rdf 

Geef de graaf de naam "https://www.ica.org/standards/RiC/ontology".

Als je nu een graaf gaat visualiseren, zie je rdfs:labels die zijn gedefinieerd in de ontologie bij de relaties staan.

Ga naar [Les 02: Onze eerste ontologie](les02.md)