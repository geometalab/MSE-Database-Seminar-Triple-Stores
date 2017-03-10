queries = dict()

queries['query_1'] = """
        PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT DISTINCT ?product ?label
            WHERE {
                ?product rdfs:label ?label .
                ?product rdf:type <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType2> .
                ?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature12> .
                ?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature20> .
                ?product bsbm:productPropertyNumeric1 ?value1 .
                FILTER (?value1 > 348)
                }
        ORDER BY ?label
        LIMIT 10
        """

queries['query_2'] = """
        PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
        PREFIX inst: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromProducer1/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dc: <http://purl.org/dc/elements/1.1/>

        SELECT ?label ?comment ?producer ?productFeature ?propertyTextual1 ?propertyTextual2 ?propertyTextual3
            ?propertyNumeric1 ?propertyNumeric2 ?propertyTextual4 ?propertyTextual5 ?propertyNumeric4
        WHERE {
            inst:Product5 rdfs:label ?label .
            inst:Product5 rdfs:comment ?comment . inst:Product5
            bsbm:producer ?p .
            ?p rdfs:label ?producer .
            inst:Product5 dc:publisher ?p .
            inst:Product5 bsbm:productFeature ?f .
            ?f rdfs:label ?productFeature .
            inst:Product5 bsbm:productPropertyTextual1 ?propertyTextual1 .
            inst:Product5 bsbm:productPropertyTextual2 ?propertyTextual2 .
            inst:Product5 bsbm:productPropertyTextual3 ?propertyTextual3 .
            inst:Product5 bsbm:productPropertyNumeric1 ?propertyNumeric1 .
            inst:Product5 bsbm:productPropertyNumeric2 ?propertyNumeric2 .

            OPTIONAL {inst:Product5 bsbm:productPropertyTextual4 ?propertyTextual4 }
            OPTIONAL {inst:Product5 bsbm:productPropertyTextual5 ?propertyTextual5 }
            OPTIONAL {inst:Product5 bsbm:productPropertyNumeric4 ?propertyNumeric4 }
        }
        """

queries['query_3'] = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>

        SELECT ?product ?label
        WHERE {
            ?product rdfs:label ?label .
            ?product rdf:type <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType2> .
            ?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature12> .
            ?product bsbm:productPropertyNumeric1 ?p1 .
            FILTER ( ?p1 > 214 )
            ?product bsbm:productPropertyNumeric3 ?p3 .
            FILTER (?p3 < 698 )

            OPTIONAL {
                ?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature20> .
                ?product rdfs:label ?testVar
            }

            FILTER (!bound(?testVar))
        }
        ORDER BY ?label
        LIMIT 10
        """

queries['query_4'] = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>

        SELECT ?product ?label
        WHERE {
            {
                ?product rdfs:label ?label .
                ?product rdf:type <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType2> .
                ?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature12> .
                ?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature20> .
                ?product bsbm:productPropertyNumeric1 ?value1 .
                FILTER (?value1 > 348)
            }
            UNION
            {
                ?product rdfs:label ?label .
                ?product rdf:type <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType1> .
                ?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature12> .
                ?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature8> .
                ?product bsbm:productPropertyNumeric2 ?p2 .
                FILTER ( ?p2>759 )
            }
        }
        ORDER BY ?label
        LIMIT 10
        OFFSET 10
        """

queries['query_5'] = """
        PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX inst: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromProducer1/>

        SELECT DISTINCT ?product ?productLabel
        WHERE {
            ?product rdfs:label ?productLabel .
            FILTER (inst:Product6 != ?product)
            inst:Product6 bsbm:productFeature ?prodFeature .
            ?product bsbm:productFeature ?prodFeature .
            inst:Product6 bsbm:productPropertyNumeric1 ?origProperty1 .
            ?product bsbm:productPropertyNumeric1 ?simProperty1 .

            FILTER (?simProperty1 < (?origProperty1 + 120) && ?simProperty1 > (?origProperty1 - 120))
            inst:Product6 bsbm:productPropertyNumeric2 ?origProperty2 .
            ?product bsbm:productPropertyNumeric2 ?simProperty2 .

            FILTER (?simProperty2 < (?origProperty2 + 170) && ?simProperty2 > (?origProperty2 - 170))
        }
        ORDER BY ?productLabel
        LIMIT 5
        """

