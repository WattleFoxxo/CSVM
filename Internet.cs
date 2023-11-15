using Newtonsoft.Json;
using System.Collections.Generic;
using static Home;
public class Modem
{
    public static Dictionary <string, object> Read(string json)
    {
        var data = JsonConvert.DeserializeObject<Dictionary<string, object>>(json);
         return  data;
    }

    pubstring Write(Dictionary<string, object> data)
    {
        var json = JsonConvert.SerializeObject(data);
         return  json;
    }
}