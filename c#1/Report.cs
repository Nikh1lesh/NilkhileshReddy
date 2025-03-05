using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StudentValidation
{
    class Report : IPrintable, ISerializable
    {
        public void Print()
        {
            Console.WriteLine("Printing Report");
        }
        public void Serialize()
        {
            Console.WriteLine("Serializing Report");
        }
    }
    
}
