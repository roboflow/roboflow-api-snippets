import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

public class UploadHosted {
    public static void main(String[] args) {
        String imageURL = "https://i.imgur.com/PEEvqPN.png"; // Replace Image URL
        String API_KEY = ""; // Your API Key
        String DATASET_NAME = "your-dataset"; // Set Dataset Name (Found in Dataset URL)

        // Upload URL
        String uploadURL = "https://api.roboflow.com/dataset/" + DATASET_NAME + "/upload" + "?api_key=" + API_KEY
                + "&name=YOUR_IMAGE.jpg" + "&split=train" + "&image="
                + URLEncoder.encode(imageURL, StandardCharsets.UTF_8);

        // Http Request
        HttpURLConnection connection = null;
        try {
            // Configure connection to URL
            URL url = new URL(uploadURL);
            connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");

            connection.setRequestProperty("Content-Length", Integer.toString(uploadURL.getBytes().length));
            connection.setRequestProperty("Content-Language", "en-US");
            connection.setUseCaches(false);
            connection.setDoOutput(true);

            // Send request
            DataOutputStream wr = new DataOutputStream(connection.getOutputStream());
            wr.writeBytes(uploadURL);
            wr.close();

            // Get Response
            InputStream stream = connection.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(stream));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
            reader.close();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (connection != null) {
                connection.disconnect();
            }
        }
    }
}
