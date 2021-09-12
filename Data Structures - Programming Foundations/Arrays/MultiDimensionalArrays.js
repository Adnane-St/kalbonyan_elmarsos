//This is Restaurant menu table two Diman
var dinnerMenue = [['Tajine','Foul','Cafe'],['Dajaj','Batata','CocaCola']]; 

let appIndex = 0;
let maindishIndex = 1;

let firstApp = dinnerMenue[appIndex][0];
let secondApp = dinnerMenue[appIndex][1];
let thirdMainDish = dinnerMenue[maindishIndex][2];

console.log(firstApp);
console.log(secondApp);
console.log(thirdMainDish);

dinnerMenue[maindishIndex][0] = "Steak";

console.log(dinnerMenue[maindishIndex][0]);

console.log(dinnerMenue);