using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Intrinsics.X86;
using System.Text;
using System.Threading.Tasks;

namespace StudentValidation
{
    

    class FileLogger : ILogger
    {
        public void Log(string message)
        {
            Console.WriteLine("Logging to file: " + message);
        }
        public void timeStamp()
        {
            Console.WriteLine("Timestamp: " + DateTime.Now);
        }
        public void errorCategorization()
        {
            Console.WriteLine("Error categorization: " + "Critical");
        }
    }
}
