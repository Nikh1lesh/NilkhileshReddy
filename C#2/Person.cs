using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPSAssignment2
{
    //Time: 15 mins
    //Create a base class `Person` and derive a class `Student`. Create an object of `Student`, upcast it to `Person`, and then downcast it back to `Student`. Demonstrate how type casting works.

    class Person
    {
        public string Name { get; set; }
        public int Age { get; set; }
        public Person(string name, int age)
        {
            Name = name;
            Age = age;
        }
        public void Displayinfo()
        {
            Console.WriteLine("Name: " + Name);
            Console.WriteLine("Age: " + Age);
        }
    }
    class Student : Person
    {
        public int RollNo { get; set; }
        public Student(string name, int age, int rollno) : base(name, age)
        {
            RollNo = rollno;
        }
        public void Displayinfo()
        {
            Console.WriteLine("Name: " + Name);
            Console.WriteLine("Age: " + Age);
            Console.WriteLine("Roll No: " + RollNo);
        }
    }
}
