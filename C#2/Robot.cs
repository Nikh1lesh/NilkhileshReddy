using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPSAssignment2
{
    class Robot : Machine,IMovable
    {
        public void Move()
        {
            // Implementation of the Move method
            Console.WriteLine("Robot is moving.");
        }
        
    }
}
