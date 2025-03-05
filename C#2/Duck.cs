using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPSAssignment2
{
    class Duck: IFlyabble, ISwimmable
    {
        public void Fly()
        {
            Console.WriteLine("Duck is flying");
        
        public void Swim()
        {
            Console.WriteLine("Duck is swimming");
        }
    }
    
}
