using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Intrinsics.X86;
using System.Text;
using System.Threading.Tasks;

namespace StudentValidation
{
    //**Decorator Pattern in a Logger System**

    //Implement an `ILogger` interface and `FileLogger` class. Use the ** Decorator Pattern** to add extra logging features like timestamp and error categorization.

    interface ILogger
    {
        public void Log(string message);
    }

}
