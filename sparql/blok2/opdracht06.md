# Opdracht 6
Voor deze opdracht maken we gebruik van het endpoint van het Getty Institute, waarin ook de Art and Architecture Thesaurus is opgenomen.

## 6.1
Zoek de AAT -uri voor het concept dat in het Nederlands wordt aangeduid met "boeken"@nl.

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0A%0ASELECT%20%3Fconcept%20WHERE%20%7B%0A%20%20%3Fconcept%20rdfs%3Alabel%20%22boeken%22%40nl%20.%0A%7D%20&endpoint=http%3A%2F%2Fvocab.getty.edu%2Fsparql&requestMethod=POST&tabTitle=Query%205&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 6.2
Wat is de broader-term?

Bekijk het voorbeeld in het boek: ex070.rq.

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20aat%3A%20%3Chttp%3A%2F%2Fvocab.getty.edu%2Faat%2F%3E%0APREFIX%20skos%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0A%0ASELECT%20%3Fbt%20%3Flabel%20WHERE%20%7B%0A%20%20%3Fconcept%20rdfs%3Alabel%20%22boeken%22%40nl%20%3B%0A%20%20%20%20%20%20%20%20%20%20%20skos%3Abroader%20%3Fbt%20.%0A%20%20%3Fbt%20rdfs%3Alabel%20%3Flabel%20.%0A%7D%20&endpoint=http%3A%2F%2Fvocab.getty.edu%2Fsparql&requestMethod=POST&tabTitle=Query%205&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 6.3
Vraag de broader op zonder de tussenliggende URI te hoeven opvragen.

Bekijk het voorbeeld in het boek: ex078.rq.

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20aat%3A%20%3Chttp%3A%2F%2Fvocab.getty.edu%2Faat%2F%3E%0APREFIX%20skos%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0A%0ASELECT%20%3Flabel%20WHERE%20%7B%0A%20%20%3Fconcept%20rdfs%3Alabel%20%22boeken%22%40nl%20%3B%0A%20%20%20%20%20%20%20%20%20%20%20skos%3Abroader%2Frdfs%3Alabel%20%3Flabel%20.%0A%7D%20&endpoint=http%3A%2F%2Fvocab.getty.edu%2Fsparql&requestMethod=POST&tabTitle=Query%205&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 6.4
Geef de labels van alle! narrower terms.

## 6.5
FILTER op Nederlands.

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20aat%3A%20%3Chttp%3A%2F%2Fvocab.getty.edu%2Faat%2F%3E%0APREFIX%20skos%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0A%0ASELECT%20%3Flabel%20WHERE%20%7B%0A%20%20%3Fconcept%20rdfs%3Alabel%20%22boeken%22%40nl%20%3B%0A%20%20%20%20%20%20%20%20%20%20%20skos%3Anarrower%2B%2Frdfs%3Alabel%20%3Flabel%20.%0A%20%20FILTER%20(lang(%3Flabel)%20%3D%20%22nl%22)%0A%7D%20&endpoint=http%3A%2F%2Fvocab.getty.edu%2Fsparql&requestMethod=POST&tabTitle=Query%205&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)