using System;
using System.Buffers.Text;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StudentValidation
{
    //**Factory Pattern for Object Creation**

    //Implement a `VehicleFactory` class that returns different vehicle objects(`Car`, `Bike`) based on an input parameter.
    class VehicleFactory
    {
        public Vehicle GetVehicle(string vehicleType)
        {
            if (vehicleType == null)
            {
                return null;
            }
            if (vehicleType.Equals("Car"))
            {
                return new Car();
            }
            else if (vehicleType.Equals("Bike"))
            {
                return new Bike();
            }
            return null;
        }
    }


}
