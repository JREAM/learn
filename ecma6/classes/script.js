function init() {
    console.log('Init');
}

// Base Class
class Animal {

    constructor() {
        console.log('animal');
        this.legs = 4;
        this.ears = 2;
    }

    set_legs(num) {
        this.legs = num;
    }

    set_ears(num) {
        this.ears = num;
    }

    get_legs() {
        return this.legs;
    }

    get_ears() {
        return this.ears;
    }

}

// Child Class
class Whale extends Animal {
    constructor() {
        super();
        this.legs = 0;
        this.ears = 0;
    }
}

class Dog extends Animal {
    constructor() {
        super();
    }
}

whale = new Whale();
console.log(whale.get_ears());
console.log(whale.get_legs());

dog = new Dog();
console.log(dog.get_ears());
console.log(dog.get_legs());