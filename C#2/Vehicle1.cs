using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPSAssignment2
{
    class Vehicle1
    {
        public string Brand { get; set; }
        public int Speed { get; set; }
        public Vehicle1(string brand, int speed)
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
    class Car1 : Vehicle1
    {
        public string Model { get; set; }
        public Car1(string brand, int speed, string model) : base(brand, speed)
        {
            Model = model;
        }

        //override Vehicle1 Displayinfo method in Car1 and Bike1 classes
        public void Displayinfo()
        {
            Console.WriteLine("Brand: " + Brand);
            Console.WriteLine("Speed: " + Speed);
            Console.WriteLine("Model: " + Model);
        }



    }
    class Bike1 : Vehicle1
    {
        public string Engine { get; set; }
        public Bike1(string brand, int speed, string engine) : base(brand, speed)
        {
            Engine = engine;

        }

        //override Vehicle1 Displayinfo method in Car1 and Bike1 classes
       public void Displayinfo()
        {
            Console.WriteLine("Brand: " + Brand);
            Console.WriteLine("Speed: " + Speed);
            Console.WriteLine("Engine: " + Engine);
        }
    }
}

