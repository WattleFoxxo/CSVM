using static Home;
using System.Collections.Generic;
using System;
using System.IO;
using System.Net.Http;
using System.Threading.Tasks;
 namespace  updater
{
	class thing
	{
		public static async Task DownloadFileFromGithubAsync(string url, string destinationPath)
		{
		    using (HttpClient client = new HttpClient())
		    {
		        using (HttpResponseMessage response = await client.GetAsync(url))
		        {
		            using (Stream stream = await response.Content.ReadAsStreamAsync())
		            {
		                using (FileStream fileStream = new FileStream(destinationPath, FileMode. new ))
		                {
		                    await stream.CopyToAsync(fileStream);
		                }
		            }
		        }
		    }
		}	
		 public static async Task Main(string[] args)
		{
		    // app updater
		    await DownloadFileFromGithubAsync("https://github.com/charlie-sans/CVSM-Repo/releases/download/v1.2/CubeScript-1.2.zip", "./");
		}
	}
}