using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace StudentValidation

{
   

class ComplexNumbers
    {
        public double Real { get; }
        public double Imaginary { get; }

       
        public ComplexNumbers(double real, double imaginary)
        {
            Real = real;
            Imaginary = imaginary;
        }

        public static ComplexNumbers operator +(ComplexNumbers c1, ComplexNumbers c2)
        {
            return new ComplexNumbers(c1.Real + c2.Real, c1.Imaginary + c2.Imaginary);
        }

        
    }
}
