using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StudentValidation
{
    class Vehicle
    {
        public virtual void start()
        {
            Console.WriteLine("Vehicle started");
        }
    }
    class Car : Vehicle
    {
        public override void start()
        {
            Console.WriteLine("Car started");
        }

    }
    class Bike : Vehicle
    {
        public override void start()
        {
            Console.WriteLine("Bike started");
        }
    }
}
