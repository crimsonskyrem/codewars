function prod(int: number): number[] {
  const arr = [];
  const res = [];
  for (let i = 0; i < int; i++) {
    arr.push(1);
    res.push(i + 1);
  }
  for (let i = 1; i <= int / 2; i++) {
    let copy = [...arr];
    let left = copy.splice(0, i);
    res.push(copy.reduce((a, b) => a + b) * left.reduce((a, b) => a + b));
  }

  return res;
}

function test() {
  // 5 [4, 3] 25 9
  // 7 [6, 3, 2] 13 4
  // 10 [8, 6] 36
  // 11 [10, 4, 2, 1] 21 5 1
  // 50 [49, 8, 5, 3, 1]  99 35 10
  // 50 [49, 9, 4, 1, 1]  99 18 2 1
  // 52 [50, 13, 5, 3, 1] 204 35 10
  console.log(prod(8));
}
export { test };