queries['query_6'] = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>

        SELECT ?product ?label
        WHERE {
            ?product rdfs:label ?label .
            ?product rdf:type bsbm:Product .
            FILTER regex(?label, "r")
        }
        """

queries['query_7'] = """
        PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dc: <http://purl.org/dc/elements/1.1/>
        PREFIX rev: <http://purl.org/stuff/rev#>

        SELECT ?productLabel ?offer ?price ?vendor ?vendorTitle ?review ?revTitle ?reviewer ?revName ?rating1 ?rating2
        WHERE {
            <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromProducer1/Product5> rdfs:label ?productLabel .

            OPTIONAL {
                ?offer bsbm:product <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromProducer1/Product5> .
                ?offer bsbm:price ?price .
                ?offer bsbm:vendor ?vendor .
                ?vendor rdfs:label ?vendorTitle .
                ?vendor bsbm:country <http://downlode.org/rdf/iso-3166/countries#DE> .
                ?offer dc:publisher ?vendor .
                ?offer bsbm:validTo ?date .
                FILTER (?date > 2001-09-16 )
            }
            OPTIONAL {
                ?review bsbm:reviewFor <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromProducer1/Product5> .
                ?review rev:reviewer ?reviewer .
                ?reviewer foaf:name ?revName .
                ?review dc:title ?revTitle .

                OPTIONAL { ?review bsbm:rating1 ?rating1 . }
                OPTIONAL { ?review bsbm:rating2 ?rating2 . }
            }
        }
        """

queries['query_8'] = """
        PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
        PREFIX dc: <http://purl.org/dc/elements/1.1/>
        PREFIX rev: <http://purl.org/stuff/rev#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX inst:<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromProducer1/>

        SELECT ?title ?text ?reviewDate ?reviewer ?reviewerName ?rating1 ?rating2 ?rating3 ?rating4
        WHERE {
            ?review bsbm:reviewFor inst:Product6 .
            ?review dc:title ?title .
            ?review rev:text ?text .
            FILTER langMatches( lang(?text), "EN" )
            ?review bsbm:reviewDate ?reviewDate .
            ?review rev:reviewer ?reviewer .
            ?reviewer foaf:name ?reviewerName .

            OPTIONAL { ?review bsbm:rating1 ?rating1 . }
            OPTIONAL { ?review bsbm:rating2 ?rating2 . }
            OPTIONAL { ?review bsbm:rating3 ?rating3 . }
            OPTIONAL { ?review bsbm:rating4 ?rating4 . }
        }
        ORDER BY DESC(?reviewDate)
        LIMIT 20
        """

# queries['query_9'] = """
#         PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#         PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#         PREFIX rev: <http://purl.org/stuff/rev#>
#
#         DESCRIBE ?x
#         WHERE {
#             <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromRatingSite1/Review4> rev:reviewer ?x
#         }
#         """

queries['query_10'] = """
        PREFIX dc: <http://purl.org/dc/elements/1.1/>
        PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

        SELECT DISTINCT ?offer ?price
        WHERE {
            ?offer bsbm:product <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromProducer1/Product1> .
            ?offer bsbm:vendor ?vendor .
            ?offer dc:publisher ?vendor .
            ?vendor bsbm:country <http://downlode.org/rdf/iso-3166/countries#GB> .
            ?offer bsbm:deliveryDays ?deliveryDays .

            FILTER (?deliveryDays <= 3)

            ?offer bsbm:price ?price .
            ?offer bsbm:validTo ?date .

            FILTER (?date > "2008-04-19T00:00:00"^^xsd:dateTime)
        }
        ORDER BY xsd:double(str(?price))
        LIMIT 10
        """

queries['query_11'] = """
        SELECT ?property ?hasValue ?isValueOf
        WHERE
        {
            {
                <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromVendor1/Offer1> ?property ?hasValue
            }
            UNION
            {
                ?isValueOf ?property <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromVendor1/Offer1>
            }
        }
        """

queries['query_12'] = """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX rev: <http://purl.org/stuff/rev#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
        PREFIX bsbm-export: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/export/>
        PREFIX dc: <http://purl.org/dc/elements/1.1/>

        CONSTRUCT {
            <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromVendor1/Offer1> bsbm-export:product ?productURI .
            <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromVendor1/Offer1> bsbm-export:productlabel ?productlabel .
            <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromVendor1/Offer1> bsbm-export:vendor ?vendorname .
            <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromVendor1/Offer1> bsbm-export:vendorhomepage ?vendorhomepage .
            <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromVendor1/Offer1> bsbm-export:offerURL ?offerURL .
            <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromVendor1/Offer1> bsbm-export:price ?price .
            <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromVendor1/Offer1> bsbm-export:deliveryDays ?deliveryDays .
            <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromVendor1/Offer1> bsbm-export:validuntil ?validTo
        }

        WHERE {
            <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromVendor1/Offer1> bsbm:product ?productURI .
            ?productURI rdfs:label ?productlabel .
            <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromVendor1/Offer1> bsbm:vendor ?vendorURI .
            ?vendorURI rdfs:label ?vendorname .
            ?vendorURI foaf:homepage ?vendorhomepage .
            <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromVendor1/Offer1> bsbm:offerWebpage ?offerURL .
            <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromVendor1/Offer1> bsbm:price ?price .
            <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromVendor1/Offer1> bsbm:deliveryDays ?deliveryDays .
            <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromVendor1/Offer1> bsbm:validTo ?validTo
        }
        """
