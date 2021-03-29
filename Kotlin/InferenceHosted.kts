import java.io.BufferedReader
import java.io.DataOutputStream
import java.io.InputStreamReader
import java.net.HttpURLConnection
import java.net.URL
import java.net.URLEncoder
import java.nio.charset.StandardCharsets

fun main() {
    val imageURL = "https://i.imgur.com/PEEvqPN.png" // Replace Image URL
    val API_KEY = "" // Your API Key
    val MODEL_ENDPOINT = "xx-your-model--1" // Set model endpoint

    // Upload URL
    val uploadURL = "https://infer.roboflow.com/" + MODEL_ENDPOINT + "?access_token=" + API_KEY + "&image="
                + URLEncoder.encode(imageURL, "utf-8");

    // Http Request
    var connection: HttpURLConnection? = null
    try {
        // Configure connection to URL
        val url = URL(uploadURL)
        connection = url.openConnection() as HttpURLConnection
        connection.requestMethod = "POST"
        connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded")
        connection.setRequestProperty("Content-Length", Integer.toString(uploadURL.toByteArray().size))
        connection.setRequestProperty("Content-Language", "en-US")
        connection.useCaches = false
        connection.doOutput = true

        // Send request
        val wr = DataOutputStream(connection.outputStream)
        wr.writeBytes(uploadURL)
        wr.close()

        // Get Response
        val stream = connection.inputStream
        val reader = BufferedReader(InputStreamReader(stream))
        var line: String?
        while (reader.readLine().also { line = it } != null) {
            println(line)
        }
        reader.close()
    } catch (e: Exception) {
        e.printStackTrace()
    } finally {
        connection?.disconnect()
    }
}

main()