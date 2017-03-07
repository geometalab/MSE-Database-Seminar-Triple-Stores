import org.apache.jena.query.*;
import org.apache.jena.rdf.model.*;

import java.io.FileNotFoundException;
import java.io.InputStream;


public class JenaTripelsExample {

    public static void main(String[] args) throws FileNotFoundException {
        Model model = ModelFactory.createDefaultModel();
        ClassLoader classLoader = JenaTripelsExample.class.getClassLoader();
        InputStream in = classLoader.getResourceAsStream("dataset.ttl");
        //InputStream in = classLoader.getResourceAsStream("scale10000.ttl");
        model.read(in, null, "TTL");
        showModelSize(model);
        query(model);
    }

    private static void showModelSize(Model m) {
        System.out.println(String.format("The model contains %d triples", m.size()));
    }

    private static void query(Model model) {
        String queryString = "\n" +
                "PREFIX bsbm-inst: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/>\n" +
                "PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>\n" +
                "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n" +
                "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n" +
                "\n" +
                "SELECT DISTINCT ?product ?label\n" +
                "WHERE { \n" +
                " ?product rdfs:label ?label .\n" +
                "\t}\n" +
                "ORDER BY ?label\n" +
                "LIMIT 10";

        try {
            Query query = QueryFactory.create(queryString);

            try (QueryExecution qexec = QueryExecutionFactory.create(query, model)) {
                ResultSet results = qexec.execSelect();
                for (; results.hasNext(); ) {
                    QuerySolution soln = results.nextSolution();
                    System.out.println(soln.toString());
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
