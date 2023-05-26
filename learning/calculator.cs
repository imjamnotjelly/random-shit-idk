using System;

namespace multifunctioncalculator
{
    internal class Program
    {
        public static void Main (string[] args) {
            Console.Title = "Multi-Function Calculator";
            double memory = 0,total_num = 0;
            string op;
            Console.WriteLine("Here are the set of available actions: ");
            Console.WriteLine("[ + | add ],  [ - | subtract ], [ * | x | multiply ], [ / | divide ], [ % | modulo ], [ ^ | square_root ] \n[ c | clear ], [ cv | current_val ],  [ m | write_to_memory ], [ e | end ]\n");
            while (true)
            {
                Console.Write("Enter an operation: ");
                op = Console.ReadLine()?.ToLower();
                switch (op)
                {
                    case var s when s == "add" || s == "+":
                        total_num += return_num();
                        break;
                    case var s when s == "subtract" || s == "-":
                        total_num -= return_num();
                        break;
                    case var s when s == "multiply" || s == "*" || s == "x":
                        total_num *= return_num();
                        break;
                    case var s when s == "divide" || s == "/":
                        total_num /= return_num();
                        break;
                    case var s when s == "modulo" || s == "%":
                        total_num %= return_num();
                        break;
                    case var s when s == "square_root" || s == "^":
                        total_num = Math.Sqrt(total_num);
                        break;
                    case var s when s == "clear" || s == "c":
                        total_num = 0;
                        break;
                    case var s when s =="cv" || s == "current_val":
                        break;
                    case var s when s == "write_to_memory" || s == "m":
                        memory += total_num;
                        Console.WriteLine($"Memory: {memory}");
                        break;
                    case var s when s == "end" || s == "e":
                        Console.ForegroundColor = ConsoleColor.DarkRed;
                        Console.WriteLine("Closing...");
                        return;
                    default:
                        Console.ForegroundColor = ConsoleColor.DarkRed;
                        Console.WriteLine("Invalid operation.");
                        Console.ResetColor();
                        break;

                }

                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine($"Your current value is: {total_num}");
                Console.ResetColor();
            }

            double return_num() {
                Console.Write("Enter a value (or type 'mem' to enter saved value): ");
                string input = Console.ReadLine();
                return (input == "mem" ?  memory: Convert.ToDouble(input));
            }
        }
    }
}
