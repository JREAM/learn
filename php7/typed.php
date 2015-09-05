<?php
# Force Type Hinting and Return Types
declare(strict_types = 1); # Seems to not do anything
error_reporting(E_ALL | E_STRICT); # This is required to enforce the below

# These aliases are removed:
# interger is now always: int
# boolean is now always:  bool

function foo(): string {
    return 'hello';
}

echo foo();

// dont use 'object' non scalar
function bar($name, int $age, bool $alive, float $money): stdClass {
    $person = new \stdClass();
    $person->name = $name;
    $person->age = $age;
    $person->alive = $alive;
    $person->money = $money;

    return $person;
}

var_dump(bar('jesse', 25, true, 310.25));

# Prevent Null
// function baz(): bool {
//     return null;
// }
// baz();

# Doesnt work
// function boo(): void {
    // valid
// }
// boo();


class User {

    // Can't declare return type:
    // public function __construct(): bool {
    //     return true;
    // }
    public function get(): self {
        return self;
    }

}

class Profile extends User {


    public function getUser(int $id): parent {
        return new User();
    }

}

$p = new  Profile;
$result = $p->getUser(1);
var_dump($result);
