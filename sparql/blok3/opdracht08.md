# Opdracht 8
We gaan nog meer oefenen met RiC-O op het ALEGORIA-endpoint.

## 8.1
Vraag alle 'dingen' in het endpoint op van het rdf:type rico:Record.

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rico%3A%20%3Chttps%3A%2F%2Fwww.ica.org%2Fstandards%2FRiC%2Fontology%23%3E%0A%0ASELECT%20*%20WHERE%20%7B%0A%20%20%3Fr%20rdf%3Atype%20rico%3ARecord%20.%0A%7D%0A&endpoint=http%3A%2F%2Fdata.alegoria-project.fr%2Fsparql%2F&requestMethod=POST&tabTitle=Query&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 8.2
Vraag bij rico:Record's ook de rico:creationDate op.

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rico%3A%20%3Chttps%3A%2F%2Fwww.ica.org%2Fstandards%2FRiC%2Fontology%23%3E%0A%0ASELECT%20*%20WHERE%20%7B%0A%20%20%3Fr%20rdf%3Atype%20rico%3ARecord%20%3B%0A%20%20%20%20%20rico%3AcreationDate%20%3Fdate%20.%0A%7D%0A&endpoint=http%3A%2F%2Fdata.alegoria-project.fr%2Fsparql%2F&requestMethod=POST&tabTitle=Query&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 8.3
Nu gaan we vroege luchtfoto's opvragen, dat wil zeggen, die zijn gemaakt voor 1920.

Dit kun je doen door een FILTER te gebruiken. Dat hebben we eerder gedaan met een REGEX en met de taal. Wat je doet is filteren op rico:Record's die een rico:creationDate hebben die kleiner is dan "1920".

Bekijk het voorbeeld in het boek: ex105.rq.

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rico%3A%20%3Chttps%3A%2F%2Fwww.ica.org%2Fstandards%2FRiC%2Fontology%23%3E%0A%0ASELECT%20*%20WHERE%20%7B%0A%20%20%3Fr%20rdf%3Atype%20rico%3ARecord%20%3B%0A%20%20%20%20%20rico%3AcreationDate%20%3Fdate%20.%0A%20%20FILTER%20(%3Fdate%20%3C%20%221920%22)%0A%7D&endpoint=http%3A%2F%2Fdata.alegoria-project.fr%2Fsparql%2F&requestMethod=POST&tabTitle=Query%201&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

Ga naar [Opdracht 09](opdracht09.md).