# Opdracht 10
In deze opdracht gaan we een aantal standaard queries bedenken die je kunt toepassen om te kijken wat er in een endpoint is opgeslagen. We maken daarbij gebruik van een Japans endpoint: 
https://mediag.bunka.go.jp/sparql. Let op: het endpoint is langzaam, dus het duurt even voor je antwoord krijgt.

## 10.1 

Nette Linked Data geeft van alle "dingen" aan van welke class het is. Dat is aan het "ding" gekoppeld met de property "rdf:type". Maak een query die een overzicht geeft van alle afzonderlijke (lees: "distincte" (dikke tip)) class's die in het Japanse endpoint zijn opgenomen.

Antwoord: [yasgui-link](https://yasgui.triply.cc/?query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT%20*%20WHERE%20%7B%0A%20%20%3Fsub%20%3Fpred%20%3Fobj%20.%0A%7D%20%0ALIMIT%2010&endpoint=http%3A%2F%2Fldf.fi%2Fmufi%2Fsparql#query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0ASELECT%20DISTINCT%20%3Fclass%20WHERE%20%7B%0A%20%20%3Fsub%20rdf%3Atype%20%3Fclass%20.%0A%7D%20&endpoint=https%3A%2F%2Fmediag.bunka.go.jp%2Fsparql&requestMethod=POST&tabTitle=Query&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 10.2 
Nu is het handig om te weten hoeveel elke class voorkomt. Dan moeten we de voorkomens van elke class gaan tellen. Maak een query die telt hoeveel er van elke class in het Japanse endpoint zijn opgenomen.

Bekijk het voorbeeld in het boek: ex162.rq.

Antwoord: [yasgui-link](https://yasgui.triply.cc/?query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT%20*%20WHERE%20%7B%0A%20%20%3Fsub%20%3Fpred%20%3Fobj%20.%0A%7D%20%0ALIMIT%2010&endpoint=http%3A%2F%2Fldf.fi%2Fmufi%2Fsparql#query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0ASELECT%20%3Fclass%20(COUNT(%3Fclass)%20AS%20%3FclassCount)%20WHERE%20%7B%0A%20%20%3Fsub%20rdf%3Atype%20%3Fclass%20.%0A%7D%20%0AGROUP%20BY%20%3Fclass&endpoint=https%3A%2F%2Fmediag.bunka.go.jp%2Fsparql&requestMethod=POST&tabTitle=Query%201&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 10.3
Behalve de class's kun je ook de verschillende soorten properties tellen die in het endpoint zijn opgenomen. Deze query lijkt heel erg op de vorige.

Antwoord: [yasgui-link](https://yasgui.triply.cc/?query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT%20*%20WHERE%20%7B%0A%20%20%3Fsub%20%3Fpred%20%3Fobj%20.%0A%7D%20%0ALIMIT%2010&endpoint=http%3A%2F%2Fldf.fi%2Fmufi%2Fsparql#query=SELECT%20%3Fpred%20(COUNT(%3Fpred)%20AS%20%3FpredCount)%20WHERE%20%7B%0A%20%20%3Fsub%20%3Fpred%20%3Fobj%20.%0A%7D%20%0AGROUP%20BY%20%3Fpred&endpoint=https%3A%2F%2Fmediag.bunka.go.jp%2Fsparql&requestMethod=POST&tabTitle=Query%201&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 10.4
Echt overzicht heb je nog niet echt. Je zou het resultaat kunnen ordenen zodat de meest gebruikte property bovenaan staat.

Bekijk het voorbeeld in het boek: ex148.rq

Antwoord: [yasgui-link](https://yasgui.triply.cc/?query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT%20*%20WHERE%20%7B%0A%20%20%3Fsub%20%3Fpred%20%3Fobj%20.%0A%7D%20%0ALIMIT%2010&endpoint=http%3A%2F%2Fldf.fi%2Fmufi%2Fsparql#query=SELECT%20%3Fpred%20(COUNT(%3Fpred)%20AS%20%3FpredCount)%20WHERE%20%7B%0A%20%20%3Fsub%20%3Fpred%20%3Fobj%20.%0A%7D%20%0AGROUP%20BY%20%3Fpred%0AORDER%20BY%20DESC(%3FpredCount)&endpoint=https%3A%2F%2Fmediag.bunka.go.jp%2Fsparql&requestMethod=POST&tabTitle=Query%201&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

Ga naar [Opdracht 11](opdracht11.md).