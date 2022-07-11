# Opdracht 7
_In deze opdracht leer je zoeken naar data van een bepaalde Class uit een ontologie en over het gebruik van DISTINCT._

In Frankrijk is een samenwerkingsproject geweest met de naam ALEGORIA, waarin (metadata over) foto's vanuit de lucht zijn opgenomen, afkomstig uit verschillende collecties. En de metadata is gemodelleerd in ... RiC-O !! De metadata is beschikbaar via dit SPARQL-endpoint: http://data.alegoria-project.fr/sparql/. De foto's zelf zijn helaas achter een wachtwoord verstopt. De prefix voor rico is: ```<https://www.ica.org/standards/RiC/ontology#>```.

## 7.1
Bekijk het voorbeeld in het boek: ex415.rq. De letter ```a``` in deze query is een afkorting voor de porperty ```rdf:type```.

We gaan de data als echte archivarissen van boven naar beneden benaderen. Het 'ding' in de top van de hierarchie van een archiefbeschrijving is van het rdf:type rico:RecordSet. Welke rico:RecordSet's met de property rico:hasRecordSetType <https://www.ica.org/standards/RiC/vocabularies/recordSetTypes#Fonds> zijn er in het endpoint opgenomen? 

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rico%3A%20%3Chttps%3A%2F%2Fwww.ica.org%2Fstandards%2FRiC%2Fontology%23%3E%0A%0ASELECT%20%3Frs%20WHERE%20%7B%0A%3Frs%20rdf%3Atype%20rico%3ARecordSet%20%3B%0A%20%20rico%3AhasRecordSetType%20%3Chttps%3A%2F%2Fwww.ica.org%2Fstandards%2FRiC%2Fvocabularies%2FrecordSetTypes%23Fonds%3E%20.%0A%7D%0A&endpoint=http%3A%2F%2Fdata.alegoria-project.fr%2Fsparql%2F&requestMethod=POST&tabTitle=Query&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 7.2
Behalve het ric-rst:Fonds zijn er nog meer soorten rico:RecordSet's. Een rico:RecordSet kan immers zelf ook rico:RecordSet's bevatten en deze bevatten zelf misschien ook wel weer rico:RecordSet's. Geef een overzicht van alle rico:RecordSet's in het endpoint met het gekoppelde rico:RecordSetType (gekoppeld met rico:hasRecordSetType).

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rico%3A%20%3Chttps%3A%2F%2Fwww.ica.org%2Fstandards%2FRiC%2Fontology%23%3E%0A%0ASELECT%20%3Frs%20%3Frst%20WHERE%20%7B%0A%3Frs%20rdf%3Atype%20rico%3ARecordSet%20%3B%0A%20%20rico%3AhasRecordSetType%20%3Frst%20.%0A%7D%0A&endpoint=http%3A%2F%2Fdata.alegoria-project.fr%2Fsparql%2F&requestMethod=POST&tabTitle=Query&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 7.3
Bekijk het voorbeeld in het boek: ex094.rq.

Geef een overzicht van de verschillende rico:RecordSetTypes die zijn gebruikt in het endpoint. Gebruik DISTINCT.

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rico%3A%20%3Chttps%3A%2F%2Fwww.ica.org%2Fstandards%2FRiC%2Fontology%23%3E%0A%0ASELECT%20DISTINCT%20%3Frst%20WHERE%20%7B%0A%3Frs%20rdf%3Atype%20rico%3ARecordSet%20%3B%0A%20%20rico%3AhasRecordSetType%20%3Frst%20.%0A%7D%0A&endpoint=http%3A%2F%2Fdata.alegoria-project.fr%2Fsparql%2F&requestMethod=POST&tabTitle=Query&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

Ga naar [Opdracht 08](opdracht08.md).
