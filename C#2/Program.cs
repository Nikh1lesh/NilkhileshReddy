namespace OOPSAssignment2
{
    class Program
    {
        public void question1()
        {
            Vehicle car = new Car("Toyota", 100);
            Vehicle bike = new Bike("Yamaha", 80);
            car.Displayinfo();
            bike.Displayinfo();
        }
        public void question2()
        {
            Vehicle1 car = new Car1("Toyota", 100, "Camry");
            Vehicle1 bike = new Bike1("Yamaha", 80, "150cc");
            car.Displayinfo();
            bike.Displayinfo();
            Console.WriteLine("-------------------------------------------------");
            Car1 car1 = new Car1("Toyota", 100, "Camry");
            Bike1 bike1 = new Bike1("Yamaha", 80, "150cc");
            car1.Displayinfo();
            bike1.Displayinfo();
        }
        
        public void question3()
        {
            Manager manager = new Manager("John", 50000, 5000);
            Console.WriteLine("Name: " + manager.Name);
            Console.WriteLine("Salary: " + manager.Salary);
            Console.WriteLine("Bonus: " + manager.Bonus);
        }
        public void question4()
        {
            Animal dog = new Dog();
            Animal cat = new Cat();
            dog.MakeSound();
            cat.MakeSound();
        }
        public void question5()
        {
            Robot robot = new Robot();
            robot.Start();
            robot.Move();
        }
        public void question6()
        {
            SavingsAccount savingsAccount = new SavingsAccount();
            savingsAccount.CalculateInterest();
        }
        public void question7()
        {
            Duck duck = new Duck();
            duck.Fly();
            duck.Swim();
        }
        public void question8()
        {
            Student student = new Student("John", 20, 101);
            student.Displayinfo();
            Person person = student;
            person.Displayinfo();
            Student student1 = (Student)person;
            student1.Displayinfo();
        }
        public void question9()
        {
            ElectronicProduct electronicProduct = new ElectronicProduct("Laptop", 50000,"HP");
            Console.WriteLine("Discounted Price: "+electronicProduct.GetDiscountedPrice());
            ClothingProduct clothingProduct = new ClothingProduct("Shirt", 2000, "Cotton");
            Console.WriteLine("Discounted Price: " + clothingProduct.GetDiscountedPrice());
        }
        




            static void Main(string[] args)
        {

            Program program = new Program();
            //program.question1();
            //program.question2();
            //program.question3();
            //program.question4();
            //program.question5();
            //program.question6();
            //program.question7();
            //program.question8();
            program.question9();


        }
    }
}