using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPSAssignment2
//Create a base class `Product` with properties `Name` and `Price`. Derive two classes `ElectronicProduct` and `ClothingProduct`. Add a `GetDiscountedPrice()` method in the base class and override it in the derived classes to apply different discount rules.
{
    class Product
    {
        public string Name { get; set; }
        public double Price { get; set; }
        public Product(string name, double price)
        {
            Name = name;
            Price = price;
        }
        public virtual double GetDiscountedPrice()
        {
            return Price; 
        }
    }
    class ElectronicProduct : Product
    {
        public string Quality { get; set; }
        public ElectronicProduct(string name, double price, string quality) : base(name, price)
        {
            Quality = quality;
        }
        public override double GetDiscountedPrice()
        {
            return Price * 0.9;
        }
    }
    class ClothingProduct : Product
    {
        public string Brand { get; set; }
        public ClothingProduct(string name, double price, string brand) : base(name, price)
        {
            Brand = brand;
        }
        public override double GetDiscountedPrice()
        {
            return Price * 0.6;
        }
    }
}
