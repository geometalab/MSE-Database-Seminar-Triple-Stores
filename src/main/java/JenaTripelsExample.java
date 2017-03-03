import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class JenaTripelsExample {

    public static void main(String[] args) throws FileNotFoundException {
        Model model = ModelFactory.createDefaultModel();
        ClassLoader classLoader = JenaTripelsExample.class.getClassLoader();
        FileInputStream in = new FileInputStream(classLoader.getResource("dataset.ttl").getFile());
        model.read(in, null, "TTL");
        showModelSize(model);
    }

    private static void showModelSize(Model m) {
        System.out.println(String.format("The model contains %d triples", m.size()));
    }
}
