<?php

function foo(): string {
    return 'hello';
}

echo foo();

// dont use 'object' non scalar
function bar(string $name, int $age, bool $alive, float $money): stdClass {
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
