import java.io.*
import java.net.HttpURLConnection
import java.net.URL
import java.nio.charset.StandardCharsets
import java.util.*

fun main() {
    // Get Image Path
    val filePath = System.getProperty("user.dir") + System.getProperty("file.separator") + "YOUR_IMAGE.jpg"
    val file = File(filePath)

    // Base 64 Encode
    val encodedFile: String
    val fileInputStreamReader = FileInputStream(file)
    val bytes = ByteArray(file.length().toInt())
    fileInputStreamReader.read(bytes)
    encodedFile = String(Base64.getEncoder().encode(bytes), StandardCharsets.US_ASCII)
    val API_KEY = "" // Your API Key
    val MODEL_ENDPOINT = "dataset/v" // Set model endpoint (Found in Dataset URL)

    // Construct the URL
    val uploadURL ="https://detect.roboflow.com/" + MODEL_ENDPOINT + "?api_key=" + API_KEY + "&name=YOUR_IMAGE.jpg";

    // Http Request
    var connection: HttpURLConnection? = null
    try {
        // Configure connection to URL
        val url = URL(uploadURL)
        connection = url.openConnection() as HttpURLConnection
        connection.requestMethod = "POST"
        connection.setRequestProperty("Content-Type",
                "application/x-www-form-urlencoded")
        connection.setRequestProperty("Content-Length",
                Integer.toString(encodedFile.toByteArray().size))
        connection.setRequestProperty("Content-Language", "en-US")
        connection.useCaches = false
        connection.doOutput = true

        //Send request
        val wr = DataOutputStream(
                connection.outputStream)
        wr.writeBytes(encodedFile)
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