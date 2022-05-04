# Opdracht 7
In Frankrijk is een samenwerkingsproject geweest met de naam ALEGORIA, waarin (metadata over) foto's vanuit de lucht zijn opgenomen, afkomstig uit verschillende collecties. En de metadata is gemodelleerd in ... RiC-O !! De metadata is beschikbaar via dit SPARQL-endpoint: http://data.alegoria-project.fr/sparql/. De foto's zelf zijn helaas achter een wachtwoord verstopt.

Voor nu niet nodig, maar als je je een keer in deze toepassing van RiC-O wilt verdiepen, is hier meer informatie:
* Over het project: https://www.alegoria-project.fr/. (Engels)
* Over hoe de metadata in RiC-O beschikbaar is: https://www.alegoria-project.fr/sites/default/files/3.pres_PubMetadataLOD-FClavaud-PCharbonnier-NAbadie.pdf (Frans)

## 7.1
We gaan de data als echte archivarissen van boven naar beneden benaderen. Het 'ding' in de top van de hierarchie van een archiefbeschrijving is van het rdf:type rico:RecordSet. Welke rico:RecordSet's met de property rico:hasRecordSetType <https://www.ica.org/standards/RiC/vocabularies/recordSetTypes#Fonds> zijn er in het endpoint opgenomen? 

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rico%3A%20%3Chttps%3A%2F%2Fwww.ica.org%2Fstandards%2FRiC%2Fontology%23%3E%0A%0ASELECT%20%3Frs%20WHERE%20%7B%0A%3Frs%20rdf%3Atype%20rico%3ARecordSet%20%3B%0A%20%20rico%3AhasRecordSetType%20%3Chttps%3A%2F%2Fwww.ica.org%2Fstandards%2FRiC%2Fvocabularies%2FrecordSetTypes%23Fonds%3E%20.%0A%7D%0A&endpoint=http%3A%2F%2Fdata.alegoria-project.fr%2Fsparql%2F&requestMethod=POST&tabTitle=Query&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 7.2
Een rico:RecordSet kan rico:RecordSet's bevatten en deze bevatten misschien ook wel weer rico:RecordSet's. Geef een overzicht van alle rico:RecordSet's in het endpoint met hun rico:RecordSetType (gekoppeld met rico:hasRecordSetType).

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rico%3A%20%3Chttps%3A%2F%2Fwww.ica.org%2Fstandards%2FRiC%2Fontology%23%3E%0A%0ASELECT%20%3Frs%20%3Frst%20WHERE%20%7B%0A%3Frs%20rdf%3Atype%20rico%3ARecordSet%20%3B%0A%20%20rico%3AhasRecordSetType%20%3Frst%20.%0A%7D%0A&endpoint=http%3A%2F%2Fdata.alegoria-project.fr%2Fsparql%2F&requestMethod=POST&tabTitle=Query&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 7.3
Geef een overzicht van de verschillende rico:RecordSetTypes die zijn gedefinieerd. Gebruik DISTINCT.

Bekijk het voorbeeld in het boek: ex094.rq.

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rico%3A%20%3Chttps%3A%2F%2Fwww.ica.org%2Fstandards%2FRiC%2Fontology%23%3E%0A%0ASELECT%20DISTINCT%20%3Frst%20WHERE%20%7B%0A%3Frs%20rdf%3Atype%20rico%3ARecordSet%20%3B%0A%20%20rico%3AhasRecordSetType%20%3Frst%20.%0A%7D%0A&endpoint=http%3A%2F%2Fdata.alegoria-project.fr%2Fsparql%2F&requestMethod=POST&tabTitle=Query&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

Ga naar [Opdracht 08](opdracht08.md).