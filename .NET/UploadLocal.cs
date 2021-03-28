using System;
using System.IO;
using System.Net;
using System.Text;

namespace UploadLocal
{
    class UploadLocal
    {

        static void Main(string[] args)
        {
            byte[] imageArray = System.IO.File.ReadAllBytes(@"YOUR_IMAGE.jpg");
            string encoded = Convert.ToBase64String(imageArray);
            byte[] data = Encoding.ASCII.GetBytes(encoded);
            string API_KEY = ""; // Your API Key
            string DATASET_NAME = "your-dataset"; // Set Dataset Name (Found in Dataset URL)

            // Construct the URL
            string uploadURL =
                    "https://api.roboflow.com/dataset/" +
                            DATASET_NAME + "/upload" +
                            "?api_key=" + API_KEY +
                            "&name=YOUR_IMAGE.jpg" +
                            "&split=train";

            // Service Request Config
            ServicePointManager.Expect100Continue = true;
            ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;

            // Configure Request
            WebRequest request = WebRequest.Create(uploadURL);
            request.Method = "POST";
            request.ContentType = "application/x-www-form-urlencoded";
            request.ContentLength = data.Length;

            // Write Data
            using (Stream stream = request.GetRequestStream())
            {
                stream.Write(data, 0, data.Length);
            }

            // Get Response
            string responseContent = null;
            using (WebResponse response = request.GetResponse())
            {
                using (Stream stream = response.GetResponseStream())
                {
                    using (StreamReader sr99 = new StreamReader(stream))
                    {
                        responseContent = sr99.ReadToEnd();
                    }
                }
            }

            Console.WriteLine(responseContent);

        }
    }
}
