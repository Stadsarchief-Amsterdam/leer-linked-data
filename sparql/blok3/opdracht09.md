# Opdracht 9
We gaan nog meer oefenen met RiC-O op het ALEGORIA-endpoint. In deze oefening bouwen we geleidelijk aan een SPARQL query om te leren hoe dat opbouwen meestal stapje voor stapje gebeurt.

We willen uiteindelijk alle foto's waarop (een stukje van) de region Bourgogne-Franche-Comte is afgebeeld. Dat gaat niet zomaar, want niet alle foto's zijn (direct) gekoppeld aan de URI voor Bourgogne-Franche-Comte.

## 9.1
Vraag de URI en het label van de region met nummer "27" (de code voor Bourgogne-Franche-Comte). De property daarvoor is: <http://rdf.insee.fr/def/geo#codeRegion>.

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rico%3A%20%3Chttps%3A%2F%2Fwww.ica.org%2Fstandards%2FRiC%2Fontology%23%3E%0A%0ASELECT%20%3FregionLabel%20WHERE%20%7B%0A%20%20%3Fregion%20%3Chttp%3A%2F%2Frdf.insee.fr%2Fdef%2Fgeo%23codeRegion%3E%20%2227%22%20%3B%0A%20%20%20%20%20%20%20%20%20%20rdfs%3Alabel%20%3FregionLabel%20.%0A%7D&endpoint=http%3A%2F%2Fdata.alegoria-project.fr%2Fsparql%2F&requestMethod=POST&tabTitle=Query%201&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 9.2
Alle departementen en communes zijn als een boom aan Bourgogne-Franche-Comte gekoppeld. Dus: commune X rico:isOrWasContainedBy departement Y rico:isOrWasContainedBy Bourgogne-Franche-Comte. Let op: deze property wijst in de hierarchie dus van de onderliggende plaats naar boven. Breid de query uit. Zoek alle departementen en communes in Bourgogne-Franche-Comte. Geef de labels.

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rico%3A%20%3Chttps%3A%2F%2Fwww.ica.org%2Fstandards%2FRiC%2Fontology%23%3E%0A%0ASELECT%20%3FregionLabel%20%3FplaceLabel%20WHERE%20%7B%0A%20%20%3Fregion%20%3Chttp%3A%2F%2Frdf.insee.fr%2Fdef%2Fgeo%23codeRegion%3E%20%2227%22%20%3B%0A%20%20%20%20%20%20%20%20%20%20rdfs%3Alabel%20%3FregionLabel%20.%0A%20%20%3Fplace%20rico%3AisOrWasContainedBy%2B%20%3Fregion%20%3B%0A%20%20%20%20%20%20%20%20%20rdfs%3Alabel%20%3FplaceLabel%20.%0A%7D&endpoint=http%3A%2F%2Fdata.alegoria-project.fr%2Fsparql%2F&requestMethod=POST&tabTitle=Query%201&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

## 9.3
Laatste stap: zoek alle rico:Record's waarvan de rico:hasOrHadMainSubject een van de plaatsen in Bourgogne-Franche-Comte is.

Antwoord: [yasgui-link](http://yasgui.triply.cc/#query=PREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rico%3A%20%3Chttps%3A%2F%2Fwww.ica.org%2Fstandards%2FRiC%2Fontology%23%3E%0A%0ASELECT%20%3FregionLabel%20%3FplaceLabel%20%3FrecordLabel%20WHERE%20%7B%0A%20%20%3Fregion%20%3Chttp%3A%2F%2Frdf.insee.fr%2Fdef%2Fgeo%23codeRegion%3E%20%2227%22%20%3B%0A%20%20%20%20%20%20%20%20%20%20rdfs%3Alabel%20%3FregionLabel%20.%0A%20%20%3Fplace%20rico%3AisOrWasContainedBy%2B%20%3Fregion%20%3B%0A%20%20%20%20%20%20%20%20%20rdfs%3Alabel%20%3FplaceLabel%20.%0A%20%20%3Frecord%20rdf%3Atype%20rico%3ARecord%20%3B%0A%20%20%20%20%20%20%20%20%20%20rico%3AhasOrHadMainSubject%20%3Fplace%20%3B%0A%20%20%20%20%20%20%20%20%20%20rdfs%3Alabel%20%3FrecordLabel%20.%0A%7D&endpoint=http%3A%2F%2Fdata.alegoria-project.fr%2Fsparql%2F&requestMethod=POST&tabTitle=Query%201&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table)

Einde blok 3
