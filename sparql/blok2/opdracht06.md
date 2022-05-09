# Opdracht 6
Voor deze opdracht maken we gebruik van het endpoint van het Getty Institute (http://vocab.getty.edu/sparql.json), waarin onder meer de Art and Architecture Thesaurus (AAT) is opgenomen. De AAT maakt gebruik van Simple Knowledge Organisation Standard. In SKOS (PREFIX skos: <http://www.w3.org/2004/02/skos/core#>) geeft het Getty aan hoe concepten zich tot elkaar verhouden. Dit sluit aan bij de terminologie die we kennen van thesauri. Zo zijn er van een concept "broader terms" en "narrower terms".

## 6.1
Zoek de AAT-uri voor het concept dat in het Nederlands wordt aangeduid met "boeken"@nl als skos:prefLabel.

Bekijk het voorbeeld in het boek: ex008.rq.

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20skos%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0A%0ASELECT%20%3Fconcept%20WHERE%20%7B%0A%20%20%3Fconcept%20skos%3AprefLabel%20%22boeken%22%40nl%20.%0A%7D%20&endpoint=http%3A%2F%2Fvocab.getty.edu%2Fsparql.json&requestMethod=POST&tabTitle=Query%205&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson&outputFormat=table)

## 6.2
Het concept "boeken" heeft in thesaurus een bovenliggende term, een term die broader wordt genoemd. De broader term wordt aan het concept gekoppeld met de property skos:broader. Maak een query die de skos:broader term van "boeken" opzoekt. Geef de URI en het label.

Bekijk het voorbeeld in het boek: ex070.rq.

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20skos%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0A%0ASELECT%20%3Fbt%20%3Flabel%20WHERE%20%7B%0A%20%20%3Fconcept%20skos%3AprefLabel%20%22boeken%22%40nl%20%3B%0A%20%20%20%20%20%20%20%20%20%20%20skos%3Abroader%20%3Fbt%20.%0A%20%20%3Fbt%20skos%3AprefLabel%20%3Flabel%20.%0A%7D%20&endpoint=http%3A%2F%2Fvocab.getty.edu%2Fsparql.json&requestMethod=POST&tabTitle=Query%205&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 6.3
Vraag de broader term op zonder de tussenliggende URI te hoeven opvragen.

Bekijk het voorbeeld in het boek: ex082.rq.

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20skos%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0A%0ASELECT%20%3Flabel%20WHERE%20%7B%0A%20%20%3Fconcept%20skos%3AprefLabel%20%22boeken%22%40nl%20%3B%0A%20%20%20%20%20%20%20%20%20%20%20skos%3Abroader%2Fskos%3AprefLabel%20%3Flabel%20.%0A%7D%20&endpoint=http%3A%2F%2Fvocab.getty.edu%2Fsparql.json&requestMethod=POST&tabTitle=Query%205&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 6.4
Realiseer je dat een thesaurus een boom is met termen. Een term heeft 'onderliggende' termen gekoppeld met de property skos:narrower, maar die termen hebben ook weer onderliggende termen die met dezelfde property (namelijk skos:narrower) zijn gekoppeld. Maak een query waarmee de labels van alle (!) narrower terms, dus ook van de terms die narrower zijn dan de narrower term etc.

Bekijk het voorbeeld in het boek: ex078.rq

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20skos%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0A%0ASELECT%20%3Flabel%20WHERE%20%7B%0A%20%20%3Fconcept%20skos%3AprefLabel%20%22boeken%22%40nl%20%3B%0A%20%20%20%20%20%20%20%20%20%20%20skos%3Anarrower%2B%2Fskos%3AprefLabel%20%3Flabel%20.%0A%7D%20&endpoint=http%3A%2F%2Fvocab.getty.edu%2Fsparql.json&requestMethod=POST&tabTitle=Query%205&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 6.5
FILTER bij de laatste query op skos:prefLabels in het Nederlands.

Bekijk het voorbeeld in het boek: ex049.rq

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20skos%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0A%0ASELECT%20%3Flabel%20WHERE%20%7B%0A%20%20%3Fconcept%20skos%3AprefLabel%20%22boeken%22%40nl%20%3B%0A%20%20%20%20%20%20%20%20%20%20%20skos%3Anarrower%2B%2Fskos%3AprefLabel%20%3Flabel%20.%0A%20%20FILTER%20(lang(%3Flabel)%20%3D%20%22nl%22)%0A%7D%20&endpoint=http%3A%2F%2Fvocab.getty.edu%2Fsparql.json&requestMethod=POST&tabTitle=Query%205&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

Einde blok 2
