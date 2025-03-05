using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPSAssignment2
{
    class Vehicle
    {
        public string Brand { get; set; }
        public int Speed { get; set; }
        public Vehicle(string brand, int speed)
        {
            Brand = brand;
            Speed = speed;
        }
        public void Displayinfo()
        {
            Console.WriteLine("Brand: " + Brand);
            Console.WriteLine("Speed: " + Speed);
        }

    }
    class Car : Vehicle
    {
       
        public Car(string brand, int speed) : base(brand, speed)
        { 
        }
        

    }
    class Bike : Vehicle
    {
        public Bike(string brand, int speed) : base(brand, speed)
        {
        }
    }
}
