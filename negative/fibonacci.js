fibonaccis_reversed = [1, 1, 0]

function prev_fibonacci(n1, n2) {
    return n2 - n1;
}

for (let x = 0; x < 50; x++) {
    fibonaccis_reversed.push(prev_fibonacci(fibonaccis_reversed[fibonaccis_reversed.length - 1], fibonaccis_reversed[fibonaccis_reversed.length - 2]))
}


console.log(fibonaccis_reversed)
