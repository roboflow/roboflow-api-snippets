using System;
using System.IO;
using System.Net;
using System.Web;

namespace InferenceHosted
{
    class InferenceHosted
    {
        static void Main(string[] args)
        {
            string API_KEY = ""; // Your API Key
            string imageURL = "https://i.imgur.com/PEEvqPN.png";
            imageURL = HttpUtility.UrlEncode(imageURL);
            string MODEL_ENDPOINT = "xx-your-model--1"; // Set model endpoint

            // Construct the URL
            string uploadURL =
                    "https://infer.roboflow.com/" + MODEL_ENDPOINT
                    + "?access_token=" + API_KEY
                    + "&image=" + HttpUtility.UrlEncode(imageURL);

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
