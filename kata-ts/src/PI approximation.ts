function iterPi(epsilon: number): number[] {
    let plus:Boolean = false
    let aprox : number = 4
    let times : number = 1
    while (Math.abs(Math.PI - aprox) > epsilon) {
        if (plus) {
            aprox += (4 / (2 * times + 1));
        } else {
            aprox -= (4 / (2 * times + 1));
        }
        plus = !plus;
        times++;
    }
    aprox = Number(aprox.toPrecision(10))
    return [times, aprox];
}

console.log(iterPi(0.1));
