

function sort( width, height, length, mass) { 
    
    // Calculate the volume of the package
    const volume = width * height * length;
    // Determine if the package is bulky
    const isBulky = volume >= 1000000 || width >= 150 || height >= 150 || length >= 150;
    // Determine if the package is heavy
    const isHeavy = mass >= 20;
    // Determine the stack based on the conditions

    if (isBulky && isHeavy) {
            return "REJECTED";
    } else if (isBulky || isHeavy) {
            return "SPECIAL";
    } else {
            return "STANDARD";
    }
}

console.log(sort(200, 100, 50, 10)); // Output: "SPECIAL" (bulky but not heavy)
console.log(sort(100, 100, 100, 25)); // Output: "SPECIAL" (heavy but not bulky)
console.log(sort(200, 200, 200, 25)); // Output: "REJECTED" (both bulky and heavy)
console.log(sort(50, 50, 50, 10)); // Output: "STANDARD" (neither bulky nor heavy)
