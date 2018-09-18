//Do you like alface?
var eatsPlants = false;
//What about bacon?
var eatsAnimals = true;
//category receives 2 boolean conditions inside 1 boolean condition, beautiful isn't it?
var category = (eatsPlants ? (eatsAnimals ? "omnivore" : "herbivore") : (eatsAnimals ? "carnivore" : undefined));
//prints category.
console.log(category);
