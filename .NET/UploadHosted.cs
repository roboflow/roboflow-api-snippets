using System;
using System.IO;
using System.Net;
using System.Text;
using System.Web;

namespace UploadHosted
{
    class UploadHosted
    {
        static void Main(string[] args)
        {
            string API_KEY = ""; // Your API Key
            string DATASET_NAME = "your-dataset"; // Set Dataset Name (Found in Dataset URL)
            string imageURL = "https://i.imgur.com/PEEvqPN.png";
            imageURL = HttpUtility.UrlEncode(imageURL);

            // Construct the URL
            string uploadURL =
                    "https://api.roboflow.com/dataset/" +
                            DATASET_NAME + "/upload" +
                            "?api_key=" + API_KEY +
                            "&name=YOUR_IMAGE.jpg" +
                            "&split=train" +
                            "&image=" + imageURL;

            // Service Point Config
            ServicePointManager.Expect100Continue = true;
            ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;

            // Configure Http Request
            WebRequest request = WebRequest.Create(uploadURL);
            request.Method = "POST";
            request.ContentType = "application/x-www-form-urlencoded";
            request.ContentLength = 0;

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
