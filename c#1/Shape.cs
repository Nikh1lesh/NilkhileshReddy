using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StudentValidation
{
    public class Shape
    {
        public virtual double Area()
        {
            return 0;
        }
    }
    class Circle : Shape
    {
        private double radius;
        public Circle(double radius)
        {
            Radius = radius;
        }
        public double Radius
        {
            get { return radius; }
            set
            {
                if (value < 0)
                {
                    throw new Exception("Radius cannot be negative");
                }
                radius = value;
            }
        }
        public override double Area()
        {
            return Math.PI * radius * radius;
        }
    }
    public class Rectangle : Shape
    {
        private double length;
        private double breadth;
        public Rectangle(double length, double breadth)
        {
            Length = length;
            Breadth = breadth;
        }
        public double Length
        {
            get { return length; }
            set
            {
                if (value < 0)
                {
                    throw new Exception("Length cannot be negative");
                }
                length = value;
            }
        }
        public double Breadth
        {
            get { return breadth; }
            set
            {
                if (value < 0)
                {
                    throw new Exception("Breadth cannot be negative");
                }
                breadth = value;
            }
        }
        public override double Area()
        {
            return length * breadth;
        }
    }
}
