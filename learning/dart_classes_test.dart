class Toaster {
  List<String> toaststates = ["Uncooked", "Perfectly Ready", "Overcooked", "Burnt"];
  String toaststate = "Uncooked";
  bool inserted = false;
  String name;

  Toaster(String name) {
    this.name = name;
    // Naming the toast is essencial
  }
  
  MoveToast(bool inserted) {
    this.inserted = inserted;
  }
  
  CookToast() {
    toaststate = toaststates[toaststates.indexOf(toaststate)+1];
  }
}

abstract class Example {
  void example();
}

class AnotherExample implements Example { 
  void example() {
  }
}

void main() {
  Toaster t = Toaster();
  print(t.toaststate);
}