# Opdracht 11
We oefenen nog meer op het Japanse endpoint.

## 11.1 
Het endpoint koppelt op twee manieren de vervaardiger aan een object, met schema:creator en met dct:creator. (Let op: "dct" is Dublin Core Terms en dat is anders dan "dc", Dublin Core. Type de prefix in en je krijgt de juiste prefix definitie in je query).

De koppeling met "dct:creator" is netjes via een URI. Zoek met dct:creator van alle dingen in het endpoint de rdfs:label van de vervaardiger op.

Antwoord: [yasgui-link](https://yasgui.triply.cc/?query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT%20*%20WHERE%20%7B%0A%20%20%3Fsub%20%3Fpred%20%3Fobj%20.%0A%7D%20%0ALIMIT%2010&endpoint=http%3A%2F%2Fldf.fi%2Fmufi%2Fsparql#query=PREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20dct%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0ASELECT%20*%20WHERE%20%7B%0A%20%20%3Fding%20dct%3Acreator%20%3Fcreator%20.%0A%20%20%3Fcreator%20rdfs%3Alabel%20%3FcreatorLabel%20.%0A%7D%20%0A&endpoint=https%3A%2F%2Fmediag.bunka.go.jp%2Fsparql&requestMethod=POST&tabTitle=Query%201&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 11.2 
Welke verschillende vervaardigers zijn er allemaal in het endpoint opgenomen?

Antwoord: [yasgui-link](https://yasgui.triply.cc/?query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT%20*%20WHERE%20%7B%0A%20%20%3Fsub%20%3Fpred%20%3Fobj%20.%0A%7D%20%0ALIMIT%2010&endpoint=http%3A%2F%2Fldf.fi%2Fmufi%2Fsparql#query=PREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20dct%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0ASELECT%20DISTINCT%20%3Fcreator%20%3FcreatorLabel%20WHERE%20%7B%0A%20%20%3Fding%20dct%3Acreator%20%3Fcreator%20.%0A%20%20%3Fcreator%20rdfs%3Alabel%20%3FcreatorLabel%20.%0A%7D%20%0A&endpoint=https%3A%2F%2Fmediag.bunka.go.jp%2Fsparql&requestMethod=POST&tabTitle=Query%201&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 11.3 
Hoe vaak komt elke vervaardiger voor? Welke het meeste?

Antwoord: [yasgui-link](https://yasgui.triply.cc/?query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT%20*%20WHERE%20%7B%0A%20%20%3Fsub%20%3Fpred%20%3Fobj%20.%0A%7D%20%0ALIMIT%2010&endpoint=http%3A%2F%2Fldf.fi%2Fmufi%2Fsparql#query=PREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20dct%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0ASELECT%20%3Fcreator%20%3FcreatorLabel%20(COUNT(%3Fcreator)%20AS%20%3FcreatorCount)%20WHERE%20%7B%0A%20%20%3Fding%20dct%3Acreator%20%3Fcreator%20.%0A%20%20%3Fcreator%20rdfs%3Alabel%20%3FcreatorLabel%20.%0A%7D%20%0AGROUP%20BY%20%3Fcreator%20%3FcreatorLabel%20%0AORDER%20BY%20DESC(%3FcreatorCount)&endpoint=https%3A%2F%2Fmediag.bunka.go.jp%2Fsparql&requestMethod=POST&tabTitle=Query%201&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 11.4
Zonder een query te maken: wat zou jij (als mens) denken dat die vervaardigers voor class's zijn? Hoe weet je dat?